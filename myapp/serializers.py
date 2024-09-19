from rest_framework import serializers
from rest_framework.relations import StringRelatedField
import datetime
from myapp.models import User, Ad, Booking, Review
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
import re


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(max_length=50, write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'is_landlord', 'is_renter', 'password','re_password']
        extra_kwargs = {'password': {'write_only': True}}
        ordering = ['email']

    def validate(self, data):
        name = data.get('name')

        if not re.match('^.{0,20}$', name):
            raise serializers.ValidationError({"name": "Ensure this field has no more than 20 characters."})

        password = data.get("password")
        re_password = data.get("re_password")

        if password != re_password:
            raise serializers.ValidationError({"password": "Passwords don't match."})

        try:
            validate_password(password)
        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        return data

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('re_password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        ordering = ['email']

class UserRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['id', 'name', 'email', 'date_joined', 'last_login', 'groups', 'user_permissions']
        ordering = ['email']


class AdSerializer(serializers.ModelSerializer):
    owner = StringRelatedField(read_only=True)
    average_rating = serializers.ReadOnlyField()

    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        ordering = ['-id']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Title must be at least 5 characters long')
        if len(value) > 100:
            raise serializers.ValidationError('Title must be less than 100 characters long')
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Description must be less than 500 characters long')
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be a positive number')
        return value

    def validate_rooms(self, value):
        if value < 1:
            raise serializers.ValidationError('Number of rooms must be at least 1')
        return value

    def validate_state(self, value):
        if not re.match(r'^([a-zA-Z ]{2,50})$', value):
            raise serializers.ValidationError( "The state must be represented by alphabetic characters")
        return value

    def validate_city(self, value):
        if not re.match(r'^([a-zA-Z ]{2,50})$', value):
            raise serializers.ValidationError("The city must be represented by alphabetic characters")
        return value

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class BookingCreateSerializer(serializers.ModelSerializer):
    total_days = serializers.ReadOnlyField()
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = ['id', 'ad', 'start_date', 'end_date', 'total_cost', 'total_days']


    def validate_ad(self, ad):
        if not ad.is_active:
            raise serializers.ValidationError('This ad is not active, you cannot book it.')
        return ad

    def validate_start_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError({'start_date':'Start date cannot be in the past'})
        return value

    def validate_end_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError({'end_date': 'End date cannot be in the past'})
        return value

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        ad = data.get('ad')

        # Проверяем, что дата начала не позже даты окончания
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError({'start_date': 'Start date cannot be later than end date'})

        # Проверка на пересечение бронирований
        if ad and start_date and end_date:
            overlapping_bookings = Booking.objects.filter(
                ad=ad,
                status__in=["Confirmed", "Pending"],
                start_date__lt=end_date,  # Начало бронирования меньше даты окончания
                end_date__gt=start_date  # Конец бронирования больше даты начала
            ).exclude(id=self.instance.id if self.instance else None)

            if overlapping_bookings.exists():
                raise serializers.ValidationError({"start_date and end_date": "The dates are already taken"})

        return data


    def create(self, validated_data):
        validated_data['renter'] = self.context['request'].user
        validated_data['landlord'] = validated_data['ad'].owner
        return super().create(validated_data)


class BookingListSerializer(serializers.ModelSerializer):
    ad = AdSerializer()
    renter = StringRelatedField()
    landlord = StringRelatedField()
    total_days = serializers.ReadOnlyField()
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = '__all__'


class BookingUpdateSerializer(serializers.ModelSerializer):
    renter = StringRelatedField()
    landlord = StringRelatedField()
    total_days = serializers.ReadOnlyField()
    total_cost = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        exclude = ['created_at', 'updated_at']
        read_only_fields = ['id', 'ad', 'renter', 'landlord', 'start_date', 'end_date']

    def validate(self, data):
        user = self.context['request'].user
        new_status = data.get('status')
        booking = self.instance  # Получаем объект бронирования

        # Проверка на отмену менее чем за 2 дня до начала бронирования
        if new_status == 'Rejected':
            days_until_start = (booking.start_date - datetime.date.today()).days
            if days_until_start < 2:
                raise serializers.ValidationError({
                    'status': 'Booking cannot be canceled less than 2 days before the start date'
                })

        # Валидация прав арендатора и арендодателя
        if user.is_renter and new_status != 'Rejected':
            raise serializers.ValidationError({'status': 'Renter can only update status to Rejected'})

        if user.is_landlord and new_status == "Pending":
            raise serializers.ValidationError({'status': 'Landlord can only update status to Rejected or Confirmed'})

        return data


class BookedDatesSerializer(serializers.ModelSerializer):
    ad = StringRelatedField()
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'ad']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['ad', 'rating', 'comment']

    def validate(self, data):
        user = self.context['request'].user
        ad = data.get('ad')

        booking = Booking.objects.filter(
            ad=ad,
            renter=user,
            status="Confirmed",
            end_date__lte=datetime.date.today()).exists()

        if not booking:
            raise serializers.ValidationError({'ad': 'You can leave a review only after staying at this property.'})

        if Review.objects.filter(user=user, ad=ad).exists():
            raise serializers.ValidationError({"review": "You have already submitted a review for this listing."})

        return data

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError({'rating': 'Rating must be between 0 and 5'})

        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ReviewListSerializer(serializers.ModelSerializer):
    user = StringRelatedField()
    ad = StringRelatedField()

    class Meta:
        model = Review
        fields = ['user', 'ad', 'rating', 'comment', 'created_at']

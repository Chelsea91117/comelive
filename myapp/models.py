from datetime import timedelta

from django.contrib.auth.models import UserManager, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone

class CustomUserManager(UserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('You didn\'t enter an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20, blank=True, default='')
    is_renter = models.BooleanField(default=False)
    is_landlord = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['email']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name or self.email.split('@')[0]

    def __str__(self):
        return self.email

    
class Ad(models.Model):
    TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ad'
        verbose_name_plural = 'ads'
        ordering = ['-id']

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [ ('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Rejected', 'Rejected'), ]
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField(verbose_name='Start date', unique=True)
    end_date = models.DateField(verbose_name='End date', unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateField(auto_now=True, verbose_name="Updated at")
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='renter_bookings')
    landlord = models.ForeignKey(User, on_delete=models.CASCADE, related_name='landlord_bookings')

    @property
    def busy_dates(self):
        bookings = Booking.objects.filter(ad=self.ad).exclude(id=self.id)
        busy_dates = []
        for booking in bookings:
            for date in range(booking.start_date, booking.end_date + timedelta(days=1)):
                busy_dates.append(date)
        return busy_dates

    class Meta:
        verbose_name = 'booking'
        verbose_name_plural = 'bookings'
        ordering = ['-created_at']

    def __str__(self):
        return f'Booking {self.id} for {self.ad.title}'
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
    price = models.IntegerField()
    rooms = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


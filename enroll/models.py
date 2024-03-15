from django.contrib.auth.models import AbstractUser,Permission
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="User")
    cnic = models.CharField(max_length=15, default='', blank=True, null=True,)
    address = models.CharField(max_length=255, default='', blank=True, null=True,)
    contact = models.CharField(max_length=20, default='default_value', blank=True, null=True,)
    image = CloudinaryField('image',blank=True, null=True,)
    email = models.EmailField(_('email address'), default='example@example.com')
    is_email_verified = models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,default=False)
    new_email = models.EmailField(_('new email address'), blank=True, null=True)

   
    def is_admin(self):
        return self.role == 'Admin'


    def __str__(self):
        return self.username

    def __str__(self):
        return self.username
    
class AdminPermission(Permission):
    class Meta:
        permissions = (
            ("view_statement_history", "Can view statement history of users"),
            ("load_wallet_balance",  "Can load wallet balance of users"),
        )    

class Wallet(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Wallet of {self.user.username}"

class Transaction(models.Model):
    sender_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purpose = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id}"

class Friend(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.nickname
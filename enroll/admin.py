from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Transaction, Wallet, Friend

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email','image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Info', {'fields': ('cnic', 'address', 'contact')}),
    )
    add_fieldsets = (
    (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('sender_wallet', 'receiver_wallet', 'amount', 'purpose', 'timestamp')

class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

class FriendAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Friend)

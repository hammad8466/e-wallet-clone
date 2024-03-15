# admin_views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Wallet

def load_wallet_balance(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')  # Assuming you have a form field to specify the user ID
        amount = request.POST.get('amount')    # Assuming you have a form field to specify the amount to load
        
        try:
            user_wallet = Wallet.objects.get(user_id=user_id)
            user_wallet.balance += amount
            user_wallet.save()
            messages.success(request, 'Balance loaded successfully!')
        except Wallet.DoesNotExist:
            messages.error(request, 'User does not exist or does not have a wallet.')
        except ValueError:
            messages.error(request, 'Invalid amount provided.')
        
        return redirect('admin:load_wallet_balance')  # Redirect back to the load wallet balance page
    else:
        return render(request, 'admin/load_wallet_balance.html')

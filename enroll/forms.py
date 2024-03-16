from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,Friend
from cloudinary.forms import CloudinaryFileField

class StatementHistoryForm(forms.Form):
    contact = forms.CharField(label=' Contact Number')

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser  
        fields = ['username', 'first_name', 'last_name', 'email',]
        labels = {'email': 'Email Address'}

        image = CloudinaryFileField(
        options={"folder": "blog/", "crop": "limit", "width": 600, "height": 600,}
    )    
class EditUserProfileForm(UserChangeForm):
    password = None
    cnic = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    contact = forms.CharField(max_length=20)  
    profile_image = forms.ImageField(label='Profile Image', required=False)

    class Meta:
        model = CustomUser  
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'cnic', 'address','contact','profile_image']
        labels = {'email': 'Email Address','username':'Full Name'}

    def __init__(self, *args, **kwargs):
        super(EditUserProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

class EditAdminProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser  
        fields = '__all__'
        labels = {'email': 'Email'}


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['nickname', 'email', 'contact_number']   
       
class TransferFundsForm(forms.Form):
    contact = forms.CharField(max_length=20, label='Receiver Contact')
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Amount')
    purpose = forms.CharField(max_length=255, label='Purpose')

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount <= 0:
            raise forms.ValidationError("Amount must be greater than zero.")
        return amount
    

class ToggleBalanceForm(forms.Form):
    toggle_balance = forms.BooleanField(label='Toggle Balance', required=False)    

    
class EmailChangeForm(forms.ModelForm):
    new_email = forms.EmailField(label='New Email Address')

    class Meta:
        model = CustomUser
        fields = ['new_email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Remove 'user' from kwargs
        super(EmailChangeForm, self).__init__(*args, **kwargs)
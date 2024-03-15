from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import SignUpForm,EditUserProfileForm,TransferFundsForm,ToggleBalanceForm,FriendForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from datetime import datetime,date
from django.utils.encoding import force_bytes
# from django.utils.encoding import smart_bytes, force_text
from .forms import EmailChangeForm
from django.conf import settings
import ssl
from decimal import Decimal
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse
from .models import  Wallet, CustomUser,Transaction,Friend
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, smart_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.db import IntegrityError
from .tokens import account_activation_token
from django.http import HttpResponseBadRequest
import logging
from .forms import StatementHistoryForm
from django.core.mail import send_mail
# from django.utils.encoding import force_bytes, smart_text
logger = logging.getLogger(__name__)



# from django.contrib import messages
# from django.shortcuts import redirect
# ssl._create_default_https_context = ssl._create_unverified_context

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')

#             try:
#                 send_mail(
#                     mail_subject, message, 'from@example.com', [to_email], fail_silently=False,
#                     html_message=message,  # Specify HTML content
#                     # timeout=10,  # Set a timeout for the email sending request
#                 )
#                 messages.success(request, 'Activation email sent successfully.')
#                 messages.info(request, f'Email sent from: from@example.com to: {to_email}')
#             except Exception as e:
#                 messages.error(request, f'Failed to send activation email: {e}')
#             return redirect('signup')  # Redirect to the sign-up page after processing the form
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')

#             try:
#                 # Set up SSL certificate verification
#                 ssl._create_default_https_context = ssl._create_unverified_context

#                 # Send email
#                 send_mail(
#                     mail_subject, message, 'from@example.com', [to_email], fail_silently=False,
#                     html_message=message,  # Specify HTML content
#                 )
#                 messages.success(request, 'Activation email sent successfully.')
#                 messages.info(request, f'Email sent from: from@example.com to: {to_email}')
#             except Exception as e:
#                 messages.error(request, f'Failed to send activation email: {e}')
#             return redirect('signup')  # Redirect to the sign-up page after processing the form
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})


# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')

#             try:
#                 send_mail(
#                     mail_subject, message, 'from@example.com', [to_email], fail_silently=False,
#                     html_message=message,  # Specify HTML content
#                 )
#                 messages.success(request, 'Activation email sent successfully.')
#                 messages.info(request, f'Email sent from: from@example.com to: {to_email}')
#             except Exception as e:
#                 messages.error(request, f'Failed to send activation email: {e}')
#             return redirect('signup')  # Redirect to the sign-up page after processing the form
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')

#             try:
#                 send_mail(
#                     mail_subject, message, 'from@example.com', [to_email], fail_silently=False,
#                     html_message=message,  # Specify HTML content
#                     timeout=10,  # Set a timeout for the email sending request
#                 )
#                 messages.success(request, 'Activation email sent successfully.')
#                 messages.info(request, f'Email sent from: from@example.com to: {to_email}')
#             except Exception as e:
#                 messages.error(request, f'Failed to send activation email: {e}')
#             return redirect('signup')  # Redirect to the sign-up page after processing the form
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})


# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()

#             current_site = get_current_site(request)
#             mail_subject = 'Activate your account.'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': account_activation_token.make_token(user),
#             })
#             to_email = form.cleaned_data.get('email')

#             # Disable SSL certificate verification for email sending
#             try:
#                 send_mail(
#                     mail_subject, message, 'from@example.com', [to_email], fail_silently=False,
#                     html_message=message,  # Specify HTML content
#                     timeout=10,  # Set a timeout for the email sending request
#                 )
#                 return render(request, 'enroll/signupconfirm.html')
#             except Exception as e:
#                 # Handle any errors that occur during email sending
#                 return render(request, 'enroll/signup.html', {'form': form, 'error_message': str(e)})
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})

# def sign_up(request):
#     if request.method == "POST":
#         fm=SignUpForm(request.POST)
#         if fm.is_valid():
#             messages.success(request,'Account Created Successfully !!')
#             fm.save()
#     else:
#      fm=SignUpForm()        
#     return render(request,'enroll/signup.html',{'form':fm})
# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             # Retrieve form data
#             username = fm.cleaned_data.get('username')
#             email = fm.cleaned_data.get('email')
#             pass1 = fm.cleaned_data.get('password1')

#             # Create user object
#             myuser = CustomUser.objects.create_user(username, email, pass1)
#             myuser.is_active = False  # Disable account until email confirmation
#             myuser.save()

#             # Send welcome email
#             subject = "Welcome to Our Django User Registration System"
#             message = f"Hello {myuser.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
#             from_email = settings.EMAIL_HOST_USER
#             to_list = [myuser.email]
#             send_mail(subject, message, from_email, to_list, fail_silently=True)

#             # Send email confirmation link
#             current_site = get_current_site(request)
#             email_subject = "Confirm Your Email Address"
#             message2 = render_to_string('email_confirmation.html', {
#                 'name': myuser.first_name,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#                 'token': default_token_generator.make_token(myuser)
#             })
#             email = EmailMessage(
#                 email_subject,
#                 message2,
#                 settings.EMAIL_HOST_USER,
#                 [myuser.email],
#             )
#             email.send(fail_silently=True)

#             messages.success(request, "Your account has been created successfully! Please check your email to confirm your email address and activate your account.")
#             return redirect('signin')

#     else:
#         fm = SignUpForm()
        
#     return render(request, 'enroll/signup.html', {'form': fm})

# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             # Save form data
#             fm.save()

#             # Retrieve form data
#             username = fm.cleaned_data.get('username')
#             email = fm.cleaned_data.get('email')
            
#             # Create user object
#             user = CustomUser.objects.create(
#                 username=username,
#                 email=email,
#                 is_active=False  # Set user as inactive until email confirmation
#             )
            
#             # Generate email confirmation link
#             current_site = get_current_site(request)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             token = default_token_generator.make_token(user)
#             confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"

#             # Compose email message
#             subject = "Confirm Your Email Address"
#             message = render_to_string('email_confirmation.html', {
#                 'user': user,
#                 'confirmation_link': confirmation_link,
#             })
            
#             # Send email
#             send_mail(
#                 subject,
#                 message,
#                 'from@example.com',  # Replace with your email address
#                 [email],
#                 fail_silently=True,
#             )

#             # Display success message
#             messages.success(request, 'Account created successfully! Please check your email to confirm your email address.')
#             return redirect('home')  # Redirect to home page after successful registration
#     else:
#         fm = SignUpForm()
        
#     return render(request, 'enroll/signup.html', {'form': fm})

# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             username = fm.cleaned_data.get('username')
#             email = fm.cleaned_data.get('email')
#             password = fm.cleaned_data.get('password1')

#             try:
#                 user = CustomUser.objects.create_user(username, email, password)
#                 user.is_active = False  # Set user as inactive until email confirmation
#                 user.save()

#                 # Send email confirmation
#                 current_site = get_current_site(request)
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = default_token_generator.make_token(user)
#                 confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"
#                 # Send confirmation email
#                 # Code to send confirmation email...
                
#                 messages.success(request, 'Account created successfully! Please check your email to confirm your email address.')
#                 return redirect('login')
#             except IntegrityError:
#                 messages.error(request, 'Username already exists. Please choose a different username.')
#                 return redirect('signup')  # Redirect back to the signup page with an error message

#     else:
#         fm = SignUpForm()

#     return render(request, 'enroll/signup.html', {'form': fm})

# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# @@@@@@
# *******
# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             username = fm.cleaned_data.get('username')
#             email = fm.cleaned_data.get('email')
#             password = fm.cleaned_data.get('password1')

#             try:
#                 user = CustomUser.objects.create_user(username, email, password)
#                 user.is_active = False  # Set user as inactive until email confirmation
#                 user.save()

#                 # Send email confirmation
#                 # breakpoint()
#                 current_site = get_current_site(request)
#                 uid = urlsafe_base64_encode(force_bytes(user.pk))
#                 token = default_token_generator.make_token(user)
#                 confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"

#                 # Send confirmation email
#                 subject = 'Confirm your email address'
#                 message = render_to_string('enroll/confirmation_email.html', {
#                     'user': user,
#                     'confirmation_link': confirmation_link,
#                 })
#                 # breakpoint()
#                 send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

#                 messages.success(request, 'Account created successfully! Please check your email to confirm your email address.')
#                 return redirect('login')
#             except IntegrityError:
#                 messages.error(request, 'Username already exists. Please choose a different username.')
#                 return redirect('signup')  # Redirect back to the signup page with an error message

#     else:
#         fm = SignUpForm()

#     return render(request, 'enroll/signup.html', {'form': fm})

# def confirm_view(request, uidb64, token):
#     try:
#         uid = force_bytes(urlsafe_base64_decode(uidb64))
#         user = CustomUser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'Your email address has been confirmed. You can now login.')
#         return redirect('login')
#     else:
#         messages.error(request, 'Invalid confirmation link. Please contact support for assistance.')
#         return redirect('login')
# ********* 
# def confirm_view(request, param1, param2):
#     # Example logic to handle confirmation
#     # For demonstration purposes, we'll just render a template with confirmation details
#     confirmation_data = {
#         'param1': param1,
#         'param2': param2,
#         'confirmation_message': 'Your confirmation has been successful.'
#     }
#     return render(request, 'enroll/confirmation_template.html', confirmation_data)

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data.get('username')
            email = fm.cleaned_data.get('email')
            password = fm.cleaned_data.get('password1')

            try:
                user = CustomUser.objects.create_user(username, email, password)
                user.is_active = False  # Set user as inactive until email confirmation
                user.save()

                # Send email confirmation
                current_site = get_current_site(request)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"

                # Send confirmation email
                subject = 'Confirm your email address'
                message = render_to_string('enroll/confirmation_email.html', {
                    'user': user,
                    'confirmation_link': confirmation_link,
                })
                send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

                # Display success message and redirect to login page
                messages.success(request, 'Account created successfully! Please check your email to confirm your email address.')
                return redirect('login')
            except IntegrityError:
                # Display error message and redirect back to sign up page
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect('signup')

    else:
        fm = SignUpForm()

    return render(request, 'enroll/signup.html', {'form': fm})

def confirm_view(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Display success message and redirect to login page
        messages.success(request, 'Your email address has been confirmed. You can now login.')
        return redirect('login')
    else:
        # Display error message and redirect to login page
        messages.error(request, 'Invalid confirmation link. Please contact support for assistance.')
        return redirect('login')

# @@@@@@@



# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             username = fm.cleaned_data.get('username')
#             email = fm.cleaned_data.get('email')
#             password = fm.cleaned_data.get('password1')

#             try:
#                 user = CustomUser.objects.create_user(username, email, password)
#                 user.is_active = False  # Set user as inactive until email confirmation
#                 user.save()

#                 # Send email confirmation
#                 current_site = get_current_site(request)
#                 uid = urlsafe_base64_encode(smart_bytes(user.pk))
                
#                 token = default_token_generator.make_token(user)
#                 confirmation_link = f"http://{current_site.domain}/confirm/{uid}/{token}/"

#                 # Send confirmation email
#                 subject = 'Confirm your email address'
#                 message = render_to_string('enroll/confirmation_email.html', {
#                     'user': user,
#                     'confirmation_link': confirmation_link,
#                 })
#                 send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

#                 messages.success(request, 'Account created successfully! Please check your email to confirm your email address.')
#                 return redirect('login')
#             except IntegrityError:
#                 messages.error(request, 'Username or email already exists. Please choose a different one.')
#                 return redirect('signup')

#     else:
#         fm = SignUpForm()

#     return render(request, 'enroll/signup.html', {'form': fm})

# def confirm_view(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = CustomUser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(request, 'Your email address has been confirmed. You can now login.')
#         return redirect('login')
#     else:
#         messages.error(request, 'Invalid confirmation link. Please contact support for assistance.')
#         return redirect('login')  # Redirect to login page with an error message




# def sign_up(request):
#     if request.method == "POST":
#         fm=SignUpForm(request.POST)
#         if fm.is_valid():
#             messages.success(request,'Account Created Successfully !!')
#             fm.save()
#     else:
#      fm=SignUpForm()        
#     return render(request,'enroll/signup.html',{'form':fm})

# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#              messages.success(request,'Account Created Successfully !!')
#              fm.save()
    

            
#             # # Send welcome email
#             # subject = "Welcome to Our Django User Registration System"
#             # message = f"Hello {myuser.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
#             # from_email = settings.EMAIL_HOST_USER
#             # to_list = [myuser.email]
#             # send_mail(subject, message, from_email, to_list, fail_silently=True)

#             # Send email confirmation link
#             current_site = get_current_site(request)
#             email_subject = "Confirm Your Email Address"
#             message2 = render_to_string('email_confirmation.html', {
#                 'name': myuser.first_name,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#                 'token': default_token_generator.make_token(myuser)
#             })
#             email = EmailMessage(
#                 email_subject,
#                 message2,
#                 settings.EMAIL_HOST_USER,
#                 [myuser.email],
#             )
#             email.send(fail_silently=True)

#             messages.success(request, "Your account has been created successfully! Please check your email to confirm your email address and activate your account.")
#             return redirect('signin')

#     else:
#         fm = SignUpForm()
        
#     return render(request, 'enroll/signup.html', {'form': fm})

# def sign_up(request):
#     if request.method == "POST":
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             # Retrieve form data
#             username = fm.cleaned_data.get('username')
#             fname = fm.cleaned_data.get('fname')
#             lname = fm.cleaned_data.get('lname')
#             email = fm.cleaned_data.get('email')
#             pass1 = fm.cleaned_data.get('password1')
#             pass2 = fm.cleaned_data.get('password2')

#             # Validate username
#             if CustomUser.objects.filter(username=username).exists():
#                 messages.error(request, "Username already exists! Please try a different username.")
#                 return redirect('home')
            
#             # Validate email
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.error(request, "Email already registered!")
#                 return redirect('home')
            
#             # Validate password match
#             if pass1 != pass2:
#                 messages.error(request, "Passwords do not match!")
#                 return redirect('home')
            
#             # Create user object
#             myuser = CustomUser.objects.create_user(username, email, pass1)
#             myuser.first_name = fname
#             myuser.last_name = lname
#             myuser.is_active = False  # Disable account until email confirmation
#             myuser.save()

#             # Send welcome email
#             subject = "Welcome to Our Django User Registration System"
#             message = f"Hello {myuser.first_name}!\n\nThank you for registering on our website. Please confirm your email address to activate your account.\n\nRegards,\nThe Django Team"
#             from_email = settings.EMAIL_HOST_USER
#             to_list = [myuser.email]
#             send_mail(subject, message, from_email, to_list, fail_silently=True)

#             # Send email confirmation link
#             current_site = get_current_site(request)
#             email_subject = "Confirm Your Email Address"
#             message2 = render_to_string('email_confirmation.html', {
#                 'name': myuser.first_name,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
#                 'token': default_token_generator.make_token(myuser)
#             })
#             email = EmailMessage(
#                 email_subject,
#                 message2,
#                 settings.EMAIL_HOST_USER,
#                 [myuser.email],
#             )
#             email.send(fail_silently=True)

#             messages.success(request, "Your account has been created successfully! Please check your email to confirm your email address and activate your account.")
#             return redirect('signin')

#     else:
#         fm = SignUpForm()
        
#     return render(request, 'enroll/signup.html', {'form': fm})

# def sign_up(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False  # Deactivate the user until email confirmation
#             user.save()
            
#             # Send email confirmation
#             current_site = get_current_site(request)
#             subject = 'Activate your account'
#             message = render_to_string('enroll/account_activation_email.html', {
#                 'user': user,
#                 'domain': current_site.domain,
#                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                 'token': default_token_generator.make_token(user),
#             })
#             user.email_user(subject, message)
            
#             return redirect('account_activation_sent')
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})



@login_required
def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account_activation_complete')
    else:
        return HttpResponseBadRequest('Activation link is invalid!')

@login_required
def account_activation_complete(request):
    return render(request, 'account_activation_complete.html') 
# def sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.is_active = False
#             user.save()
#             send_confirmation_email(request, user)
#             messages.success(request, 'Account created successfully. Please check your email to confirm your email address.')
#             return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})

# def sign_up(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             if CustomUser.objects.filter(email=email).exists():
#                 messages.error(request, 'This email address is already registered.')
#             else:
#                 user = form.save(commit=False)
#                 user.is_active = False
#                 user.save()
#                 send_confirmation_email(request, user)
#                 messages.success(request, 'Account created successfully. Please check your email to confirm your email address.')
#                 return redirect('login')
#     else:
#         form = SignUpForm()
#     return render(request, 'enroll/signup.html', {'form': form})

# def send_confirmation_email(request, user):
#     token = default_token_generator.make_token(user)
#     current_site = get_current_site(request)
#     subject = 'Confirm your email address'
#     message = render_to_string('enroll/confirmation_email.html', {
#         'user': user,
#         'domain': current_site.domain,
#         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#         'token': token,
#     })
#     send_mail(subject, message, 'from@example.com', [user.email])



# def send_confirmation_email(request, user):
#     try:
#         token = default_token_generator.make_token(user)
#         current_site = get_current_site(request)
#         subject = 'Confirm your email address'
#         message = render_to_string('enroll/confirmation_email.html', {
#             'user': user,
#             'domain': current_site.domain,
#             'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#             'token': token,
#         })
#         send_mail(subject, message, 'from@example.com', [user.email])
#     except Exception as e:
#         logger.exception("Error occurred while sending confirmation email: %s", str(e))


# def confirm_email(request, uidb64, token):
#     try:
#         uid = smart_bytes(urlsafe_base64_decode(uidb64))
#         user = CustomUser.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_email_verified = True
#         user.save()
#         messages.success(request, 'Your email address has been confirmed. You can now log in.')
#         return redirect('login')
#     else:
#         return HttpResponse('Invalid confirmation link.')
    

# @login_required
def admin_dashboard(request):
    # Your admin dashboard view logic here
    username="Hammad"
    return render(request, 'enroll/admin_dashboard.html',{'username':username})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # breakpoint()
                if user.is_staff == True:
                #  return HttpResponseRedirect(reverse('admin_dashboard'))
                #  return HttpResponseRedirect(reverse('admin_dashboard'))
                 return render(request, 'enroll/admin_dashboard.html')
                else:
                #  return redirect('profile')
                 return HttpResponseRedirect(reverse('profile'))
            else:
                # Increase the login attempts count
                login_attempts = request.session.get('login_attempts', 0)
                request.session['login_attempts'] = login_attempts + 1
                
                # Check if login attempts threshold is reached
                if login_attempts >= 2:  # Adjusted to start from 0
                    login_disabled_until = timezone.now() + timezone.timedelta(minutes=5)
                    request.session['login_disabled_until'] = login_disabled_until.strftime('%Y-%m-%d %H:%M:%S')
                    return HttpResponse("Login is disabled for 5 minutes.")
                else:
                    # Return an error indicating invalid credentials
                    form.add_error(None, "Invalid username or password.")
                    # Re-render the login form with errors
                    return render(request, 'enroll/userlogin.html', {'form': form})
        else:
            # Form is invalid, likely due to incorrect credentials
            # Increase the login attempts count
            login_attempts = request.session.get('login_attempts', 0)
            request.session['login_attempts'] = login_attempts + 1

            # Check if login attempts threshold is reached
            if login_attempts >= 2:  # Adjusted to start from 0
                login_disabled_until = timezone.now() + timezone.timedelta(minutes=5)
                request.session['login_disabled_until'] = login_disabled_until.strftime('%Y-%m-%d %H:%M:%S')
                return HttpResponse("Login is disabled for 5 minutes.")
            else:
                # Re-render the login form with errors
                return render(request, 'enroll/userlogin.html', {'form': form})
    else:
        form = AuthenticationForm()
    
    # Handle login disabled state
    login_disabled_until = request.session.get('login_disabled_until')
    if login_disabled_until:
        login_disabled_until = timezone.make_aware(datetime.strptime(login_disabled_until, '%Y-%m-%d %H:%M:%S'))
        time_remaining = login_disabled_until - timezone.now()
        if time_remaining.total_seconds() > 0:
            remaining_minutes = int(time_remaining.total_seconds() // 60)
            return HttpResponse(f"Login is disabled for {remaining_minutes} minutes.")
        else:
            # If login is re-enabled, clear session data and redirect to login page
            del request.session['login_disabled_until']
            del request.session['login_attempts']
            return HttpResponseRedirect(reverse('login'))  # Redirect to the login page
    
    context = {'form': form}
    return render(request, 'enroll/userlogin.html', context)


def user_profile(request):  
    if request.user.is_authenticated:
      if request.method == "POST":
        fm=EditUserProfileForm(request.POST,instance=request.user)
        if fm.is_valid():
          messages.success(request,"Profile Updated Successfully !!")
          fm.save()
      else:
         fm=EditUserProfileForm(instance=request.user)   
      return render(request,'enroll/profile.html',{'name':request.user,'form':fm})
    else:
       return HttpResponseRedirect('/login/')
       
def user_logout(request):     
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required
def user_change_pass(request):  
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Password changed successfully.")
            return redirect('profile')  # Assuming 'profile' is the name of the URL for the user's profile page
        else:
            messages.error(request, "An error occurred while changing the password. Please try again.")
    else:    
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'enroll/changepass.html', {'form': fm})     

def user_change_email(request):
    if request.method == "POST":
        form = EmailChangeForm(request.POST, user=request.user)
        if form.is_valid():
            new_email = form.cleaned_data.get('new_email')
            # Set the new email in the user model for temporary storage
            request.user.new_email = new_email
            request.user.save()
            # Send email confirmation
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(request.user.pk))
            token = default_token_generator.make_token(request.user)
            confirmation_link = f"http://{current_site.domain}/confirm_email_change/{uid}/{token}/"
            subject = 'Confirm your new email address'
            message = render_to_string('enroll/confirmation_email_change.html', {
                'user': request.user,
                'confirmation_link': confirmation_link,
            })
            send_mail(subject, message, settings.EMAIL_HOST_USER, [new_email])
            messages.success(request, 'Confirmation email sent to your new email address.')
            return redirect('profile')  # Redirect to user's profile page
    else:
        form = EmailChangeForm()
    return render(request, 'enroll/change_email.html', {'form': form})

def confirm_email_change(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        new_email = user.new_email
        if new_email:
            user.email = new_email  # Update the user's email address
            user.new_email = ''  # Clear the temporary new email field
            user.save()
            messages.success(request, 'Your email address has been successfully updated.')
        else:
            messages.error(request, 'No new email address found to update.')
    else:
        messages.error(request, 'Invalid confirmation link.')

    return redirect('profile')  # Redirect to user's profile page
def home(request):
    user_name = request.user.get_full_name() if request.user.is_authenticated else None
    current_balance = 0.0
    show_balance = False

    if request.method == 'POST':
        toggle_form = ToggleBalanceForm(request.POST)
        if toggle_form.is_valid():
            show_balance = toggle_form.cleaned_data.get('toggle_balance', False)
    else:
        toggle_form = ToggleBalanceForm()

    if show_balance:
        # Retrieve the current wallet balance of the logged-in user
        try:
            current_balance = request.user.wallet.balance
        except Wallet.DoesNotExist:
            pass  # Handle the case where the user does not have a wallet

    return render(request, 'enroll/home.html', {'current_balance': current_balance, 'user_name': user_name, 'toggle_form': toggle_form, 'show_balance': show_balance})

def transfer_funds(request):
    if request.method == 'POST':
        form = TransferFundsForm(request.POST)
        if form.is_valid():
            sender = request.user
            recipient_contact = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']
            purpose = form.cleaned_data['purpose']

            try:
                recipient = CustomUser.objects.get(contact=recipient_contact)
                sender_wallet = sender.wallet
                recipient_wallet = recipient.wallet

                # Calculate the total amount transferred by the sender today
                today_transactions = Transaction.objects.filter(sender_wallet=sender_wallet, timestamp__date=date.today())
                total_amount_today = today_transactions.aggregate(total=Sum('amount'))['total'] or 0

                # Check if the total amount exceeds the daily limit
                if total_amount_today + amount > 25000:
                    # Apply extra charge
                    amount += 200
                
                if sender_wallet.balance >= amount:
                    # Perform the transfer
                    sender_wallet.balance -= amount
                    sender_wallet.save()
                    recipient_wallet.balance += amount
                    recipient_wallet.save()
                    
                    # Create transaction record
                    Transaction.objects.create(sender_wallet=sender_wallet, receiver_wallet=recipient_wallet, amount=amount, purpose=purpose)

                    return JsonResponse({'message': 'Transfer successful.'})
                else:
                    return JsonResponse({'message': 'Insufficient balance.'})
            except CustomUser.DoesNotExist:
                return JsonResponse({'message': 'Recipient user does not exist.'})
        else:
            return JsonResponse({'message': 'Invalid form data.'}, status=400)  # Bad request for invalid form data
    else:
        form = TransferFundsForm()

    return render(request, 'enroll/transfer_funds.html', {'form': form})



def account_statement(request):
    # Retrieve incoming and outgoing transactions for the logged-in user
    user = request.user
    incoming_transactions = Transaction.objects.filter(receiver_wallet__user=user)
    outgoing_transactions = Transaction.objects.filter(sender_wallet__user=user)

    # Pass transaction data to the template
    context = {
        'incoming_transactions': incoming_transactions,
        'outgoing_transactions': outgoing_transactions
    }

    # Render the account statement template with transaction data
    return render(request, 'enroll/account_statement.html', context)


def add_friend(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            friend = form.save(commit=False)
            friend.user = request.user
            friend.save()
            return redirect('friends_list')  # Redirect to the friends list page after adding a friend
    else:
        form = FriendForm()
    return render(request, 'enroll/add_friend.html', {'form': form})

def friends_list(request):
    friends = Friend.objects.filter(user=request.user)
    return render(request, 'enroll/friends_list.html', {'friends': friends})

from decimal import Decimal

# @login_required
def admin_load_balance(request):
    if request.method == 'POST':
        email_or_contact = request.POST.get('email_or_contact')
        amount = request.POST.get('amount')

        try:
            user = CustomUser.objects.get(email=email_or_contact)  # Try to find user by email
        except CustomUser.DoesNotExist:
            try:
                user = CustomUser.objects.get(contact=email_or_contact)  # Try to find user by contact number
            except CustomUser.DoesNotExist:
                error_message = "User not found."
                return render(request, 'enroll/admin_load_balance.html', {'error_message': error_message})

        try:
            wallet = user.wallet
        except Wallet.DoesNotExist:
            error_message = f"No wallet found for user: {user.get_full_name()}. Please create a wallet for the user."
            return render(request, 'enroll/admin_load_balance.html', {'error_message': error_message})

        try:
            amount = Decimal(amount)  # Convert amount to Decimal
            if amount <= Decimal('0'):
                raise ValueError("Invalid amount")
        except ValueError:
            error_message = "Invalid amount. Please enter a valid positive number."
            return render(request, 'enroll/admin_load_balance.html', {'error_message': error_message})

        wallet.balance += amount  # Perform addition operation
        wallet.save()
        messages.success(request, f"Successfully loaded {amount} into {user.get_full_name()}'s wallet.")
        return redirect('admin_load_balance')
    else:
        return render(request, 'enroll/admin_load_balance.html')

def admin_statement_history(request):
    if request.method == 'POST':
        form = StatementHistoryForm(request.POST)
        if form.is_valid():
            # breakpoint()
            email_or_contact = form.cleaned_data['contact']

            try:
                    user = CustomUser.objects.get(contact=email_or_contact)  # Try to find user by contact number
            except CustomUser.DoesNotExist:
                    user = None  # If user not found, set to None

            if user:
                # Retrieve incoming and outgoing transactions for the user
                incoming_transactions = Transaction.objects.filter(receiver_wallet__user=user)
                outgoing_transactions = Transaction.objects.filter(sender_wallet__user=user)
                return render(request, 'enroll/admin_account_statement.html', {
                    'user': user,
                    'incoming_transactions': incoming_transactions,
                    'outgoing_transactions': outgoing_transactions
                })
            else:
                error_message = "User not found. Please enter a valid email address or contact number."
                return render(request, 'enroll/admin_statement_history_form.html', {'form': form, 'error_message': error_message})
    else:
        form = StatementHistoryForm()
    return render(request, 'enroll/admin_statement_history_form.html', {'form': form})
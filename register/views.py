from django.shortcuts import render,redirect
from django.contrib import admin
from django import forms
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth
#register
global code ,passw , uid ,mailid , email, username,user
code=''
user=''
email=''
import smtplib
import ssl
from email.message import EmailMessage
from .forms import RegisterForm       
def register(request):
    global code,user,email,username
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken!')
                return HttpResponse('Username already taken!')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already exists!')
                return HttpResponse('Email already exists!')
            else:
                email_sender = 'noreplycursorhigh@gmail.com'
                email_password = 'olclmvbmxkycihax'
                email_receiver = email
                import random
                import string
                
                def generate_code():
                    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
                    return code
                code=generate_code()
                def gen():
                    email,user=email_receiver,username
                    return email,user
                email,username=gen()
                # Set the subject and body of the email
                subject = 'Verification code for Cursor High !'
                body = f"""
                Hey there !
                here is the verification code for email
                {email_receiver}
                and user name => {username}
                verification code
                => {code} <= 
                this mail is auto-genterated for support
                please fill the google form,link down below.
                https://forms.gle/NxwsoenNu7WEpjNm9
                Thanks for joining us! :)

                """
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)

                # Add SSL (layer of security)
                context = ssl.create_default_context()
                # Log in and send the email
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                    smtp.login(email_sender, email_password)
                    smtp.sendmail(email_sender, email_receiver, em.as_string())
                return HttpResponse('OTP sent successfully!')
        else:
            return render(request, 'sign-up.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'sign-up.html', {'form': form})

def otpchk(request):
    enotp='idk ant thing'
    enotp=request.POST.get('otp')
    if code!='':
        if enotp==code:
            passw=request.POST.get('password')
            user=User.objects.create_user(username=username,email=email,password=passw)
            user.save()
            messages.success(request,'Signed UP successfully!')
            return redirect('/login/')
        else:
            messages.error(request,'OTP verification Failed !')
            return redirect('/register/')

    else:
        messages.warning(request,'Please provide above information.')
        return redirect('/register/')

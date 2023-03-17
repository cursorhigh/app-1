from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User , auth 
from django.contrib import messages 
from .forms import LoginForm
global code ,passw , uid ,mailid , email, username,user
code=''
user=''
email=''
import smtplib
import ssl
from email.message import EmailMessage
#login
from leaderboard.models import Person

def login(request):
    global code,user,email,username,password
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(username=username)
            except:
                form.add_error('username', 'incorect username !')
                return HttpResponse('incorrect username')
            if user.check_password(password):
                email_sender = 'noreplycursorhigh@gmail.com'
                email_password = 'olclmvbmxkycihax'
                email_receiver = user.email
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
                print('incorrect password')
                return HttpResponse('incorrect Password')
        else:
            return render(request, 'log-in.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'log-in.html', {'form': form})

def otpver(request):
    enotp='idk ant thing'
    enotp=request.POST.get('otp')
    if code!='':
        if enotp==code:
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # create leaderboard user
                leaderboard_user, created = Person.objects.get_or_create(name=str(user))
                if created:
                    leaderboard_user.save()
            #messages.success(request,'Signed UP successfully!')
            return redirect('http://127.0.0.1:8000/')
        else:
           messages.error(request,'OTP verification Failed !')
           print('lok')
           return redirect('/login/')

    else:
       messages.warning(request,'Please provide above information.')
       print('kol')
       return redirect('/login/')
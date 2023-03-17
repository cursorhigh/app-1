from django.shortcuts import render , redirect ,reverse
from gamepage.models import Room , Message ,ConnectedUser
from django.http import HttpResponse , HttpResponseRedirect ,JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
def gpage(request):
    return render(request,'gpage.html',{})
@login_required(login_url='http://127.0.0.1:8000/')
def roomon(request):
    user=request.user.username
    if  Room.objects.filter(name=user).exists():
        print('ROOM ALREADY EXIST')
        messages.info(request, 'CHAT ALREADY ENABLED !') 
        return render(request,'gpage.html')
    else:
        newroom = Room.objects.create(name=user)
        newroom.save()
        messages.info(request, 'CHAT ENABLED !')    
        return render(request,'gpage.html')
@login_required(login_url='http://127.0.0.1:8000/')
def roomoff(request):
    user=request.user.username
    if  Room.objects.filter(name=user).exists():
        room = Room.objects.get(name=user)
        usern = Room.objects.get(name=user)
        Message.objects.filter(room=room).delete()
        Message.objects.filter(room=usern).delete()
        room.delete()
        messages.info(request, 'CHAT DISABLED !') 
        return render(request,'gpage.html')
    else:
        #'ALREADY OFF'
        messages.info(request, 'CHAT ALREADY DISABLED !')          
        return render(request,'gpage.html')
@login_required(login_url='http://127.0.0.1:8000/')
def join(request):
    try:
        room = request.POST['room_name']
        user=request.user.username
        try:
            roomn = Room.objects.get(name=room)
            other = ConnectedUser.objects.filter(room=roomn)
        except:
            print('off1')
            other =[]
        try:
            usern = Room.objects.get(name=user)
            me = ConnectedUser.objects.filter(room=usern)
        except:
            print('off2')
            me=[]
    except:
        pass
    #roomn = Room.objects.get(name=room)
    #usern = Room.objects.get(name=user)
    if  Room.objects.filter(name=room).exists():
        if len(me)==0 and len(other)==0:
            print('me')
            room_details = Room.objects.get(name=user)
            usern = Room.objects.get(name=user)
            ent=ConnectedUser.objects.create(user=user, room=usern)
            ent.save()
            if user == room:
               messages.info(request, 'LOL CHATING WITH URSELF ?       ')  
            return render(request,'gpage.html',{'room':room,'room_proper':user,'username':user,'room_details':room_details})
        elif len(me)==0:
            print('other')
            room_details = Room.objects.get(name=room)
            if user == room:
               messages.info(request, 'LOL CHATING WITH URSELF ?       ') 
            return render(request,'gpage.html',{'room':room,'room_proper':room,'username':user,'room_details':room_details})
        elif len(other)==0:
            print('me')
            room_details = Room.objects.get(name=user)
            if user == room:
               messages.info(request, 'LOL CHATING WITH URSELF ?       ') 
            return render(request,'gpage.html',{'room':room,'room_proper':user,'username':user,'room_details':room_details})
        else:
            # MSG ROOM NOT EXIST
            messages.info(request, 'PLAYER NOT EXIST OR NOT ENABLED THE CHAT')
            return render(request,'gpage.html')
    else:
        # MSG ROOM NOT EXIST
        messages.info(request, 'PLAYER NOT EXIST OR NOT ENABLED THE CHAT')
        return render(request,'gpage.html')

@login_required(login_url='http://127.0.0.1:8000/')
def room(request,username):
    user=request.user.username
    room_details = Room.objects.get(name=user)
    print('user')
    return render(request, 'gpage.html', {
        'username': user,
        'room': username,
        'room_details': room_details
    })


@login_required(login_url='http://127.0.0.1:8000/')
def send(request):
    print(request.POST)
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
@login_required(login_url='http://127.0.0.1:8000/')
def getMessages(request, room):
    
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)

    return JsonResponse({"messages":list(messages.values())})
def home(request):
    return render(request,'home.html')
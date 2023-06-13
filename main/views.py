from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
 
# Create your views here.
def index(request):   
    return render(request,"index.html")

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def Seller_books(request):
    return render(request,'seller_in.html')

def contact(request):
    return render(request,'contact.html')

def contact_mail_send(request):
    if request.method =='POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        sender_msg = request.POST.get('sender_msg')

        send_mail(
        'Contact message by {}'.format(sender_name),
        'message is : {}  with \n email : {}' .format(sender_msg , sender_email),
            'tejbad03@gmail.com',
            ['tejbad03@gmail.com'],
            fail_silently=False,
        )
        # messages.add_message(request , 2 ,"Message Sent")
        messages.success(request , "message sent")
        # error(request,'Username taken')
        return render(request,'contact.html' )
    else:
        return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
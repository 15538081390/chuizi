import hashlib

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from django_chuizi.settings import MAXAGE
from operate.models import User


def login(request):
    if request.method == 'POST':
        phone = request.POST.get('mobile')
        password = request.POST.get('passwd')
        password_hash = hashlib.sha1(password.encode('utf8')).hexdigest()
        if User.objects.filter(phone = phone, password = password_hash):
            usr = User.objects.filter(phone = phone, password = password_hash)
            username = usr.username
            response = redirect(reverse('app:index'))
            response.session['username'] = username
            request.session.set_expiry(MAXAGE)
            return response
    return render(request, 'operate/login.html')


def register(request):
    if request.method == 'POST':
        phone = request.POST.get('mobile')
        password = request.POST.get('passwd')
        password_hash = hashlib.sha1(password.encode('utf8')).hexdigest()
        user = User(username = phone, phone = phone, password=password_hash)
        user.save()
        response = redirect(reverse('app:index'))
        response.session['username'] = phone
        request.session.set_expiry(MAXAGE)
        return response

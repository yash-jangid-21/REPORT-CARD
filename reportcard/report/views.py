# Owned by Yash Jangid 
# github_id = yash-jangid-21
# linkeldn_id = yash-21-yash

from django.shortcuts import render,redirect
from report.models import *
from django.contrib.auth.models import User 
from django.db.models import Sum , Count ,Avg
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

def register(request):
    if request.method == "POST":
        data = request.POST
        if User.objects.filter(username = data.get('user_name')).exists():
            messages.warning(request, "Username already exist")
            return redirect('/register/')

        if  (data.get('password') != data.get('confirm_password')):
            messages.warning(request, "Password and confirm Password does not match")
            return redirect('/register/')

        reg = User.objects.create(
                username = data.get('user_name')
            )    
        reg.set_password(data.get('password'))
        reg.save()
        return redirect('/login/')
    return render(request,'register.html')    

def login_page(request):
    if request.method == "POST":
        data = request.POST
        if not User.objects.filter(username = data.get('user_name')).exists():
            messages.warning(request, "Username is does not exist")
            return redirect('/login/')
        user = authenticate(username = data.get('user_name'), password = data.get('password'))
        if user is None:
            messages.warning(request, "Password does not match")
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')        

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url='/login/')
def home(request):
    datas = card.objects.all()
    paginator = Paginator(datas, 7)
    if request.GET.get('search'):
        data = datas.filter(Student_Name__icontains = request.GET.get('search')) 
        paginator = Paginator(data, 7)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',context={'datas' : page_obj})

@login_required(login_url='/login/')
def report(request,id):
    data_1 = card.objects.filter(id = id)[0]
    data_2 = score.objects.filter(Student = data_1)
    if data_2.filter(Score__lt = 33).exists():
        x = True
        return render(request,'report.html',context={'data_1':data_1,'data_2':data_2,'x':x})
    x = data_2.aggregate(Sum('Score'),Count('id'),Avg('Score'))
    x['id__count'] *= 100
    ranks = score.objects.values('Student').annotate(Avg('Score')).order_by('-Score__avg')
    rank = 0
    for i in ranks:
        rank += 1
        if i['Student'] == int(id):
            print(i['Student'])
            break
    return render(request,'report.html',context={'data_1':data_1,'data_2':data_2,'x':x,'rank':rank})
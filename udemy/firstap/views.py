from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from firstap.models import contactus,UserProfileInfo
from firstap import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    contact_show = contactus.objects.order_by('first_name')
    my_dict={'insert':contact_show}
    return render(request, 'firstap/index.html',context=my_dict)
def forms_view(request):
    form = forms.Form()
    if request.method=='POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            print('form is valid')
            print(f'Name :'+form.cleaned_data['name'])
    return render(request, 'firstap/forms.html',{'form':form})



def register(request):
    if request.method=='POST':
        user_form = forms.FormUser(data=request.POST)
        profile_form = forms.FormUserInfo(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            #user to user field
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_picture = request.FILES['profile_pic']

            profile.save()
        return render(request,'firstap/index.html')
    else:
        user_form = forms.FormUser()
        profile_form = forms.FormUserInfo()
        return render(request,'firstap/register.html',{'user_form':user_form,'profile_form':profile_form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponse('login')
            else:
                return HttpResponse('acount not active')
        else:
            return HttpResponse('nikal bsdk')
    else:
        return render(request,'firstap/login.html')


@login_required
def logout_user(request):
    logout(request)
    return HttpResponse('logout dsuccesfully')
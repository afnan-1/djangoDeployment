from django.shortcuts import render
from protwo.models import User
from protwo.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,'firstap/index.html')

def user(request):
    form = NewUserForm()
    if request.method=='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            # ar = User.objects.get()
            # form.fields['first_name'] = 'mani'
            # a = form.cleaned_data['first_name']
            # a = a.upper()
            # print(a)
            # users(a)
            
            a= form.save(commit=False)
            a.first_name = 'mani'
            a.save()
            form.save_m2m()
            return index(request)
        else:
            raise 'Error try again'
    # else:        
    return render(request,'firstap/forms.html',{'form':form})



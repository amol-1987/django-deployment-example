from django.shortcuts import render
# from apptwo.models import User
from apptwo.forms import NewUser
# Create your views here.
def index(request):
    return render(request,'apptwo/index.html')

def user(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("error !!")

    return render(request,'apptwo/user.html',{'form':form})

from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("all_Post")
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def logout_view(request):
    return redirect('all_Post')


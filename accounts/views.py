
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.

# uploader signin
def uploaderSignin(request):

    if request.method == 'POST':
        user_name = request.POST['login-username']
        password = request.POST['login-password']
        user = auth.authenticate(username=user_name, password=password)
        

        if user is not None:  
            user_job = User.objects.get(pk = user.pk)
            if user.uploader:
                auth.login(request, user)
                return redirect('../uploader/dashboard')
            else:
                messages.info(request, "Your not uploader. Contact Admin.")
                return redirect("/")
        else :
            messages.info(request, "Invalid credentials... Try again.")
            return render(request, 'upload/signin.html')
    

    else:
        print()
        return render(request, 'upload/signin.html')


# viewer signin
def viewerSignin(request):

    if request.method == 'POST':
        user_name = request.POST['login-username']
        password = request.POST['login-password']
        
        
        user = auth.authenticate(username=user_name, password=password)

            

        if user is not None:
            #user_job = UserProfile.objects.get(pk = user.pk)
            if user.viewer:
                auth.login(request, user)
                return redirect('../viewer/dashboard')
            else:
                messages.info(request,"Your not Viewer. Contact Admin.")
                return redirect("/")
        else :
            messages.info(request, "Invalid credentials... Try again.")
            return render(request, 'view/signin.html')
    
 

    else:
        return render(request, 'view/signin.html')



        

# uploader signin
def verifierSignin(request):
    if request.method == 'POST':
        user_name = request.POST['login-username']
        password = request.POST['login-password']
        
        
        user = auth.authenticate(username=user_name, password=password)
            
        if user is not None:
            #user_job = UserProfile.objects.get(pk = user.pk)
            if user.verifier:
                auth.login(request, user)
                return redirect('../verifier/dashboard')
            else:
                messages.info(request, "Your not verifier. Contact Admin.")
                return redirect("/")
        else :
            messages.info(request, "Invalid credentials... Try again.")
            return render(request, 'verify/signin.html')
    

    else:
        return render(request, 'verify/signin.html')



def logout(request):
    auth.logout(request)
    return redirect('/')
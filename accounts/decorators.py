from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated: # if the user is already logged in, it will redirect to the home page
            return redirect('home')
        else: 
            return view_func(request, *args, **kwargs)
    return wrapper_func
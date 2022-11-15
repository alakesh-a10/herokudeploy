from django.http import HttpResponse
from django.shortcuts import redirect

def loginCheck(view_func):
    def wrapper(request, *args, **kargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kargs)
    return wrapper

def allowed_user(allowedRoles=[]):
    def userDecorator(viewFunc):
        def wrapper(request, *args, **kwrags):
            allowedRoles.append('Superuser')
            gr=None
            if request.user.groups.exists():
                gr=request.user.groups.all()[0].name
            print(gr)
            if gr in allowedRoles:
                return viewFunc(request, *args, **kwrags)
            else:
                return HttpResponse(
                    '<br><br><h1 style="text-align:center ">You are not allowed to visit this page</h1>'
                    )
            
        return wrapper
    return userDecorator




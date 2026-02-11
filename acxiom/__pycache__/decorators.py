from django.http import HttpResponse

def role_required(role):
    def wrapper(view):
        def inner(req,*a,**k):
            if not req.user.is_authenticated:
                return HttpResponse("Login required")
            if req.user.role != role:
                return HttpResponse("Unauthorized")
            return view(req,*a,**k)
        return inner
    return wrapper
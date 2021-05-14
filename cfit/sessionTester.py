import functools
from django.shortcuts import redirect


def login_required(func):
    f = func
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        try:
            if(args[0].session["usuario"]):
                pass
            else:
                raise Exception
        except:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return wrapper_login_required


def not_logged_only(func):
    f = func
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        try:
            if(args[0].session["usuario"]):
                raise Exception
            else:
                pass
        except:
            return redirect("/home")
        else:
            return f(*args, **kwargs)
    return wrapper_login_required


def adm_required(func):
    f = func
    @functools.wraps(func)
    def wrapper_login_required(*args, **kwargs):
        try:
            if(args[0].session["nivel_de_acesso"]==2):
                pass
            else:
                raise Exception
        except:
            return redirect("/")
        else:
            return f(*args, **kwargs)
    return wrapper_login_required

from django.shortcuts import render
from django.http import HttpResponse
from cfit.sessionTester import not_logged_only
from cfit.models import Mensagem, Config


def index(request):
    try:
        config = Config.objects.all().values()[0]
    except:
        return render(request, "index_deslogado.html")
    else:
        return render(request, "index_deslogado.html", {"config": config})


def index_msg(request):
    mensagem = Mensagem(
        nome=request.POST["mensagem_nome"],
        mensagem=request.POST["mensagem_texto"],
        tipo=1
    )
    mensagem.save()
    try:
        config = Config.objects.all().values()[0]
    except:
        return render(request, "index_deslogado.html")
    else:
        return render(request, "index_deslogado.html", {"config": config, "msg":  " <h4 class='alert alert-success' > SUCESSO </h4>"})

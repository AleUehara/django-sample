from django.http import HttpResponse


#http://maltzsama.blogspot.com.br/2009/09/acessar-sql-server-com-python.html


def index(request):
    return HttpResponse("Hello, world. You're at banco.")# Create your views here.


def detail(request, banco_id):
    return HttpResponse("You're looking at banco %s." % banco_id)

def results(request, banco_id):
    return HttpResponse("You're looking at the banco %s." % banco_id)

#def vote(request, poll_id):
#    return HttpResponse("You're voting banco%s." % poll_id)
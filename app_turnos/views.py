from django.shortcuts import render
# Create your views here.

def bienvenida(request):
    return render(request, 'bienvenida.html')


def pagina_no_encontrada(request, exception):
    return render(request, '404.html', status=404)



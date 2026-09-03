from django.shortcuts import render
# Create your views here.


def bienvenida(request):
    return render(request, 'bienvenida.html')

def home(request):
    return render(request, 'index.html')


def error_404(request, exception):
    return render(request, '404.html', status=404)



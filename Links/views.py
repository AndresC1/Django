from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def holamundo(request):
    lenguajes = ['Pseint', 'C', 'HTML', 'Css', 'JavaScript', 'python']
    return render(request, 'hola_mundo.html', {
        'nombres': 'Andres Alexander',
        'apellido': 'Cornejo Lira',
        'genero': 'Masculino',
        'edad': 19,
        'carrera': 'Ingenieria en Sistema de la informatica',
        'titulo': 'Datos',
        'lenguajes': lenguajes
    })

def inicio(request):
    year = range(2000, 2022)
    return render(request, 'index.html', {
        'year': year
    })

def contactos(request):
    return render(request, 'contactos.html')
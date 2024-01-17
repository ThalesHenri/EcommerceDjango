from django.http import HttpResponse
from django.shortcuts import render
def home_page(request):
    context = {
            "title": "pagina principal",
            "content": "Bem-Vindo a página principal"
    }
    return render(request, "index.html",context)

def about_page(request):    
    context = {
        "title": "pagina sobre",
        "content": "bem vindo a pagina sobre"
    }
    return render(request, "index.html",context)
def contact_page(request): 
    context = {
        "title": "pagina CONTATO",
        "content": "bem vindo a pagina Contatos"
    }
    return render(request, "index.html",context)
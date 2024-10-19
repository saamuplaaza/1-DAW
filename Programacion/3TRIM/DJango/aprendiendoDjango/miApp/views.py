# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    
    html = """
                <h1>Inicio</h1>
                <p>Años hasta 2050: </p>
                <ul>
            """
    year = 2021
    
    while year<=2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year +=1
    
    html += "</ul>"
    
    return HttpResponse(html)

def holaMundo(request):
    return HttpResponse("""
                        <h1> Hola mundo con Django</h1>
                        <h3>Soy Samuel Plaza</h3>
                        """)
    
def pagina(request):
    return HttpResponse("""
                        <h1>Página de mi Web</h1>
                        <p>Creado por Samuel</p>""")
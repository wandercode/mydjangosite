from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Welcome to My Django Site!</h1>
        <p>This is a simple Django website hosted on PythonAnywhere.</p>
    """)


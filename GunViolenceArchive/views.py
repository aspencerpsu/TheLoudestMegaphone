from django.shortcuts import render
from django.http import HttpResponse

def gv_form(request):
    return render(request, "form.html", {})

def gv_table(request):
    return render(request, "index.html", {})

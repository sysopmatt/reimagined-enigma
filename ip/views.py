from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


def index(request):
    return HttpResponse(ip_address)


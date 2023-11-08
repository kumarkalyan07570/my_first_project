from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kalyan(request):
    return HttpResponse("<h1><marqee> hai kalyan</marqee></h1>")
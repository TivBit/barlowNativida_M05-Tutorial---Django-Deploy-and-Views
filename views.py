# -*- coding: utf-8 -*-
"""
Created on %(Date: ___)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: ___
"""

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from stuff.users import User


bank_members = [
    User("Tiv", 43, "New Albany"),
    User("Tommy", 23, "Lexington"),
    User("Ariel", 22, "Lexington"),
    User("Malachi", 16, "New Albany"),
    User("Gabby", 14, "New Albany")
    ]

def homePage(request):
    page = ""
    page += "<!DOCTYPE html><html><head><title>Tips and API example"
    page += "</title></head><body>"
    page += "<h2>Welcome to SDEV 220 Bank!</h2>"
    
    page += "<p><a href=\"contacts\">API</a> &nbsp; &nbsp; &nbsp;"
    page += "<a href=\"atm\">ATM Machine</a> &nbsp; &nbsp; &nbsp;"
    page += "<a href=\"template\">Basic Template</a></p>"
    
    page += "</body></html>"
    
    return HttpResponse(page)


def basicTemplate(request):
    return render(request, "basic.html", {"title": "Template Page", "message": "What's good, Dynamic World?!"})


def calculateWithdraw(request):
    return render(request, "atmInput.html")


def displayWithdraw(request):
    balance = float(request.GET["balance"])
    withdrawAmount = float(request.GET["withdrawAmount"])
    print(balance, withdrawAmount)
    withdrawAmount /= 50
    newBalance = balance - withdrawAmount
    return render(request, "atmResponse.html", {"title": "Withdraw Today", "newBalance": format(withdrawAmount, ".2f")})



def simpleAPI(request):
    data = ""
    for b in bank_members:
        data += str(b) + "<br>"
    return HttpResponse(data)
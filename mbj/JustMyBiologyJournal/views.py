from django.shortcuts import render
import requests

def index(requests):
    return render(requests, 'JustMyBiologyJournal/index.html')
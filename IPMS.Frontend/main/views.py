from django.shortcuts import render
import requests

def home(request):
    return render(request, 'index.html')

def call_api(request):
    if request.method == "POST":
        response = requests.get("http://127.0.0.1:5000/get-minimum-portfolio")  # Replace with real API
        data = response.json()
        return render(request, 'index.html', {'api_data': data})
    return render(request, 'index.html', {'api_data': "Invalid request"})
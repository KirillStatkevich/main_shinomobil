from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def pricing(request):
    return render(request,'main/pricing.html')

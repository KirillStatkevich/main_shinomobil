from django.shortcuts import render, redirect
from .forms import online_zapis_form
from . import logic

# Create your views here.
def create_online(request):
    if request.method =='POST':
        form=online_zapis_form(request.POST)
        if form.is_valid():
            form.save()
            name = request.POST.get('name')
            phone_number = request.POST.get('phone_number')
            time = request.POST.get('time')
            date = request.POST.get('date')
            main_text = request.POST.get('main_text')
            place = request.POST.get('place')
            logic.bot_main_message(name, phone_number,time,date,main_text,place)
            return render (request,'main/online_success.html')
    else:
        form=online_zapis_form()
        return render(request, 'main/online.html', {'form':form})
    return render(request, 'main/online.html', {'form': form})

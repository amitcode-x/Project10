from datetime import datetime
from django.shortcuts import render

# Create your views here.


def filter(request):
    
   
    
    d = {'data': 'hellow this is filter ', 'uf' :'user define filter', 'dt': datetime.now()}
    
    return render(request ,'filter.html',d)  
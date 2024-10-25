# import urllib.request
# from django.shortcuts import render
# from myapp.forms import weartherforms
# import json

# def Mausham(request):
#     if(request.method=='POST'):
#         city=request.POST['city']
#         source=urllib.request.urlopen("http://api.weatherapi.com/v1/current.json?key=47fcd16ec051434db8764336242410&q="+city+"&aqi=yes").read()
#         list_of_data =json.loads(source)
#         data={
#             #'name':list_of_data['location']['name'],
#             #'temp':list_of_data['current']['temp_c']
#             'name':list_of_data['location']['name'],
#             'temp':list_of_data['current']['temp_c']
#         }
#         return render(request,'home.html',{'data':data})
#     else:
#         frm=weartherforms
#     return render(request,'index.html',{'form':frm})

import urllib.request
from django.shortcuts import render
from myapp.forms import weartherforms
import json

def display(request):
    if(request.method=='POST'):
        city=request.POST['city']
        source=urllib.request.urlopen("http://api.weatherapi.com/v1/current.json?key=47fcd16ec051434db8764336242410&q="+city+"&aqi=yes").read()
        list_of_data=json.loads(source)
        data={
            'name':list_of_data['location']['name'],
            'temp':list_of_data['current']['temp_c']
        }
        return render(request,'home.html',{'data':data})
    else:
        frm=weartherforms
    return render(request,'index.html',{'form':frm})

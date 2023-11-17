from django.shortcuts import render

# Create your views here.
def data(request):
     data1='this is the data from database'
     d={'database':data1,'database1':'kranthi'}

     return render(request,'data.html',context=d)
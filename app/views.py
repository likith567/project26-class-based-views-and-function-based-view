from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.

# returning string as response by using FBV

def fbv_string(request):
    return HttpResponse('This FBV string')

# returning string as response by using Class BV

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>This Class Based View String</h1>')


# returning Html Page as response by using FBV
def fbv_html(request):
    return render(request,'fbv.html')

# returning Html Page as response by using Class BV

class CbvHtml(View):
    def get(self,request):
        return render(request,'cbv.html')

# dealing with forms in FBV

def fbv_form(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        return HttpResponse(f'name is {name} and age is {age}')
    return render(request,'fbv_form.html')

# dealing with forms in Class BV

class CbvForm(View):
    def get(self,request):
        return render(request,'cbv_form.html')
    
    def post(self,request):
        name=request.POST['name']
        age=request.POST['age']
        return HttpResponse(f'name is {name} and age is {age}')


from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Contactform
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

def Homepage(request):
    # template = loader.get_template('Home.html')
    return render(request,'Home.html')   

def Skillpage(request):
    # template = loader.get_template('Home.html')
    return render(request,'Skillset.html')
def Aboutpage(request):
    # template = loader.get_template('Home.html')
    return render(request,'About.html')   

def Contactpage(request):
    # template = loader.get_template('Home.html')
    return render(request,'Contact.html')

# from these are language pages
def Clangpage(request):
    return render(request,'Clang.html')
def Javapage(request):
    return render(request,'Java.html')
def Pythonpage(request):
    return render(request,'python.html')
def Jangopage(request):
    return render(request,'Django.html')
def Reactpage(request):
    return render(request,'React.html')
def Nodepage(request):
    return render(request,'Node.html')
def Mangopage(request):
    return render(request,'Mangodb.html')
def Htmlpage(request):
    return render(request,'HTML.html')
def Csspage(request):
    return render(request,'CSS.html')
def Jspage(request):
    return render(request,'Javascript.html')


def Formdata(request):
    if request.method=='POST':
        contact = Contactform()
        Name =request.POST.get('name')
        Company =request.POST.get('comp')
        Email =request.POST.get('email','')
        Subject = request.POST.get('subject')
        contact.Name =Name
        contact.Company =Company
        contact.Email =Email
        contact.Subject = Subject
        contact.save()
        return HttpResponse('Thanks for contact me')
    return render(request,'Contact.html')


# Only for reading the data
@api_view(['GET'])
def Get_data(request):
    form_data = Contactform.objects.all()
    serializer =WebSerializer(form_data,many=True)
    return Response(serializer.data)

    #Only for posting the data 
@api_view(['POST'])
def Post_data(request):
    # movie_data = MovieModel.objects.all()
    serializer = WebSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
   

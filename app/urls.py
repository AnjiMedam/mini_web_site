from django.urls import path 
from. import views

urlpatterns = [
    path('',views.Homepage, name="home"),
    path('skill/',views.Skillpage,name="skill"),
    path('about/',views.Aboutpage,name="about"),
    path('contact/',views.Contactpage,name="contact"),
    path('data/',views.Formdata,name="formdata"),
    # languages paths
    path('clang/',views.Clangpage,name="clang"),
    path('java/',views.Javapage,name="java"),
    path('python/',views.Pythonpage,name="python"),
    path('jango/',views.Jangopage,name="jango"),
    path('react/',views.Reactpage,name="react"),
    path('node/',views.Nodepage,name="node"),
    path('mango/',views.Mangopage,name="mango"),
    path('html/',views.Htmlpage,name="html"),
    path('css/',views.Csspage,name="css"),
    path('js/',views.Jspage,name="js"),

    # api paths
    path('get/', views.Get_data, name='get_data'),
    path('add/', views.Post_data, name='post_data'),
]













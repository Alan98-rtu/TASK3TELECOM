# enhanced_HelloWorld/urls.py

from django.contrib import admin
from django.urls import path
from hello.views import enhanced_hello_world  # Import your view

# Define a simple view for the root path
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to the Home Page!</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enhanced/', enhanced_hello_world, name='enhanced_hello_world'),
    path('', home),  # Add a root URL pattern
]

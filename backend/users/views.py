from django.shortcuts import render
from .models import Users

# Create your views here.

#CRUD - Create, Retrieve, Update, Delete

#List all our users

def user_list_view(request):
    users_object = Users.objects.all()
    context = {
        'users_object': users_object
    }
    return render(request, "index.html", context)
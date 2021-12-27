from django.contrib import admin
from django.urls import path
from users.views import user_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list_view)
]

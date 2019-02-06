from django.contrib import admin  
from django.urls import path  
from micro import views

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('newLink/', views.newLink),
    path('read/',views.read),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),  
    path('remove/<int:id>', views.remove),
]
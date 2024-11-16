
from django.contrib import admin
from django.urls import path
from Student import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('details/<str:id>',views.details,name='details'),
    path('upload/',views.upload,name='upload'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.delete,name='delete'),
]

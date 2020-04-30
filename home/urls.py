from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('adding/',views.adding),
    path('updating/',views.updating),
    path('reset/',views.reset),    
]
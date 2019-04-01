from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('Empinfo/',views.EmpView),
    path('registration/',views.EmpReg, name='registration'),
    path('login/',views.login_user, name='login'),
    path('Info/', views.Myinfo, name = 'Info'),
]

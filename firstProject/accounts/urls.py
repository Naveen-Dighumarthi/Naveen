from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.home,name='index'),
    path('login/',views.login1,name="login"),
     path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='profile'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('verify_otp/',views.verify_otp,name='verify_otp'),
    path('reset_password/',views.reset_password,name='reset_password'),
]




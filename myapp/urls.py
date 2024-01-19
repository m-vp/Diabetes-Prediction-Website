from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signuppage,name = 'signup'),
    path('login/',views.loginpage,name = 'login'),
    path("predict/",views.predict, name = 'predict'),
    path("result/",views.result,name = 'result'),
    path('provide-feedback/', views.provide_feedback, name='provide_feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
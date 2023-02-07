from django.urls import path
from .views import HomePage, DetailPage

urlpatterns = [
    path('',HomePage.as_view(), name='home'),
    path('<slug:slug>/', DetailPage.as_view(), name='details'),
    

]
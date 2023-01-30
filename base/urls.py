from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='about'),
    # path('login/', views.loginPage, name='login'),
    path('others/', views.other, name='others'),
    # path('signup/', views.signup, name='signup'),
    path('movie/<id>/', views.movie, name='movie'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.reservation, name='reservation'),
    path('movies/', views.movies, name='movies'),
    path('comingsoon/', views.comingsoon, name='comingsoon'),
]
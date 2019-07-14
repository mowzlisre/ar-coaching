from django.urls import path
from . import views, mviews

urlpatterns = [
#web-path
    path('', views.content, name="content"),
    path('about/', views.about, name="about"),    
    path('contact/', views.contact, name="contact"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('create/',views.PostCreateView.as_view(),name='createpost'),
#mobile-path
    path('m/', mviews.content, name="mcontent"),
    path('m/about/', mviews.about, name="mabout"),    
    path('m/contact/', mviews.contact, name="mcontact"),
    path('m/login/', mviews.LoginView.as_view(), name="mlogin"),
    path('m/logout/', mviews.LogoutView.as_view(),name='mlogout'),
    path('m/create/', mviews.PostCreateView.as_view(),name='mcreatepost'),
    
]

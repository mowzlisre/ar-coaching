from django.urls import path
from . import views, mviews

urlpatterns = [
#web-path
    path('', views.content, name="content"),
    path('about/', views.about, name="about"),    
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('create/',views.PostCreateView.as_view(),name='createpost'),
#mobile-path
    path('m/', mviews.content, name="mcontent"),
    path('m/about/', mviews.about, name="mabout"),    
    path('m/login/', mviews.LoginView.as_view(), name="mlogin"),
    path('m/logout/', mviews.LogoutView.as_view(),name='mlogout'),
    path('m/create/', mviews.PostCreateView.as_view(),name='mcreatepost'),
#posts-routes web-path
    path('pgtrb/', views.pgtrb, name='pgtrb'),
    path('polytrb/', views.polytrb, name='polytrb'),
    path('engrtrb/', views.engrtrb, name='engrtrb'),
    path('tnset/', views.tnset, name='tnset'),
    path('gate/', views.gate, name='gate'),
#posts-routes mobile-path
    path('m/pgtrb/', mviews.pgtrb, name='mpgtrb'),
    path('m/polytrb/', mviews.polytrb, name='mpolytrb'),
    path('m/engrtrb/', mviews.engrtrb, name='mengrtrb'),
    path('m/tnset/', mviews.tnset, name='mtnset'),
    path('m/gate/', mviews.gate, name='mgate'),
]

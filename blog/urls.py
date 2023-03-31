from django.urls import path
from .views import *
from django.contrib import admin
from blog import views

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('category/<int:category_id>/', post_list_by_category, name='post_list_by_category'),
    path('fpost/<int:pk>/', FishDetailView.as_view(), name='fish_detail'),
    path('mpost/<int:pk>/', MammalsDetailView.as_view(), name='mammals_detail'),
    path('bpost/<int:pk>/', BirdsDetailView.as_view(), name='birds_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', Bloglist.as_view(), name='home'),
    path('birds/', BlogBirds.as_view(), name='birds'),
    path('mammals/', BlogMammals.as_view(), name='mammals'),
    path('fish/', BlogFish.as_view(), name='fish'),
    path('search/', Search.as_view(), name='search'),
    path('shue/', ShuePageView.as_view(), name='shue'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('gallery/', GalleryPageView.as_view(), name='gallery'),
    path('profile', profile_view, name="profile"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]

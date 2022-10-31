from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
	path('', views.ebook_api_index, name="ebook_api_index"),
	path('ebook-list/', views.ebookList, name="ebook-list"),
	path('ebook-detail/<str:pk>/', views.ebookDetail, name="ebook-detail"),
	path('ebook-create/', views.ebookCreate, name="ebook-create"),
	path('ebook-update/<str:pk>/', views.ebookUpdate, name="ebook-update"),
	path('ebook-delete/<str:pk>/', views.ebookDelete, name="ebook-delete"),
	path('register-user/', views.register, name="register-user"),
	path('login/',obtain_auth_token,name="login"),
	path('tokenauthentication-user',views.tokenauthenticationuser,name="tokenauthentication-user"),
 
]
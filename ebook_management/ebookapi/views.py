from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EbookSerializer, UserRegister
from .models import Ebook
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication





@api_view(['GET'])
def ebook_api_index(request):
	ebookapi_urls = {
		'List':'/ebook-list/',
		'Detail View':'/ebook-detail/<str:pk>/',
		'Create':'/ebook-create/',
		'Update':'/ebook-update/<str:pk>/',
		'Delete':'/ebook-delete/<str:pk>/',
		'User Register':'/register-user/',
		'User Login':'/login/',
		'Token Authentication-user':'/tokenauthentication-user/',
		}

	return Response(ebookapi_urls)


@api_view(['GET'])
def ebookList(request):
	ebooks = Ebook.objects.all().order_by('Title')
	review = request.query_params.get('Review','')
	genre = request.query_params.get('Genre','')
	favorite = request.query_params.get('Favorite', '')

	if genre:
		if genre in ("Fantasy", "Literary", "Mystery", "Non-Fiction", "Science Fiction", "Thriller"):
			genrefilterdata = Ebook.objects.filter(Genre=genre).order_by('Title')
			serializer = EbookSerializer(genrefilterdata, many=True)
			return Response(serializer.data)
		else:
			return Response("No Data. Genre available are Fantasy, Literary, Mystery, Non-Fiction, Science Fiction, and Thriller. Try again!")

	
	if favorite:
		if favorite == "False":
			favorite = False
		elif favorite == "True":
			favorite = True
		else:
			return Response("Try again with True or False!")

		favoritefilterdata = Ebook.objects.filter(Favorite=favorite).order_by('Title')
		serializer = EbookSerializer(favoritefilterdata, many=True)
		return Response(serializer.data)


	if review:
		if review == "1":
			review = 1
		elif review == "2":
			review = 2
		elif review == "3":
			review = 3
		elif review == "4":
			review = 4
		elif review == "5":
			review = 5
		else:
			return Response("No Data. Reviews available in 1-5 stars. Try again!")

		ebooksfilterdata = Ebook.objects.filter(Review=review).order_by('Title')
		serializer = EbookSerializer(ebooksfilterdata, many=True)
		return Response(serializer.data)
          		
	else:
		serializer = EbookSerializer(ebooks, many=True)	
		return Response(serializer.data)
	



@api_view(['GET'])
def ebookDetail(request, pk):
	ebook = Ebook.objects.get(id=pk)
	serializer = EbookSerializer(ebook, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def ebookCreate(request):
	serializer = EbookSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['PUT', 'GET'])
def ebookUpdate(request, pk):
	ebook = Ebook.objects.get(id=pk)
	serializer = EbookSerializer(instance=ebook, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def ebookDelete(request, pk):
	task = Ebook.objects.get(id=pk)
	task.delete()

	return Response('Ebook succsesfully deleted!')

@api_view(['POST'])
def register(request):
	serializer=UserRegister(data=request.data)
	data={}

	if serializer.is_valid():
		val=serializer.save()
		data['response']='registered'
		data['username']=val.username
		data['email']=val.email
		token,create=Token.objects.get_or_create(user=val)
		data['token']=token.key
	else:
		data=serializer.errors
	return Response(data)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def tokenauthenticationuser(request, format=None):
	content={'user':str(request.user),'userid':str(request.user.id)}
	return Response(content)


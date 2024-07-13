from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from .models import *

from django.http import HttpResponse
from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from App.serializers import *


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from App.serializers import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view
from django.db.models import Sum
from django.db import transaction


BASE_DIR = os.path.dirname(os.path.abspath(__file__))



def home(request):

    return render(request, 'App/home.html')


class GetAllHudumaView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            # categoryId = int(request.query_params.get('id'))
            # TypeId = int(request.query_params.get('TypeId'))
            


            queryset = Huduma.objects.all(
                # productCategory__id__icontains = categoryId,
                # Type__id__icontains = TypeId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = HudumaSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class GetMgawanjoWaHudumaView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            categoryId = int(request.query_params.get('id'))
            # TypeId = int(request.query_params.get('TypeId'))
            


            queryset = MgawanjoWaHuduma.objects.filter(
                Category__id__icontains = categoryId,
                # Type__id__icontains = TypeId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = MgawanjoWaHudumaSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







class GetAinaZaKukuView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            #categoryId = int(request.query_params.get('id'))
            # TypeId = int(request.query_params.get('TypeId'))
            


            queryset = AinaZaKuku.objects.all(
                #Category__id__icontains = categoryId,
                # Type__id__icontains = TypeId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = AinaZaKukuSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUmriWaKukuView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            #categoryId = int(request.query_params.get('id'))
            # TypeId = int(request.query_params.get('TypeId'))
            


            queryset = UmriWaKuku.objects.all(
                #Category__id__icontains = categoryId,
                # Type__id__icontains = TypeId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = UmriWaKukuSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






class GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            AinaYaKuku_ID = int(request.query_params.get('KukuId'))
            UmriWaKukuId = int(request.query_params.get('id'))
            


            queryset = TaarifaZaKuku.objects.filter(
                AinaYaKuku__id__icontains = AinaYaKuku_ID,
                UmriKwaWiki__id__icontains = UmriWaKukuId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = TaarifaZaKukuSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

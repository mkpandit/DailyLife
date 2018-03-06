#views.py

from django.shortcuts import render
from rest_framework import generics
from .serializers import contactSerializer
from contact.models import Contact

#View method for listing all records
class CreateView(generics.ListCreateAPIView):
	queryset = Contact.objects.all()
	serializer_class = contactSerializer
	http_method_names = ['get']

	def perform_create(self, serializer):
		serializer.save()

#view method for one record	
class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Contact.objects.all()
	serializer_class = contactSerializer
	http_method_names = ['get']
# serializers.py

from rest_framework import serializers
from contact.models import Contact

#Define serializers
class contactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = ('first_name', 'last_name', 'phone_number')
		#read_only_fields = ('date_created', 'date_modified')
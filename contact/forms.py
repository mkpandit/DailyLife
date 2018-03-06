from django import forms
from .models import Contact

class AddContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'profile_picture', 'phone_number', 'email_address', 'postal_address', 'country')

    def __init__(self, *args, **kwargs):
        super(AddContact, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
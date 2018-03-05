from django import forms
import pytz
from .models import to_do_list
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

utc = pytz.UTC

class AddTodo(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = to_do_list
        fields = ('to_do_time', 'to_do_title', 'description', 'to_do_priority', 'attachment',)
        labels = {
            'to_do_title' : _('To Do Title'),
            'description' : _('Description'),
            'attachment': _('Upload a file'),
        }
        widgets = {
            'to_do_time': forms.DateInput(attrs={'class': 'datepicker', 'id': 'date_input'})
        }

    #custom validation for the datetime input field
    def clean(self):
        form_data = self.cleaned_data
        to_do_time = form_data['to_do_time']
        to_do_time.replace(tzinfo=utc)
        if to_do_time < timezone.now():
            raise forms.ValidationError('You can not use a past date for this field')

    #add custom class to different form fields
    def __init__(self, *args, **kwargs):
        super(AddTodo, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['to_do_time'].widget.attrs.update({'class': 'form-control datepicker'})
from django.db import models
from django.urls import reverse

class to_do_list(models.Model):
    id = models.IntegerField(primary_key=True)
    to_do_time = models.DateTimeField(blank=False, null=True)
    to_do_title = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='uploads/', blank=True)
    priority_list = (
        ('Urgent', 'Urgent'), ('Normal', 'Normal'), ('Nice to do', 'Nice to do'),
    )
    to_do_priority = models.CharField(max_length=32, choices=priority_list, default='Normal')

    def __str__(self):
        return self.to_do_title

    #absolute urls for different operations
    def get_absolute_url(self):
        return reverse('todo_details', args=[str(self.id)])
    def get_absolute_delete(self):
        return reverse('todo_delete', args=[str(self.id)])
    def get_absolute_edit(self):
        return reverse('edit_todo', args=[str(self.id)])

    #generate classes for different priority
    def priority_class(self):
        if self.to_do_priority == 'Urgent':
            return "danger"
        elif self.to_do_priority == 'Normal':
            return "warning"
        else:
            return "info"
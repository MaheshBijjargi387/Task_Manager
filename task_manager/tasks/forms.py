from django.forms import ModelForm
from .models import*

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields = ['title', 'description', 'due_date', 'is_completed']
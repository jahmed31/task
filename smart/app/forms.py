from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block w-full border border-gray-300 rounded px-3 py-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full border border-gray-300 rounded px-3 py-2',
                'rows': 4
            }),
            'status': forms.Select(attrs={
                'class': 'block w-full border border-gray-300 rounded px-3 py-2'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'block w-full border border-gray-300 rounded px-3 py-2'
            }),
        }

from django import forms
from .models import Message  # Ensure the Message model is imported

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message  # Reference the Message model
        fields = ['sender', 'recipient', 'content']  # Specify the fields

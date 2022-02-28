from django import forms

from .models import Feedback
  
# create a ModelForm
class FeedbackForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
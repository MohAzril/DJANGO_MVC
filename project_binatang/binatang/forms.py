from django import forms
from .models import Hewan

class PostForm(forms.ModelForm):

   class Meta:
       model = Hewan
       fields = ('nama', 'species','berat','umur',)
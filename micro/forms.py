from django import forms
from micro.models import Micro

class MicroForm( forms.ModelForm ):
    class Meta:
        model = Micro
        fields = "__all__"


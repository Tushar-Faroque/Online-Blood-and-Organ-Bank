from django.forms import ModelForm
from .models import BloodTest

class BloodTestForm(ModelForm):
    class Meta:
        model = BloodTest
        fields = '__all__'
from django.forms import ModelForm
from .models import BloodTest

class BloodTestForm(ModelForm):
    """

	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.

	"""

    class Meta:
        model = BloodTest
        fields = '__all__'
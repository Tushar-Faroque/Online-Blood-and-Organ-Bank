from django.forms import ModelForm

from .models import GetBLOOD

class CustomerDetailsForm(ModelForm):
    """
	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.
	"""

    class Meta:
        model =  GetBLOOD
        fields = '__all__'
from django.forms import ModelForm
from .models import GetORGAN

class CustomerDetailsForm(ModelForm):
    """
	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.
	"""

    class Meta:
        model =  GetORGAN
        fields = '__all__'
from django.forms import ModelForm
from .models import DonateORGAN

class DonatorsDetailsForm(ModelForm):
    """
	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.
	"""

    class Meta:
        model =  DonateORGAN
        fields = '__all__'
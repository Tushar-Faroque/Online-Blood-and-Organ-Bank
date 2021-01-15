from django.forms import ModelForm
from .models import DonateBLOOD

class DonatorsDetailsForm(ModelForm):
    """
	This class takes a helper class ModelForm that 
    lets you create a Form class from a Django model.
	"""

    class Meta:
        model =  DonateBLOOD
        fields = '__all__'
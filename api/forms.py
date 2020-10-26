from django.forms import ModelForm
from django import forms
from api.models import VCT,Respondance,Prob_occur

class Manage_VCT(ModelForm):
    class Meta:
        model = VCT
        fields = '__all__'
     
class Manage_Respondance(ModelForm):
    class Meta:
        model = Respondance
        fields = '__all__'

class Manage_Prob_occur(ModelForm):
    class Meta:
        model = Prob_occur
        fields = '__all__'



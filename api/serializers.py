from rest_framework import serializers
from api.models import VCT,Prob_occur,Respondance

class VCTSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCT
        fields = '__all__'

class Prob_occurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prob_occur
        fields = '__all__'

class RespondanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respondance
        fields = '__all__'

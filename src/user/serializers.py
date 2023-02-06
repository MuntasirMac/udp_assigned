from rest_framework import serializers
from user.models import ParentAddress, Parent, Child

class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentAddress
        fields = '__all__'

class UpdateAddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=16, required=False)
    city = serializers.CharField(max_length=16, required=False)
    state = serializers.CharField(max_length=16, required=False)
    zip_code = serializers.CharField(max_length=16, required=False)
    
class CreateParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class UpdateParentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32, required=False)
    last_name = serializers.CharField(max_length=32, required=False)
    address = serializers.CharField(max_length=32, required=False)
    
    
class CreateChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class UpdateChildSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=32, required=False)
    last_name = serializers.CharField(max_length=32, required=False)
    parent = serializers.CharField(max_length=32, required=False)
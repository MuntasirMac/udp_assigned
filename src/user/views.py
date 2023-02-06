from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import ParentAddress, Parent, Child
from user.serializers import (
    CreateAddressSerializer,
    UpdateAddressSerializer,
    CreateParentSerializer,
    UpdateParentSerializer,
    CreateChildSerializer,
    UpdateChildSerializer,
)

class CreateAddressView(APIView):
    def post(self, request, format=None):
        create_address_serializer = CreateAddressSerializer(data=request.data)
        
        if create_address_serializer.is_valid():
            create_address_serializer.save()
            
            print(create_address_serializer.data)
            
            return Response({'data': create_address_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_address_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateAddressView(APIView):
    def put(self, request, *args, **kwargs):
        address_uid = kwargs.get('address_uid')
        update_address_serializer= UpdateAddressSerializer(data= request.data)

        if update_address_serializer.is_valid():

            update_address_data = update_address_serializer.validated_data

            address = ParentAddress.objects.filter(uuid = address_uid).first()
            print(address)

            update_address = ParentAddress.objects.filter(uuid = address_uid).update(
                                        street=update_address_data.get('street', address.street),
                                        city = update_address_data.get('city', address.city),
                                        state = update_address_data.get('state', address.state),
                                        zip_code = update_address_data.get('zip_code', address.zip_code)
                                        )


            print(update_address)

            if update_address: 
                updated_address = ParentAddress.objects.filter(uuid = address_uid).first()         
                return Response({'data' : model_to_dict(updated_address)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': update_address_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteAddressView(APIView):
    def delete(self, request, *args, **kwargs):
        address_uid = kwargs.get('address_uid')
        address = ParentAddress.objects.filter(uuid=address_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateParentView(APIView):
    def post(self, request, format=None):
        create_parent_serializer = CreateParentSerializer(data=request.data)
        
        if create_parent_serializer.is_valid():
            create_parent_serializer.save()
            
            print(create_parent_serializer.data)
            
            return Response({'data': create_parent_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_parent_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateParentView(APIView):
    def put(self, request, *args, **kwargs):
        parent_uid = kwargs.get('parent_uid')
        update_parent_serializer= UpdateParentSerializer(data= request.data)

        if update_parent_serializer.is_valid():

            update_parent_data = update_parent_serializer.validated_data

            parent = Parent.objects.filter(uuid = parent_uid).first()
            print(parent)

            update_parent = Parent.objects.filter(uuid = parent_uid).update(
                                        first_name = update_parent_data.get('first_name', parent.first_name) ,
                                        last_name = update_parent_data.get('last_name', parent.last_name),
                                        address = update_parent_data.get('address', parent.address)
                                        )


            print(update_parent)

            if update_parent: 
                updated_parent = Parent.objects.filter(uuid = parent_uid).first()         
                return Response({'data' : model_to_dict(updated_parent)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': update_parent_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteParentView(APIView):
    def delete(self, request, *args, **kwargs):
        parent_uid = kwargs.get('parent_uid')
        parent = Parent.objects.filter(uuid=parent_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateChildView(APIView):
    def post(self, request, format=None):
        create_child_serializer = CreateChildSerializer(data=request.data)
        
        if create_child_serializer.is_valid():
            create_child_serializer.save()
            
            print(create_child_serializer.data)
            
            return Response({'data': create_child_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'data': create_child_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateChildView(APIView):
    def put(self, request, *args, **kwargs):
        child_uid = kwargs.get('child_uid')
        update_child_serializer= UpdateChildSerializer(data= request.data)

        if update_child_serializer.is_valid():

            update_child_data = update_child_serializer.validated_data

            child = Child.objects.filter(uuid = child_uid).first()
            print(child)

            update_child = Child.objects.filter(uuid = child_uid).update(
                                        first_name=update_child_data.get('first_name', child.first_name),
                                        last_name = update_child_data.get('last_name', child.last_name),
                                        parent = update_child_data.get('parent', child.parent),
                                        )


            print(update_child)

            if update_child: 
                updated_child = Child.objects.filter(uuid = child_uid).first()         
                return Response({'data' : model_to_dict(updated_child)},status=status.HTTP_201_CREATED)
            else : 
                return Response({'data': "Unable To Update Data"}, status=status.HTTP_400_BAD_REQUEST) 
        else :    
            return Response({'data': update_child_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteChildView(APIView):
    def delete(self, request, *args, **kwargs):
        child_uid = kwargs.get('child_uid')
        child = Child.objects.filter(uuid=child_uid).delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
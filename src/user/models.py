from django.db import models
import uuid

# Create your models here.
class ParentAddress(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    street = models.CharField(max_length=16)
    city = models.CharField(max_length=16)
    state = models.CharField(max_length=16)
    zip_code = models.CharField(max_length=16)

class Parent(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    address = models.ForeignKey(ParentAddress, on_delete=models.CASCADE)
    
class Child(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
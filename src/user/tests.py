from django.test import TestCase
from user.models import Parent, ParentAddress
# Create your tests here.

class ParentTest(TestCase):
    """ Test module for Parent model """

    def setUp(self):
        ParentAddress.objects.create(
            street='street1', city='city1', state='state1', zip_code='test1'
        )
        ParentAddress.objects.create(
            street='street2', city='city2', state='state2', zip_code='test2'
        )
        # Parent.objects.create(
        #     first_name='Casper', last_name='John', address=)
        # Parent.objects.create(
        #     first_name='Muffin', last_name='Dean', address=2)

    def test_parent_address(self):
        parent_street1 = ParentAddress.objects.get(street='street1')
        parent_street2 = ParentAddress.objects.get(street='street2')
from django.urls import path, include
from user.views import (
                        CreateAddressView, UpdateAddressView, DeleteAddressView,
                        CreateParentView, UpdateParentView, DeleteParentView,
                        CreateChildView, UpdateChildView, DeleteChildView,
)

urlpatterns = [
    path('create-address/', CreateAddressView.as_view(), name='create-address'),
    path('update-address/<str:address_uid>/', UpdateAddressView.as_view(), name='update-address'),
    path('delete-address/<str:address_uid>/', DeleteAddressView.as_view(), name='delete-address'),
    path('create-parent/', CreateParentView.as_view(), name='create-parent'),
    path('update-parent/<str:parent_uid>/', UpdateParentView.as_view(), name='update-parent'),
    path('delete-parent/<str:parent_uid>/', DeleteParentView.as_view(), name='delete-parent'), 
    path('create-child/', CreateChildView.as_view(), name='create-child'),
    path('update-child/<str:child_uid>/', UpdateChildView.as_view(), name='update-child'),
    path('delete-child/<str:child_uid>/', DeleteChildView.as_view(), name='delete-child'),
]
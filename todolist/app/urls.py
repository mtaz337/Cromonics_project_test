from django.urls import path
from .views import *

urlpatterns = [
    path('create', CreateView.as_view(), name='create'),
    path('list', ListView.as_view(), name='list'),
    path('get/<int:pk>', SingleDataView.as_view(), name='get_data'),
]
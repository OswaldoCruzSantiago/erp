from django.urls import path
from core.erp.def_views.category.views import category_list

from core.erp.views import myfirstview

app_name = 'erp'

urlpatterns = [
    path('index/', myfirstview),
    path('uno/', category_list, name='category_list'),
]

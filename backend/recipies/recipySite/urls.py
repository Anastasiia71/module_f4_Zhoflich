from django.urls import path
from .views import CategoryyCreate, RecipiesList, RecipyDetail, RecipyCreate, CategoryList, CategoryDetail


urlpatterns = [
   path('', CategoryList.as_view(), name='category_list'), 
   path('<int:pk>', CategoryDetail.as_view(), name='category'),
   path('create/', CategoryyCreate.as_view(), name='category_create'),
   path('recepies/', RecipiesList.as_view(), name='recipies_list'), 
   path('recepies/<int:pk>', RecipyDetail.as_view(), name='recipy'),
   path('recepies/create/', RecipyCreate.as_view(), name='recipy_create'),
]
from django.urls import path
from .views import list, result, create, detail, update, delete

app_name = 'posts'

urlpatterns = [
    path('', list, name = 'list'),
    path('result/', result, name = 'result'),
    path('create/', create, name = 'create'),
    path('detail/<int:id>/', detail, name = 'detail'),
    path('update/<int:id>/', update, name = 'update'),
    path('delete/<int:id>/', delete, name = 'delete'),
]
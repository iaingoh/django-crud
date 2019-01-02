from django.urls import path
from .views import (IndexView, 
                    ItemCreate, 
                    success, 
                    ItemDetail,
                    ItemUpdate,
                    ItemDelete)

app_name = "expenses"

urlpatterns = [
    path('index/',  IndexView.as_view(), name='index'),
    path('new/', ItemCreate.as_view(), name='create'),
    path('success/', success, name='success'),
    path('detail/<int:pk>/', ItemDetail.as_view(), name='detail'),
    path('update/<int:pk>/', ItemUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ItemDelete.as_view(), name='delete')
]
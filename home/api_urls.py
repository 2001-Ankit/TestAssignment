from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogList.as_view(), name='blog-list'),
    path('blogs/create/', views.BlogCreate.as_view(), name='blog-create'),
    path('blogs/<int:pk>/', views.BlogRetrieve.as_view(), name='blog-retrieve'),
    path('blogs/<int:pk>/update/', views.BlogUpdate.as_view(), name='blog-update'),
    path('blogs/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog-delete'),
]

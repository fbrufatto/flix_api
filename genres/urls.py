from django.urls import path
from . import views
#from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    # path('genres/', genre_create_list_view, name='genre-create-list'),
    path('genres/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]
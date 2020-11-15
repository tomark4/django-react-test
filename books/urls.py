from django.contrib import admin
from django.urls import path
from .views import BookIndexView, BookDetailView, BookListView, BookByGenreView,BookAddView, BookStoreView

app_name = 'books'

urlpatterns = [
   path('', BookListView.as_view(), name='books_index'),
   path('list/', BookListView.as_view(), name='books_list'),
   path('list-by-genre/<str:genre>/',BookByGenreView.as_view(), name='books_by_genre'),
   path('detail/<slug:slug>/', BookDetailView.as_view(), name='books_detail'),
   path('add/', BookAddView.as_view(), name='books_add'),
   path('store/', BookStoreView.as_view(), name='books_store')
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace="blog")),
    path('api/', include('blogapi.urls', namespace="api")),
    path('test/', include('prueba.urls', namespace="prueba")),
    path('books/', include('books.urls', namespace="books")),
]

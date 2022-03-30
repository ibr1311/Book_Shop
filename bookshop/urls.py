from django.contrib import admin
from django.urls import path, include
from books.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('home/', genre_view, name='main_page_url')
]

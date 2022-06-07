
from django.urls import path, include

from books import views
app_name = 'books'

urlpatterns = [
    path('', views.latest_books_list),

]
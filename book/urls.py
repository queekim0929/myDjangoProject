from django.urls import re_path
from book import views
from django.urls import path 
from testkk.settings import DEBUG, STATIC_URL, STATIC_DIR, MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static

#app_name = 'book'

urlpatterns=[
    path('',views.index, name='index'),
    path('create/',views.create, name='create-book'),
    path('update/<int:book_id>',views.update_book),
    path('delete/<int:book_id>',views.delete_book)
    # MEDIA
]

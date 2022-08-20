from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail_in_url'),
    path('rooms', views.rooms_list, name="rooms"),
    path('new', views.new, name='new')
]
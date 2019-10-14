from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('uncross/<int:id>',views.uncross,name='uncross'),
    path('cross_off/<int:id>',views.cross_off,name='cross_off'),
    path('edit/<int:id>', views.edit, name='edit'),
]

from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='n0'),
    path('n1',views.n1, name='n1'),
    path('n2',views.n2, name='n2'),
    path('n3',views.n3, name='n3'),
    path('n4',views.n4, name='n4'),
    path('n5',views.n5, name='n5'),
    path('n6',views.n6, name='n6'),
]

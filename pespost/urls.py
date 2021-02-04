from django.urls import path
from .views import detailview, iconicListView, fpListView, legendListView

urlpatterns = [
    path('legendlist/', legendListView.as_view(), name='legendlist'),
    path('iconiclist/', iconicListView.as_view(), name='iconiclist'),
    path('fplist/', fpListView.as_view(), name='fplist'),
    path('detail/<int:pk>/', detailview, name='detail'),
]

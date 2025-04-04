from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('report/<int:pk>', views.report, name = 'report'),
]

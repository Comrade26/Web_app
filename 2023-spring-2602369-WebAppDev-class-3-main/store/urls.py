from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('orm_test/', views.orm_test)
]

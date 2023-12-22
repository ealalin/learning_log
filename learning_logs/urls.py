from django.urls import path
from . import views

urlpatterns = [
    # path("learning_log/", My_View.as_view(), name="my_view")  # CBV approach, remember to have class imported
    path('', views.My_View, name="my_view")  # FBV approach
]

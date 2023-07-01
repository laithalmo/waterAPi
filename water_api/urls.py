from django.urls import path,include
from . import views
urlpatterns = [
    path("cups",views.WaterList.as_view(),name="cups"),
    path("cups/<int:pk>",views.WaterDetails.as_view(),name="cups_details"),

]
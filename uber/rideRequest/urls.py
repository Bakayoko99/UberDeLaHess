from django.urls import path
from rideRequest import views
from . import views
urlpatterns = [
    path('',views.PriceEstimateList.as_view()),
   # path('<int:pk>/',views.PriceEstimateDetail.as_view()),
    path('',views.TimeEstimateList.as_view()),
   # path('<int:pk>/',views.TimeEstimateDetail.as_view()),

]
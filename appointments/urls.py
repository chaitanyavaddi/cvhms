from django.urls import path
# from .views import appointment_list
from .views import AppointmentListView

urlpatterns = [
    path('', AppointmentListView.as_view()),
]
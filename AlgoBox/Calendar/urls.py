from . import views
from django.urls import path

urlpatterns = [
	path('', views.CalendarView.as_view(), name='Calendar'),
]
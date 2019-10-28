from django.shortcuts import render
from django.views import generic
from APIServer.models import contest

class CalendarView(generic.ListView):
	queryset = contest
	template_name = 'calendar.html'
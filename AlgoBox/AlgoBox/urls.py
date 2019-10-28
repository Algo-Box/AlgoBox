from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Articles.urls')),
    path('calendar/', include('Calendar.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('enter/', include('Users.urls')),
]
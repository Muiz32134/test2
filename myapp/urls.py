from django.urls import path
from .views import home, information, dashboard_view

urlpatterns = [
    path('', home, name='home'),  # Root path (homepage)
    path('information/', information, name='information'),  # Information page
    path('dashboard/', dashboard_view, name='dashboard'),
]

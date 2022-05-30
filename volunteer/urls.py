from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from volunteer.views import VolunteerFormView, VolunteerListView, VolunteerDetailView

urlpatterns = [
    path('', include('addresses.urls')),
    path('admin/', admin.site.urls),
    path('register/', VolunteerFormView.as_view()),
    path('volunteers', VolunteerListView.as_view()),
    path('volunteers/<int:pk>', VolunteerDetailView.as_view()),
]

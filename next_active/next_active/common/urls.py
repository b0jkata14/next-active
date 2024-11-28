from django.urls import path

from next_active.common.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]

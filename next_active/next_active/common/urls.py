from django.urls import path

from next_active.common.views import HomePageView, TrainerListView, ReviewCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', TrainerListView.as_view(), name='dashboard'),
    path('trainer/<int:trainer_id>/review/', ReviewCreateView.as_view(), name='trainer-review'),
]

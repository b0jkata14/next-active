from django.urls import path

from next_active.packages import views

urlpatterns = [
    path('add/', views.PackageAddView.as_view(), name='package-add'),
]
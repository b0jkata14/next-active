from django.contrib.auth.views import LogoutView
from django.urls import path, include

from next_active.accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailView.as_view(), name='profile-detail'),
        path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    ]))
]
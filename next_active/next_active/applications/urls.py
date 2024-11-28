from django.urls import path, include

from next_active.applications import views

urlpatterns = [
    path('', views.TrainerApplicationsListView.as_view(), name='applications'),
    path('trainer/', views.TrainerApplicationRegisterView.as_view(), name='trainer-application-register'),
    path('<int:pk>/', include([
        path('', views.TrainerApplicationDetailView.as_view(), name='trainer-application-detail'),
        path('edit/', views.TrainerApplicationEditView.as_view(), name='trainer-application-edit'),
        path('approve/', views.TrainerApplicationApproveView.as_view(), name='trainer-application-approve'),
        path('reject/', views.TrainerApplicationRejectView.as_view(), name='trainer-application-reject'),
    ])),
]

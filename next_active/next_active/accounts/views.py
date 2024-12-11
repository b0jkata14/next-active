from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from next_active.accounts.forms import CustomerRegisterForm, ProfileEditForm, TrainerEditForm
from next_active.accounts.models import UserProfile, TrainerProfile

UserModel = get_user_model()


class AppUserRegisterView(CreateView):
    form_class = CustomerRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'accounts/profile-detail.html'
    context_object_name = 'profile'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'profile-detail',
            kwargs={'pk': self.object.pk},
        )


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserModel
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


class TrainerDetailView(DetailView):
    model = TrainerProfile
    template_name = 'accounts/trainer-detail.html'
    context_object_name = 'trainer'

    def get_queryset(self):
        return (
            super().get_queryset()
            .select_related('user', 'user__profile')
            .prefetch_related('packages', 'reviews')# Една заявка за всички свързани данни
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['packages'] = self.object.packages.all()  # Зареждане на пакети
        return context


class TrainerEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TrainerProfile
    form_class = TrainerEditForm
    template_name = 'accounts/trainer-edit.html'

    def test_func(self):
        profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        return self.request.user == profile.user

    def get_success_url(self):
        return reverse_lazy(
            'trainer-detail',
            kwargs={'pk': self.object.pk},
        )

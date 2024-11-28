from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View

from next_active.applications.forms import TrainerApplicationRegisterForm, TrainerApplicationEditForm
from next_active.applications.models import TrainerApplication


class TrainerApplicationsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = TrainerApplication
    template_name = 'applications/trainer-applications-list.html'
    context_object_name = 'applications'

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return TrainerApplication.objects.filter(is_pending=True)


class TrainerApplicationRegisterView(LoginRequiredMixin, CreateView):
    model = TrainerApplication
    form_class = TrainerApplicationRegisterForm
    template_name = 'applications/trainer-application-register.html'

    def dispatch(self, request, *args, **kwargs):
        pending_application = TrainerApplication.objects.filter(user=request.user, is_pending=True).first()

        if pending_application:
            return HttpResponseRedirect(
                reverse(
                    'trainer-application-detail',
                    kwargs={'pk': pending_application.pk},
                )
            )

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.is_pending = True

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'trainer-application-detail',
            kwargs={'pk': self.object.pk},
        )


class TrainerApplicationDetailView(LoginRequiredMixin, DetailView):
    model = TrainerApplication
    template_name = 'applications/trainer-application-detail.html'


class TrainerApplicationEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TrainerApplication
    form_class = TrainerApplicationEditForm
    template_name = 'applications/trainer-application-edit.html'

    def test_func(self):
        return self.request.user.is_staff

    def get_success_url(self):
        return self.request.path


class TrainerApplicationDecisionView(View):
    @staticmethod
    def change_status(application, is_approved=None, is_rejected=None):
        if is_approved:
            application.is_approved = is_approved

        if is_rejected:
            application.is_rejected = is_rejected

        application.is_pending = False
        application.decision_date = timezone.now()

        application.save()

    def post(self, request, pk, *args, **kwargs):
        application = get_object_or_404(TrainerApplication, id=pk)
        self.change_status(application)

        return redirect('applications')


class TrainerApplicationApproveView(LoginRequiredMixin, UserPassesTestMixin, TrainerApplicationDecisionView):
    def test_func(self):
        return self.request.user.is_staff

    def change_status(self, application, is_approved=None, is_rejected=None):
        return super().change_status(application, is_approved=True)


class TrainerApplicationRejectView(LoginRequiredMixin, UserPassesTestMixin, TrainerApplicationDecisionView):
    def test_func(self):
        return self.request.user.is_staff

    def change_status(self, application, is_approved=None, is_rejected=None):
        return super().change_status(application, is_rejected=True)

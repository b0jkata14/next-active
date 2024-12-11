from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView

from next_active.accounts.models import TrainerProfile
from next_active.applications.choices import SportChoices
from next_active.common.forms import ReviewForm


class HomePageView(TemplateView):
    template_name = 'common/index.html'


class TrainerListView(ListView):
    model = TrainerProfile
    template_name = 'common/dashboard.html'
    context_object_name = 'trainers'

    def get_queryset(self):
        queryset = TrainerProfile.objects.all()

        sport = self.request.GET.get('sport')

        if sport:
            queryset = queryset.filter(sport__icontains=sport)

        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(location__icontains=location)

        price = self.request.GET.get('price')
        if price:
            queryset = queryset.filter(price__lte=price)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sport_choices'] = SportChoices.choices

        return context


class ReviewCreateView(CreateView):
    form_class = ReviewForm
    template_name = 'common/reviews.html'

    def form_valid(self, form):
        # Get the trainer object from the URL
        trainer = get_object_or_404(TrainerProfile, pk=self.kwargs['trainer_id'])

        # Set the 'to_trainer' field and associate the logged-in user with the review
        form.instance.to_trainer = trainer
        form.instance.user = self.request.user  # Assuming the logged-in user is submitting the review

        # Save the review
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the trainer's review page after submitting the review
        return reverse_lazy('trainer-detail', kwargs={'pk': self.kwargs['trainer_id']})
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import CreateView

from next_active.packages.forms import PackageAddForm
from next_active.packages.models import Package


class PackageAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Package
    template_name = 'packages/package-add.html'
    form_class = PackageAddForm
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_trainer

    def form_valid(self, form):
        package = form.save(commit=False)
        package.user = self.request.user

        return super().form_valid(form)


# class PhotoEditPage(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Photo
#     form_class = PhotoEditForm
#     template_name = 'photos/photo-edit-page.html'
#
#     def test_func(self):
#         photo = get_object_or_404(Photo, slug=self.kwargs['pk'])
#         return self.request.user == photo.user
#
#     def get_success_url(self):
#         return reverse_lazy('photo-details', kwargs={'pk': self.object.pk})
#
# @login_required
# def photo_delete(request, pk: int):
#     photo = Photo.objects.get(pk=pk)
#
#     if request.user == photo.user:
#         photo.delete()
#
#     return redirect('index')
#
#
# class PhotoDetailsView(LoginRequiredMixin, DetailView):
#     model = Photo
#     template_name = 'photos/photo-details-page.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['likes'] = self.object.like_set.all()
#         context['comments'] = self.object.comment_set.all()
#         context['comment_form'] = CommentForm()
#         self.object.has_liked = self.object.like_set.filter(user=self.request.user).exists()
#
#         return context
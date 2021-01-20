from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from trains.forms import TrainForm
from trains.models import Train

__all__ = (
    'TrainListView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDetailView',
    'TrainDeleteView',
)


class TrainListView(ListView):
    model = Train
    paginate_by = 5
    template_name = 'trains/home.html'
    form = TrainForm

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       form = TrainForm()
       context['form'] = form
       return context


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train successfully created"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Train successfully changed"


class TrainDeleteView(SuccessMessageMixin, DeleteView):
    model = Train
    success_url = reverse_lazy('trains:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Train successfully deleted")
        return self.post(request, *args, **kwargs)



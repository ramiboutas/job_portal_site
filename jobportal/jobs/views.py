from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


from .models import Job, Category
from .forms import CreateJobForm

class HomeView(ListView):
    model = Job
    template_name = 'jobs/index.html'
    context_object_name = 'jobs'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CreateJobView(SuccessMessageMixin, CreateView):
    model = Job
    template_name = 'jobs/create-job.html'
    form_class = CreateJobForm
    success_url = '/'
    success_message = _('Job has been created')

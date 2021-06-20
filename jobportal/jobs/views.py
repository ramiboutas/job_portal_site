from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import method_decorator, login_required

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

@method_decorator(login_required(login_url='/'), name='dispatch')
class CreateJobView(SuccessMessageMixin, CreateView):
    model = Job
    template_name = 'jobs/create-job.html'
    form_class = CreateJobForm
    success_url = '/'
    success_message = _('Job has been created')

    def valid_form(self, form):
        job = form.save(commit=False)
        job.employer = self.request.user
        job.save()
        return super(CreateJobView, self).form_valid(form)


class SingleJobView(DetailView):
    model = Job
    template_name = 'jobs/single.html'
    context_object_name = 'job'

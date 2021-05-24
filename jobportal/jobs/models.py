from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

from jobportal import settings

JOB_TYPES_OPTIONS = (
('full_time', _('Full time')),
('part_time', _('Part time')),
('freelance', _('Freelance')),
('internship', _('Internship')),
('temporary', _('Temporary')),
)

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=None, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def job_count(self):
        return self.jobs.all().count()

class Job(models.Model):
    title = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    type = models.CharField(max_length=20, blank=False, default=None, choices=JOB_TYPES_OPTIONS)
    location = models.CharField(max_length=50, blank=False, default=None)
    description = models.TextField(blank=False, default=None)
    publishing_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default=None, editable=False)
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id', )

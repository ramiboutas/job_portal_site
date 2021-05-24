# Generated by Django 3.0.6 on 2021-05-24 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default=None, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('company', models.CharField(max_length=300)),
                ('type', models.CharField(choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('freelance', 'Freelance'), ('internship', 'Internship'), ('temporary', 'Temporary')], default=None, max_length=20)),
                ('location', models.CharField(default=None, max_length=50)),
                ('description', models.TextField(default=None)),
                ('publishing_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(default=None, editable=False)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobs.Category')),
                ('employer', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]

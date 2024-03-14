# Generated by Django 4.2.11 on 2024-03-14 15:10

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
            name='Trigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('trigger_date', models.IntegerField(choices=[(0, 'Pick a year and quarter'), (1, '2024-Q1'), (2, '2024-Q2'), (3, '2024-Q3'), (4, '2024-Q4'), (5, '2025-Q1'), (6, '2025-Q2'), (7, '2025-Q3'), (8, '2025-Q4')], default=0)),
                ('summary', models.TextField()),
                ('website_link', models.CharField(max_length=200, unique=True)),
                ('pr_link', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to=settings.AUTH_USER_MODEL)),
                ('trigger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='triggerlist.trigger')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

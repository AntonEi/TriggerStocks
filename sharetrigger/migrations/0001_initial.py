# Generated by Django 4.2.11 on 2024-03-17 16:10

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
            name='sharetrigger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggest_stock', models.CharField(max_length=200)),
                ('suggest_date', models.IntegerField(choices=[(0, 'Pick a year and quarter'), (1, '2024-Q1'), (2, '2024-Q2'), (3, '2024-Q3'), (4, '2024-Q4'), (5, '2024-H1'), (6, '2024-H2'), (7, '2025-Q1'), (8, '2025-Q2'), (9, '2025-Q3'), (10, '2025-Q4'), (11, '2025-H1'), (12, '2025-H2')], default=0)),
                ('suggest_summary', models.TextField()),
                ('more_info', models.CharField(max_length=200)),
                ('suggest_pr', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggester', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]

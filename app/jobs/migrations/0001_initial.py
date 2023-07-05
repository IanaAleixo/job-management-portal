# Generated by Django 4.2.3 on 2023-07-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('salary_range', models.PositiveIntegerField(blank=True, choices=[(0, 'up to 1.000'), (1, 'from 1.000 to 2.000'), (2, 'from 2.000 to 3.000'), (3, 'over 3.000')], default=0, verbose_name='Salary range')),
                ('requirements', models.CharField(max_length=255, verbose_name='Requirements')),
                ('schooling', models.PositiveIntegerField(blank=True, choices=[(0, 'Elementary School'), (1, 'High school'), (2, 'Technologist'), (3, 'University education'), (4, "Post / MBA / Master's"), (5, 'Doctorate degree')], default=0, verbose_name='Schooling')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this job should be treated as active. Unselect this instead of deleting accounts.', verbose_name='Active?')),
            ],
        ),
    ]
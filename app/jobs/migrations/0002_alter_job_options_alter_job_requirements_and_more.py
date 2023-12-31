# Generated by Django 4.2.3 on 2023-07-12 23:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.TextField(max_length=255, verbose_name='Requirements'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_range',
            field=models.PositiveIntegerField(blank=True, choices=[('up to 1.000', 'up to 1.000'), ('from 1.000 to 2.000', 'from 1.000 to 2.000'), ('from 2.000 to 3.000', 'from 2.000 to 3.000'), ('over 3.000', 'over 3.000')], default=0, verbose_name='Salary range'),
        ),
        migrations.AlterField(
            model_name='job',
            name='schooling',
            field=models.PositiveIntegerField(blank=True, choices=[('Elementary School', 'Elementary School'), ('High school', 'High school'), ('Technologist', 'Technologist'), ('University education', 'University education'), ("Post / MBA / Master's", "Post / MBA / Master's"), ('Doctorate degree', 'Doctorate degree')], default=0, verbose_name='Schooling'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expected_salary', models.FloatField(blank=True, max_length=255, null=True, verbose_name='Expected salary')),
                ('experience', models.CharField(blank=True, max_length=255, null=True, verbose_name='Experience')),
                ('last_education', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Education')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applicantions',
                'unique_together': {('job', 'user')},
            },
        ),
    ]

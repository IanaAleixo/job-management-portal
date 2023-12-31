# Generated by Django 4.2.3 on 2023-07-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_options_alter_job_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='expected_salary',
            field=models.FloatField(blank=True, choices=[('up to 1.000', 'up to 1.000'), ('from 1.000 to 2.000', 'from 1.000 to 2.000'), ('from 2.000 to 3.000', 'from 2.000 to 3.000'), ('over 3.000', 'over 3.000')], max_length=255, null=True, verbose_name='Expected salary'),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_education',
            field=models.CharField(blank=True, choices=[('Elementary School', 'Elementary School'), ('High school', 'High school'), ('Technologist', 'Technologist'), ('University education', 'University education'), ("Post / MBA / Master's", "Post / MBA / Master's"), ('Doctorate degree', 'Doctorate degree')], max_length=255, null=True, verbose_name='Last Education'),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary_range',
            field=models.FloatField(blank=True, choices=[('up to 1.000', 'up to 1.000'), ('from 1.000 to 2.000', 'from 1.000 to 2.000'), ('from 2.000 to 3.000', 'from 2.000 to 3.000'), ('over 3.000', 'over 3.000')], default=0, verbose_name='Salary range'),
        ),
    ]

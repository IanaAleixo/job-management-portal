# Generated by Django 4.2.3 on 2023-07-13 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_expected_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_education',
            field=models.CharField(blank=True, choices=[('Elementary_School', 'Elementary School'), ('High_school', 'High school'), ('Technologist', 'Technologist'), ('University_education', 'University education'), ("Post_MBA _Master's", "Post / MBA / Master's"), ('Doctorate_degree', 'Doctorate degree')], max_length=255, null=True, verbose_name='Last Education'),
        ),
    ]
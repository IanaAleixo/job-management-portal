# Generated by Django 4.2.3 on 2023-07-13 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_expected_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='expected_salary',
            field=models.CharField(choices=[('up_to_1000', 'up to 1.000'), ('from_1000_to_2000', 'from 1.000 to 2.000'), ('from_2000_to_3000', 'from 2.000 to 3.000'), ('over_3000', 'over 3.000')], default='up_to_1000', max_length=255, null=True, verbose_name='Expected salary'),
        ),
    ]
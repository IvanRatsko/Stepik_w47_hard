# Generated by Django 3.0.7 on 2020-06-12 16:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0003_auto_20200611_0234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'отклик', 'verbose_name_plural': 'отклики'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'компанию', 'verbose_name_plural': 'компании'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'специализацию', 'verbose_name_plural': 'специализации'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'вакансию', 'verbose_name_plural': 'вакансии'},
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

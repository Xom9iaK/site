# Generated by Django 5.1.3 on 2024-12-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fps', '0009_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('responsibilities', models.TextField()),
                ('requirements', models.TextField()),
                ('conditions', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]

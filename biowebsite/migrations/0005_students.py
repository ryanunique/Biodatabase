# Generated by Django 4.2.7 on 2023-11-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biowebsite', '0004_ongoin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=50)),
                ('event', models.CharField(max_length=100)),
            ],
        ),
    ]

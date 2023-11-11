# Generated by Django 4.2.7 on 2023-11-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Common_Name', models.CharField(max_length=100)),
                ('Family_Name', models.CharField(max_length=100)),
                ('Scientific_Name', models.CharField(max_length=100)),
                ('Conservation_status', models.CharField(max_length=100)),
                ('image_link', models.TextField()),
            ],
        ),
    ]

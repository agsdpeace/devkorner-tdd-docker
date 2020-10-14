# Generated by Django 3.0.5 on 2020-10-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('linkedin', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
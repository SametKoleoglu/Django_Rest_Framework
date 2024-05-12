# Generated by Django 5.0.6 on 2024-05-11 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journalist', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
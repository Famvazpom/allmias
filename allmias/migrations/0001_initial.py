# Generated by Django 3.2.13 on 2022-09-14 17:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mamography',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=(224, 224), upload_to='mammography/')),
                ('etiqueta', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
    ]
# Generated by Django 3.2 on 2023-04-20 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head_image', models.ImageField(blank=True, upload_to='dr_f_app/images/')),
            ],
        ),
    ]
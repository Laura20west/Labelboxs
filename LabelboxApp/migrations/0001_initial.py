# Generated by Django 4.1 on 2024-12-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Job', models.CharField(max_length=100)),
                ('hotel_Main_Img', models.ImageField(default='SOME STRING', upload_to='images/')),
                ('release_date', models.DateField()),
            ],
        ),
    ]

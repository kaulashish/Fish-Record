# Generated by Django 4.0.3 on 2022-03-25 07:44

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
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('length', models.FloatField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

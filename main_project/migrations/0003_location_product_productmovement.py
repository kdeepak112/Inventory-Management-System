# Generated by Django 3.2.3 on 2021-09-22 17:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_project', '0002_auto_20210922_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMovement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 9, 22, 22, 43, 30, 235083))),
                ('qty', models.IntegerField()),
                ('from_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main_project.location')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main_project.product')),
                ('to_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main_project.location')),
            ],
        ),
    ]
# Generated by Django 3.2.7 on 2021-11-29 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_logs', '0004_children_height'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=60)),
                ('number_of_doses', models.IntegerField()),
                ('number_of_doses_taken', models.IntegerField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_logs.children')),
            ],
        ),
        migrations.CreateModel(
            name='SleepLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_logs.children')),
            ],
        ),
        migrations.CreateModel(
            name='GrowthLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now=True)),
                ('height', models.IntegerField()),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_logs.children')),
            ],
        ),
        migrations.CreateModel(
            name='DiaperChangeLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=250)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_logs.children')),
            ],
        ),
    ]

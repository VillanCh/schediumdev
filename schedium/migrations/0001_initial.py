# Generated by Django 2.1.2 on 2018-10-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchediumDelayModelTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(default='default', max_length=2000)),
                ('relative_id', models.CharField(max_length=2000)),
                ('start_time', models.DateTimeField()),
                ('delay_seconds', models.PositiveIntegerField()),
                ('next_execute_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SchediumLoopModelTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(default='default', max_length=2000)),
                ('relative_id', models.CharField(max_length=2000)),
                ('first', models.BooleanField(default=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('interval_seconds', models.PositiveIntegerField()),
                ('end_time', models.DateTimeField(null=True)),
                ('next_execute_datetime', models.DateTimeField()),
                ('is_finished', models.BooleanField()),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-29 02:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchediumDelayModelTask',
            fields=[
                ('schedium_id', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('task_type', models.CharField(default='default', max_length=2000)),
                ('relative_id', models.CharField(max_length=2000)),
                ('start_time', models.DateTimeField()),
                ('delay_seconds', models.PositiveIntegerField()),
                ('next_execute_datetime', models.DateTimeField()),
                ('is_finished', models.BooleanField(default=False)),
                ('in_sched', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SchediumLoopModelTask',
            fields=[
                ('schedium_id', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('task_type', models.CharField(default='default', max_length=2000)),
                ('relative_id', models.CharField(max_length=2000)),
                ('first', models.BooleanField(default=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('interval_seconds', models.PositiveIntegerField()),
                ('end_time', models.DateTimeField(null=True)),
                ('next_execute_datetime', models.DateTimeField()),
                ('is_finished', models.BooleanField(default=False)),
                ('in_sched', models.BooleanField(default=False)),
            ],
        ),
    ]

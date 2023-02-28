# Generated by Django 4.0.6 on 2023-01-28 23:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import workouts.models.exercise
import workouts.models.workout_day
import workouts.models.workout_day_exercise


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_goal_alter_disability_name_workout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Dati numele exercitiului', max_length=20)),
                ('description', models.TextField()),
                ('video', models.FileField(null=True, upload_to=workouts.models.exercise.video_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('muscle_group', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(help_text='Numarul zilei', validators=[workouts.models.workout_day.validate_day])),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workout')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='WorkoutDayExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.CharField(choices=[('Timp', 'Timp'), ('Seturi si Repetitii', 'Seturi si Repetitii')], default='Seturi si Repetitii', max_length=20)),
                ('time', models.IntegerField(default=0, validators=[workouts.models.workout_day_exercise.validate])),
                ('sets', models.IntegerField(default=0, validators=[workouts.models.workout_day_exercise.validate])),
                ('repetitions', models.IntegerField(default=0, validators=[workouts.models.workout_day_exercise.validate])),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.exercise')),
                ('workout_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workouts.workoutday')),
            ],
            options={
                'ordering': ['workout_day'],
            },
        ),
    ]

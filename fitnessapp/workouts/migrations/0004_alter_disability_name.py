# Generated by Django 4.0.6 on 2023-01-29 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_exercise_workoutday_workoutdayexercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disability',
            name='name',
            field=models.CharField(help_text='Dati numele dizabilitatii', max_length=200),
        ),
    ]

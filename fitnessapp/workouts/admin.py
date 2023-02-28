from django.contrib import admin
from .models import Workout, WorkoutDay, WorkoutDayExercise, Goal, Disability, Exercise

admin.site.register(Workout)
admin.site.register(WorkoutDay)
admin.site.register(WorkoutDayExercise)
admin.site.register(Goal)
admin.site.register(Disability)
admin.site.register(Exercise)

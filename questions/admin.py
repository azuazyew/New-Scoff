from django.contrib import admin


from .models import *


admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)
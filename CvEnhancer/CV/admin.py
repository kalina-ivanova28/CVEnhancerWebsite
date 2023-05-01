from django.contrib import admin

from .models import Experience
from .models import Skill
from .models import Rate


admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Rate)

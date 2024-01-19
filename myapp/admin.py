from django.contrib import admin

# Register your models here.
from .models import Result
from .models import Feedback

admin.site.register(Result)
admin.site.register(Feedback)

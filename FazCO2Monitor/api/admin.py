from django.contrib import admin
from .models import PPMData, NowPPM

# Register your modelsNowPPM here.

admin.site.register(PPMData)
admin.site.register(NowPPM)
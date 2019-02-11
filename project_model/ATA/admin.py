from django.contrib import admin
from .models import Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,Live_code

my_model = [Direksi,Mentee,Mentor,Mata_pelajaran,Challenge,Live_code]
admin.site.register(my_model)
# Register your models here.
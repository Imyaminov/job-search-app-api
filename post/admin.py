from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Status)
admin.site.register(Post)
admin.site.register(Region)
admin.site.register(ProfessionalField)
admin.site.register(OfficialPosition)


# from django.apps import apps
# models = apps.get_models()
# for model in models:
#     admin.site.register(model)

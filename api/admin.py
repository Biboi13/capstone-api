from django.contrib import admin
from .models import VCT,Prob_occur,Respondance

# Register your models here.
class VCTAdminLook(admin.ModelAdmin):
    list_display =['pk', 'vct_name', 'vct_active_users', 'vct_developer']

admin.site.register(Prob_occur)
admin.site.register(Respondance)
admin.site.register(VCT,VCTAdminLook)



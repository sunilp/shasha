from django.contrib import admin

# Register your models here.
from .models import Register

class RegisterAdmin(admin.ModelAdmin):
	list_display = ['email','timestamp','updated']
	class Meta:
		model = Register


admin.site.register(Register,RegisterAdmin)
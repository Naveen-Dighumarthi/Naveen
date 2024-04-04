from django.contrib import admin
from htmlwebsite.models import Contact,LoginForm,SignupForm

# Register your models here.

admin.site.register(Contact)
admin.site.register(LoginForm)
admin.site.register(SignupForm)

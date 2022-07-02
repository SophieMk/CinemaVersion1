from django.contrib import admin

# Register your models here.
@admin.register(Movie)
class UserAdmin(admin.ModelAdmin):
    pass
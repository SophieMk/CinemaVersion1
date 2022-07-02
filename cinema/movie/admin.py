from django.contrib import admin

# Register your models here.
@admin.Register(Movie)
class UserAdmin(admin.ModelAdmin):
    pass
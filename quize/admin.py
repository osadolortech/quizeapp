from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Category)

class Catadmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
@admin.register(models.Quizes)
class Quizeadmin(admin.ModelAdmin):
    list_display = [
        'id','title'
    ]

class AswerAdminIline(admin.TabularInline):
    model = models.Answers
    fields = [
        "answer_text", "is_right"
    ]

@admin.register(models.Quesion)
class Questionadmin(admin.ModelAdmin):
    fields = [
        "title",'quize'
    ]
    list_display = [
        'title',"quize","date_created"
    ]

    inlines = [
        AswerAdminIline
    ]
    

@admin.register(models.Answers)
class QAnsweAdmin(admin.ModelAdmin):
    list_display = [
        "answer_text","is_right","question"
    ]
from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ['votes']
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    readonly_fields = ['was_published_recently']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'was_published_recently']})
    ]
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'get_question_text', 'votes']
    readonly_fields = ['votes']
    search_fields = ['choice_text', 'question__question_text']

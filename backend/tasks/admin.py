from django.contrib import admin

from .models import (
    Task, TaskImageAttachment,
    Answer, AnswerImageAttachment
)

admin.site.register(Task)
admin.site.register(TaskImageAttachment)
admin.site.register(Answer)
admin.site.register(AnswerImageAttachment)

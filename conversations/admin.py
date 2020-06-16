from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ convercation Admin Definition """

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ convercation Admin Definition """

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )

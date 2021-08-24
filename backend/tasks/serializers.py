from rest_framework.serializers import ModelSerializer
from drf_extra_fields.fields import Base64ImageField

from .models import Task, TaskImageAttachment, Answer, AnswerImageAttachment


class TaskImageAttachmentSerilaizer(ModelSerializer):
    """ TaskImageAttachment model Serializer """
    image = Base64ImageField(write_only=True)

    class Meta:
        model = TaskImageAttachment
        fields = (
            "id",
            "task",
            "image",
        )


class TaskSerializer(ModelSerializer):
    """ Task model Serializer """
    images_set = TaskImageAttachmentSerilaizer(many=True, required=False)
    
    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "text",
            "posted_by",
            "images_set"
        )

    def get_validation_exclusions(self):
        exclusions = super(TaskSerializer, self).get_validation_exclusions()
        return exclusions + ['images_set']


class AnswerImageAttachmentSerializer(ModelSerializer):
    """ AnwerImageAttachment model Serializer """
    class Meta:
        model = AnswerImageAttachment
        fields = "__all__"


class AnswerSerialzier(ModelSerializer):
    """ Answer model Serializer """
    images_set = AnswerImageAttachmentSerializer(many=True, required=False)

    class Meta:
        model = Answer
        fields = (
            "id",
            "text",
            "task",
            "posted_by",
            "images_set"
        )

    def get_validation_exclusions(self):
        exclusions = super(AnswerSerialzier, self).get_validation_exclusions()
        return exclusions + ["images_set"]

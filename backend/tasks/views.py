from rest_framework.viewsets import ModelViewSet
from dry_rest_permissions.generics import DRYPermissions

from .models import Task, Answer
from .serializers import (
    TaskSerializer, TaskImageAttachmentSerilaizer,
    AnswerSerialzier, AnswerImageAttachmentSerializer,
)

class TaskModelView(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (DRYPermissions,)
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Task.objects.all()


class AnswerModelView(ModelViewSet):
    serializer_class = AnswerSerialzier
    permission_classes = (DRYPermissions,)
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        return Answer.objects.filter(task__pk=self.kwargs['task_pk'])

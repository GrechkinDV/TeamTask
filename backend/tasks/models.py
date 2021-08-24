from django.db import models
from django.contrib.auth.models import BaseUserManager

from rest_framework.serializers import ValidationError
from dry_rest_permissions.generics import authenticated_users


class TaskManager(BaseUserManager):
    """ Manager for Task model """

    use_in_migrations = True

    def create_task(self, title: str, text: str, posted_by, images_set=None):
        """
        Create a Task
        :param title: title of a task
        :type title: str
        :param text: assignment of a task
        :type text: str
        :param posted_by: the user posted the task
        :type posted_by: django.contrib.auth.models.User
        """
        # Check if the fields are set
        for key, value in {
            "вопрос": title,
            "текст вопроса": text,
            "posted_by": posted_by,
        }.items():
            if value is None or value == "":
                raise ValidationError(f"Введите {key}!")
        # Create object
        task = self.model(
            title=title,
            text=text,
            posted_by=posted_by
        )
        # Save the image attachments
        images_set = images_set if images_set else []
        for image in images_set:
            if image:
                TaskImageAttachment.objects.update_or_create(
                    task=task, image=image["image"]
                )

        return task


class Task(models.Model):
    """ Model for tasks """
    title = models.CharField(max_length=2500)
    text = models.TextField()
    posted_by = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)

    objects = TaskManager()

    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    @authenticated_users
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return True

    def has_object_read_permission(self, request):
        return True


class AnswerManager(BaseUserManager):
    """ Manager for Answer model """

    use_in_migrations = True

    def create_answer(self, text: str, task: Task, posted_by, images_set: None):
        """
        Create an Answer
        :param text: text of an answer
        :type text: str
        :param task: the task the answer refers to
        :type task: Task
        :param posted_by: the user posted the answer
        :type posted_by: django.contrib.auth.models.User
        """
        # 1. Check if the fields are set
        for key, value in {
            "текст ответа": text,
            "ответ": task,
            "posted_by": posted_by,
        }.itmes():
            if value is None or value == "":
                raise ValidationError(f"The {key} parameter must be set")
        # 2. Create object
        answer = self.model(
            text=text,
            task=task,
            posted_by=posted_by
        )
        # 3. Save the image attachments
        images_set = images_set if images_set else []
        for image in images_set:
            AnswerImageAttachment.objects.update_or_create(answer=answer, image=image)

        return answer


class Answer(models.Model):
    """ Model for answers """
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    posted_by = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)

    objects = AnswerManager
    
    @staticmethod
    def has_read_permission(request):
        return True

    @staticmethod
    @authenticated_users
    def has_write_permission(request):
        return True

    def has_object_write_permission(self, request):
        return True

    def has_object_read_permission(self, request):
        return True


class AnswerImageAttachment(models.Model):
    """ Model for image attachments to Answers """
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="images_set")
    image = models.ImageField()


class TaskImageAttachment(models.Model):
    """ Model for image attachments to Tasks """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="images_set")
    image = models.ImageField()

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.core.exceptions import ValidationError

from dry_rest_permissions.generics import authenticated_users


class AccountManager(BaseUserManager):
    """ Manager for Account model """

    use_in_migrations = True

    def create_user(self, email, name="Team Tasker", password="SSO", institution=""):
        """
            Create account
            :param email: Email required
            :type email: email
            :param name: Name of a user
            :type name: str
            :param institution: Educational institution user is attending
            :type institution: str 
        """
        if password == "SSO":
            password = self.make_random_password()
        email = self.normalize_email(email)

        # Check that values are set
        for key, value in {"email": email}.items():
            if value == "":
                raise ValidationError(f"Введите {key}!", code=400)

        # Create the object
        user = self.model(
            email=email,
            name=name,
            institution=institution,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
        
    def create_superuser(self, email, name, password):
        """ Create admin account """
        user = self.create_user(email, name, password)
        user.is_admin = True
        user.save()
        return user

    def get_object_or_404(self, id):
        """ Get object or raise 404 """
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            raise ValidationError("Account matching query does not exist.", code=404)


class Account(AbstractBaseUser, PermissionsMixin):
    """ Custom user """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    institution = models.CharField(max_length=500, blank=True)

    # Abstract BaseUser requirement
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]
    is_active = models.BooleanField(default=True)

    objects = AccountManager()

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    @staticmethod
    @authenticated_users
    def has_read_permission(request):
        return True

    @staticmethod
    @authenticated_users
    def has_write_permission(request):
        return True

    def has_object_read_permission(self, request):
        return True # Temporary

    def has_oject_write_permission(self, request):
        return True # Temporary

    def has_object_update_permission(self, request):
        return True # Temporary


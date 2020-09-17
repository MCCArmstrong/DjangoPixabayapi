from django.db import models
from .validators import validate_file_extension
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
#
#
# class Users(AbstractUser):
#     email = models.EmailField(_('Email field'))


# Create your models here.

class UploadFile(models.Model):
    file_format = models.FileField(upload_to='media/', validators=[validate_file_extension], help_text='upload a file')
    file_name = models.CharField(max_length=100, help_text='add a file description')

    def __str__(self):
        return self.file_name

import os
import html
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    extension = os.path.splitext(value.name)[1]
    allowed_extension = ['.jpg', '.png', '.jpeg']
    if not extension.lower() in allowed_extension:
        raise ValidationError("This is a supported image format")

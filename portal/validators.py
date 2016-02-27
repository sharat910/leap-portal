import os
from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.Please upload a document in doc, docx or pdf format.')

def validate_file_extension_intro(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.ppt', '.pptx']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.Please upload a presentation in ppt or pptx format.')

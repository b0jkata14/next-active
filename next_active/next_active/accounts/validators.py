from django.core.exceptions import ValidationError


# def validate_image_format(image=False):
#     if image:
#         valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
#         ext = image.name.split('.')[-1].lower()
#         if ext not in valid_extensions:
#             raise ValidationError("Only JPG, PNG, and WebP files are supported.")

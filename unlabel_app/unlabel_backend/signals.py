import cloudinary

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Project, ProjectImage

@receiver(pre_delete, sender=Project)
def project_photo_delete(sender, instance, **kwargs):
	cloudinary.uploader.destroy(instance.cover_image.public_id)


@receiver(pre_delete, sender=ProjectImage)
def project_image_photo_delete(sender, instance, **kwargs):
	cloudinary.uploader.destroy(instance.image.public_id)

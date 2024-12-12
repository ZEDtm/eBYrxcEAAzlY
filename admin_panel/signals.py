from time import sleep

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from loguru import logger

from .models import TgUser, InviteUser, GroupUser


@receiver(pre_save, sender=InviteUser)
def create_tg_user(sender, instance: InviteUser, **kwargs):
    logger.info('create')
    user = TgUser.objects.create(
        fio=instance.fio,
        phone=instance.phone,
        ref_code=TgUser.generate_ref_code(),
        api_key=instance.api_key,
        workers=instance.workers,
    )

    instance.user = user




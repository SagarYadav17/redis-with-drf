from django.dispatch import receiver
from django.db.models.signals import post_save
from config.utils import delete_cache

from test_app.models import TestModel


@receiver(post_save, sender=TestModel)
def delete_cache_on_changes(sender, instance, created, **kwargs):
    """
    Signal to delete the cache on changes to the TestModel instance
    """
    delete_cache("test-view")

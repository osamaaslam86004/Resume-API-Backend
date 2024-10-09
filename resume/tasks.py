from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


import logging

logger = logging.getLogger(__name__)


@shared_task
def delete_blacklisted_tokens():
    tokens = BlacklistedToken.objects.all()
    logger.info(f"Total tokens: {tokens.count()}")

    cutoff_time = timezone.now() - timedelta(days=1)
    logger.info(f"Cutoff time: {cutoff_time}")

    for token in tokens:
        logger.info(f"Token ID: {token.id}, blacklisted_at: {token.blacklisted_at}")

    tokens_to_delete = tokens.filter(blacklisted_at__lt=cutoff_time)
    logger.info(f"Tokens to delete: {tokens_to_delete.count()}")

    if tokens_to_delete.exists():
        tokens_to_delete.delete()
        logger.info("Deleted tokens successfully")
    else:
        logger.info("No tokens to delete")

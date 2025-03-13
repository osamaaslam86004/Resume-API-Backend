import logging
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from rest_framework_simplejwt.token_blacklist.models import (  # OutstandingToken,
    BlacklistedToken,
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Delete blacklisted JWT tokens older than 24 hours"

    def handle(self, *args, **kwargs):
        self.delete_blacklisted_tokens()

    def delete_blacklisted_tokens(self):
        tokens = BlacklistedToken.objects.all()
        logger.info(f"Total tokens: {tokens.count()}")

        cutoff_time = timezone.now() - timedelta(days=1)
        logger.info(f"Cutoff time: {cutoff_time}")

        tokens_to_delete = tokens.filter(blacklisted_at__lt=cutoff_time)
        logger.info(f"Tokens to delete: {tokens_to_delete.count()}")

        if tokens_to_delete.exists():
            tokens_to_delete.delete()
            logger.info("Deleted tokens successfully")
        else:
            logger.info("No tokens to delete")

        print(f"My scheduled task ran at {timezone.now()}")


# class Command(BaseCommand):
#     help = "Delete all tokens in the OutstandingToken table that have been blacklisted"

#     def handle(self, *args, **kwargs):

#         blacklisted_tokens = BlacklistedToken.objects.values_list("token_id", flat=True)
#         deleted, _ = OutstandingToken.objects.filter(
#             token_id__in=blacklisted_tokens
#         ).delete()
#         self.stdout.write(
#             self.style.SUCCESS(
#                 f"Successfully deleted {deleted} blacklisted outstanding tokens"
#             )
#         )

#         count, _ = BlacklistedToken.objects.all().delete()
#         self.stdout.write(
#             self.style.SUCCESS(f"Successfully deleted {count} blacklisted tokens")
#         )

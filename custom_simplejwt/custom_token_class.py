from rest_framework_simplejwt.tokens import (
    Token,
    # RefreshToken,
    # BlacklistMixin,
)

# from rest_framework_simplejwt.utils import get_md5_hash_password
# from rest_framework_simplejwt.exceptions import AuthenticationFailed
# from django.conf import settings
# from django.contrib.auth import get_user_model
from typing import Dict, Any
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import default_user_authentication_rule
from rest_framework_simplejwt.authentication import (
    JWTStatelessUserAuthentication,
    default_user_authentication_rule,
)
import logging

# from django.core.exceptions import ValidationError

logger = logging.getLogger(__name__)


# Prevent incorrect usage of Token.for_user #804
class CustomToken(Token):
    payload: Dict[str, Any]

    def __init__(self, token=None):
        super().__init__(token)

        # user_id = self.payload.get(settings.SIMPLE_JWT["USER_ID_CLAIM"], None)

        auth = JWTStatelessUserAuthentication()
        user = auth.get_user(validated_token=token)

        if not default_user_authentication_rule(user):
            return InvalidToken("token not valid because user is inactive")

        # try:
        #     user = get_user_model().objects.get(id=user_id)
        #     logger.info("user object", user)

        #     if not user.is_active:
        #         BlacklistedToken.objects.create(token=token)
        #         raise TokenError(("User is inactive"))
        # except:
        #     raise TokenError(("User is inactive"))

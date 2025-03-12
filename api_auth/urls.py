from django.urls import path, include
from api_auth.views import UserCreateView, MyTokenObtainPairView, LogOutView
from rest_framework.routers import DefaultRouter
from custom_simplejwt.views import CustomTokenRefreshView, CustomTokenVerifyView

router = DefaultRouter()
router.register(r"crud-user", UserCreateView, basename="crud-user")


urlpatterns = [
    # get the access token
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # provide user details with refresh token to get new access token
    path("token/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    # Logout endpoint
    path("logout/", LogOutView.as_view(), name="logout"),
    path(
        "get-api-user-id-for-user/",
        UserCreateView.as_view({"post": "get_api_user_id_for_user"}),
        name="get_api_user_id_for_user",
    ),
    # # Token is outstanding
    # path(
    #     "token/check-outstanding/",
    #     CheckOutstandingTokenView.as_view(),
    #     name="check_outstanding_token",
    # ),
] + [path("", include(router.urls))]

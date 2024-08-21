from django.urls import path, include
from paractice_module.views import EducationCreateAPIView


urlpatterns = [
    path(
        "api/education/create/",
        EducationCreateAPIView.as_view(),
        name="education-create",
    ),
]

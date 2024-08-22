from django.urls import path
from paractice_module.views import (
    EducationCreateAPIView,
    # EducationCreateAPIView_Schema_Field,
)


urlpatterns = [
    path(
        "api/education/create/extend-schema-serializer",
        EducationCreateAPIView.as_view(),
        name="education-create-extend-schema-serializer",
    ),
    # path(
    #     "api/education/create/extend-schema-field",
    #     EducationCreateAPIView_Schema_Field.as_view(),
    #     name="education-create-extend-schema-field",
    # ),
]

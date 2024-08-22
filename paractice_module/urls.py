from django.urls import path, include
from rest_framework import routers
from paractice_module.serializers import SkillAndSkillLevelSerializer_Paractice
from paractice_module.views import (
    EducationCreateAPIView,
    Skill_SkillLevel_CreateAPIView,
    # EducationCreateAPIView_Schema_Field,
)

router = routers.DefaultRouter()

# Define your example data
example = {"text": "Python Development", "skill_level": "Intermediate"}

# Register the viewset and pass the example for the serializer
router.register(
    r"skill-and-skill-level",
    Skill_SkillLevel_CreateAPIView,
    basename="skill-and-skill-level",
    Example={
        "requestBody": SkillAndSkillLevelSerializer_Paractice(example=example).data,
        "responses": {
            "201": SkillAndSkillLevelSerializer_Paractice(example=example).data
        },
    },
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
] + [path("", include(router.urls))]

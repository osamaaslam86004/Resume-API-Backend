from rest_framework import serializers

# from paractice_module.custom_fields import CustomDateField
# from datetime import datetime, timedelta
from drf_spectacular.utils import (
    # extend_schema_field,
    extend_schema_serializer,
    OpenApiExample,
    # OpenApiTypes,
)
from resume.models import Education


@extend_schema_serializer(
    exclude_fields=("id",),
    examples=[
        OpenApiExample(
            name="Example 1",
            summary="short summary",
            description="DateField can accept DD-MM-YYY, YYYY-MM-DD",
            value={
                "name": "eight",
                "location": "North Jon",
                "schoolurl": "https://www.stone-logan.com/",
                "education_start_date": {
                    "01-01-2020": True,
                    "2021-01-31": True,
                },
                "education_end_date": {
                    "01-01-2020": True,
                    "2021-01-31": True,
                },
                "degree": "degree",
                "description": "DateField can accept DD-MM-YYY, YYYY-MM-DD",
            },
            request_only=True,
            response_only=False,
        ),
    ],
)
class EducationSerializer_Paractice_Request(serializers.ModelSerializer):

    education_start_date = serializers.DateField(input_formats=["%d-%m-%Y", "%Y-%m-%d"])
    education_end_date = serializers.DateField(input_formats=["%d-%m-%Y", "%d-%m-%Y"])

    class Meta:
        model = Education
        fields = [
            "name",
            "location",
            "schoolurl",
            "education_start_date",
            "education_end_date",
            "degree",
            "description",
        ]

    def update(self, instance, validated_data):
        fields_to_update = [
            "name",
            "location",
            "schoolurl",
            "education_start_date",
            "education_end_date",
            "degree",
            "description",
        ]

        for field in fields_to_update:
            setattr(
                instance, field, validated_data.get(field, getattr(instance, field))
            )
            instance.save()

        return instance


class EducationSerializer_Paractice_Response(EducationSerializer_Paractice_Request):

    education_start_date = serializers.DateField(format="%Y-%m-%d")
    education_end_date = serializers.DateField(format="%Y-%m-%d")


# class EducationSerializer_Paractice_Field_Request(serializers.ModelSerializer):
#     # Use the custom date field with specific date formats
#     education_start_date_ = CustomDateField(
#         input_formats=["%d-%m-%Y", "%Y-%m-%d", "%m/%d/%Y"],
#         default=lambda: datetime.now().strftime("%d-%m-%Y"),
#     )
#     education_end_date_ = CustomDateField(
#         input_formats=["%d-%m-%Y", "%Y-%m-%d", "%m/%d/%Y"],
#         default=lambda: (datetime.now() + timedelta(days=7)).strftime("%d-%m-%Y"),
#     )

#     class Meta:
#         model = Education
#         fields = [
#             "name",
#             "location",
#             "schoolurl",
#             "education_start_date_",
#             "education_end_date_",
#             "degree",
#             "description",
#         ]

#     def update(self, instance, validated_data):
#         fields_to_update = [
#             "name",
#             "location",
#             "schoolurl",
#             "education_start_date",
#             "education_end_date",
#             "degree",
#             "description",
#         ]

#         for field in fields_to_update:
#             setattr(
#                 instance, field, validated_data.get(field, getattr(instance, field))
#             )
#             instance.save()

#         return instance


# class EducationSerializer_Paractice_Field_Response(
#     EducationSerializer_Paractice_Field_Request
# ):

#     education_start_date_ = serializers.DateField(format="%Y-%m-%d")
#     education_end_date_ = serializers.DateField(format="%Y-%m-%d")

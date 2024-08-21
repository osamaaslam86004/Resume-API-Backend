from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema_field,
    extend_schema_serializer,
    OpenApiExample,
    OpenApiTypes,
)
from resume.models import Education


# @extend_schema_serializer(
#     exclude_fields=("id",),
#     examples=[
#         OpenApiExample(
#             name="Example 1",
#             summary="short summary",
#             description="longer description",
#             value={
#                 "name": "eight",
#                 "location": "North Jon",
#                 "schoolurl": "https://www.stone-logan.com/",
#                 "education_start_date": {
#                     "01-01-2020": True,
#                     "2021-01-31": True,
#                 },
#                 "education_end_date": {
#                     "01-01-2020": True,
#                     "2021-01-31": True,
#                 },
#                 "degree": "degree",
#                 "description": "Onto production back. Response gun read child.",
#             },
#             request_only=True,
#             response_only=False,
#         ),
#     ],
# )
# class EducationSerializer_Paractice_Request(serializers.ModelSerializer):

#     education_start_date = serializers.DateField(input_formats=["%d-%m-%Y"])
#     education_end_date = serializers.DateField(input_formats=["%d-%m-%Y"])

#     class Meta:
#         model = Education
#         fields = [
#             "name",
#             "location",
#             "schoolurl",
#             "education_start_date",
#             "education_end_date",
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


# class EducationSerializer_Paractice_Response(EducationSerializer_Paractice_Request):

#     education_start_date = serializers.DateField(format="%Y-%m-%d")
#     education_end_date = serializers.DateField(format="%Y-%m-%d")


class EducationSerializer_Paractice_Field_Request(serializers.ModelSerializer):
    education_start_date = serializers.DateField(input_formats=["%d-%m-%Y"])
    education_end_date = serializers.DateField(input_formats=["%d-%m-%Y"])

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

    # Applying the examples in the schema using drf-spectacular
    @extend_schema_field(OpenApiTypes.DATE)
    def get_education_start_date(self, obj):
        return "DD-mm-YYYY"

    @extend_schema_field(OpenApiTypes.DATE)
    def get_education_end_date(self, obj):
        return "DD-mm-YYYY"


class EducationSerializer_Paractice_Field_Response(
    EducationSerializer_Paractice_Field_Request
):

    education_start_date = serializers.DateField(format="%Y-%m-%d")
    education_end_date = serializers.DateField(format="%Y-%m-%d")

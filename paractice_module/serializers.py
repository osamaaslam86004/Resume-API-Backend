from rest_framework import serializers
from drf_spectacular.utils import (
    extend_schema_field,
    OpenApiExample,
    extend_schema_serializer,
)
from resume.models import Education


@extend_schema_serializer(
    exclude_fields=("id",),
    examples=[
        OpenApiExample(
            name="Example 1",
            summary="short summary",
            description="longer description",
            value={
                "name": {"eight": True},
                "location": {"North Jon": True},
                "schoolurl": {"https://www.stone-logan.com/": True},
                "education_start_date": {
                    "01-01-2020": True,
                    "2021-01-31": True,
                },
                "education_end_date": {
                    "01-01-2020": True,
                    "2021-01-31": True,
                },
                "degree": {"degree": True},
                "description": {"Onto production back. Response gun read child.": True},
            },
            request_only=True,
            response_only=False,
        ),
    ],
)
class EducationSerializer_Paractice(serializers.ModelSerializer):

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

    # @extend_schema_field(OpenApiTypes.DATE)
    # def get_job_start_date(self, obj):
    #     return "DD-mm-YYYY"
    #     return obj.job_start_date.strftime("%d-%m-%Y") if obj.job_start_date else None

    # @extend_schema_field(OpenApiTypes.DATE)
    # def get_job_end_date(self, obj):
    #     return "DD-mm-YYYY"
    #     return obj.job_end_date.strftime("%d-%m-%Y") if obj.job_end_date else None

    # @extend_schema_field(OpenApiTypes.DATE)
    # def get_education_start_date(self, obj):
    #     return "DD-mm-YYYY"
    # return (
    #     obj.education_start_date.strftime("%d-%m-%Y")
    #     if obj.education_start_date
    #     else None
    # )

    # @extend_schema_field(OpenApiTypes.DATE)
    # def get_education_end_date(self, obj):
    #     return "DD-mm-YYYY"
    # return (
    #     obj.education_end_date.strftime("%d-%m-%Y")
    #     if obj.education_end_date
    #     else None
    # )

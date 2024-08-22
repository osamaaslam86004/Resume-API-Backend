from rest_framework import serializers
from drf_spectacular.utils import OpenApiTypes, extend_schema_field


class CustomDateField(serializers.DateField):
    @extend_schema_field(OpenApiTypes.STR)
    def to_representation(self, value):
        # You can specify the custom date format here, e.g., '%d-%m-%Y'
        return value.strftime("%d-%m-%Y")

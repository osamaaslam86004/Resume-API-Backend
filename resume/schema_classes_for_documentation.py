from drf_spectacular.utils import extend_schema_field, OpenApiTypes
from rest_framework import serializers
from rest_framework.fields import DateField


@extend_schema_field(OpenApiTypes.DATE)
class CustomDateField(DateField):
    pass

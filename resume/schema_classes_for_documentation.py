from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.fields import DateField


@extend_schema_field(
    serializers.DateField(format="%Y-%m-%d", input_formats=["%d-%m-%Y", "%Y-%m-%d"])
)
class CustomDateField(DateField):
    pass

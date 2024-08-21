from rest_framework import serializers
from resume_api.custom_user_rated_throtle_class import CustomAnonRateThrottle
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from paractice_module.serializers import (
    # EducationSerializer_Paractice_Request,
    # EducationSerializer_Paractice_Response,
    EducationSerializer_Paractice_Field_Request,
    EducationSerializer_Paractice_Field_Response,
)


# @extend_schema(
#     request=EducationSerializer_Paractice_Request,
#     responses={"201": EducationSerializer_Paractice_Response},
#     methods=["POST"],
# )
# class EducationCreateAPIView(APIView):
#     """
#     API view to create a new Education entry.
#     Paractice of @extend_schema_serializer decorator
#     """

#     parser_classes = [JSONParser]
#     renderer_classes = [JSONRenderer]
#     throttle_classes = [CustomAnonRateThrottle]
#     http_method_names = ["post", "options"]

#     def post(self, request, format=None):
#         serializer = EducationSerializer_Paractice_Request(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def finalize_response(self, request, response, *args, **kwargs):
#         response = super().finalize_response(request, response, *args, **kwargs)

#         response["X-RateLimit-Limit"] = request.rate_limit["X-RateLimit-Limit"]
#         response["X-RateLimit-Remaining"] = request.rate_limit["X-RateLimit-Remaining"]
#         return response


@extend_schema(
    request=EducationSerializer_Paractice_Field_Request,
    responses={"201": EducationSerializer_Paractice_Field_Response},
    methods=["POST"],
)
class EducationCreateAPIView_Schema_Field(APIView):
    """
    API view to create a new Education entry.
    Paractice of @extend_schema_field decorator
    """

    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]
    throttle_classes = [CustomAnonRateThrottle]
    http_method_names = ["post", "options"]

    def post(self, request, format=None):
        serializer = EducationSerializer_Paractice_Field_Request(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        response["X-RateLimit-Limit"] = request.rate_limit["X-RateLimit-Limit"]
        response["X-RateLimit-Remaining"] = request.rate_limit["X-RateLimit-Remaining"]
        return response

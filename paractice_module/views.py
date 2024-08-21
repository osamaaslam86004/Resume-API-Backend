from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from paractice_module.serializers import (
    EducationSerializer_Paractice_Request,
    EducationSerializer_Paractice_Response,
)


@extend_schema(
    request=EducationSerializer_Paractice_Request,
    responses={"201": EducationSerializer_Paractice_Response},
    methods=["POST"],
)
class EducationCreateAPIView(APIView):
    """
    API view to create a new Education entry.
    """

    # permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]
    renderer_classes = [JSONRenderer]

    def post(self, request, format=None):
        serializer = EducationSerializer_Paractice_Request(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

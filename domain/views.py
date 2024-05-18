from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from domain.serializers import RequestsCatcherSerializer
from domain.utils import send_info


class RequestsCatcherView(generics.GenericAPIView):
    serializer_class = RequestsCatcherSerializer

    @send_info
    def get(*args, **kwargs):
        return Response({"message": "GET request"})

    @send_info
    def post(*args, **kwargs):
        return Response({"message": "POST request"})

    @send_info
    def put(*args, **kwargs):
        print("PUT request")
        return Response({"message": "PUT request"})

    @send_info
    def patch(*args, **kwargs):
        print("PATCH request")
        return Response({"message": "PATCH request"})

    @send_info
    def delete(*args, **kwargs):
        print("DELETE request")
        return Response({"message": "DELETE request"})

    @send_info
    def head(*args, **kwargs):
        print("HEAD request")
        return Response({"message": "HEAD request"})

    @send_info
    def options(*args, **kwargs):
        print("OPTIONS request")
        return Response({"message": "OPTIONS request"})

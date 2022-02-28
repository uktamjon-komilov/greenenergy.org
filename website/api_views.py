from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from website.serializers import FeedbackSerializer


class FeedbackApiView(APIView):
    serializer_class = FeedbackSerializer

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

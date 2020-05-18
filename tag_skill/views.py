# Create your views here.
from rest_framework.views import APIView
from tag_skill.services.process_handler import handlerClass
from rest_framework.response import Response


class PreprocessingText(APIView):

    def post(self, request):
        response_from_backend = request.data
        input_data = response_from_backend['input_string']
        obj = handlerClass()
        mapped_tags = obj.processHandler(input_data)
        print(mapped_tags)
        return Response(mapped_tags, status=200)

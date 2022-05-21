from django.http import JsonResponse, FileResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from .services.WordCloudService import WordCloudService
from .services.TextSummaryService import TextSummaryService
from .services.TextSimilarityService import TextSimilarityService
from .services import FileService


class WordCloudView(APIView):
    parser_class = (FileUploadParser,)
    parser_class = (FileUploadParser,)

    def get(self, request, *args, **kwargs):
        text = request.GET.get('inputText')
        service = WordCloudService(text)
        file_obj = service.generate_word_cloud()
        response = FileResponse(file_obj)
        return response

    def post(self, request, *args, **kwargs):
        file_data = request.data['file']
        text = FileService.get_data_from_file(file_data)
        service = WordCloudService(text)
        file_obj = service.generate_word_cloud()
        response = FileResponse(file_obj)
        return response


class TextSummaryView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_data = request.data['file']
        text = FileService.get_data_from_file(file_data)
        service = TextSummaryService(text)
        summary = service.get_text_summary()

        return JsonResponse({'result': summary})

    def get(self, request, *args, **kwargs):
        text = request.GET.get('inputText')
        service = TextSummaryService(text)
        summary = service.get_text_summary()

        return JsonResponse({'result': summary})


class TextSimilarityView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        first_file = request.data['firstFile']
        second_file = request.data['secondFile']
        first_input_text = FileService.get_data_from_file(first_file)
        second_input_text = FileService.get_data_from_file(second_file)
        service = TextSimilarityService(first_input_text, second_input_text)
        similarity = service.calculate_similarity()
        return JsonResponse({'result': similarity})

    def get(self, request, *args, **kwargs):
        first_input_text = request.GET.get("firstInputText")
        second_input_text = request.GET.get("secondInputText")
        service = TextSimilarityService(first_input_text, second_input_text)
        similarity = service.calculate_similarity()
        return JsonResponse({'result': similarity})

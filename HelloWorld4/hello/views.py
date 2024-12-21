from django.http import JsonResponse, StreamingHttpResponse, FileResponse, HttpResponse
import os

# HttpResponse Examples
def plain_text_response(request):
    return HttpResponse("This is plain text.")

def json_response(request):
    return JsonResponse({"message": "Hello, JSON!"})

def file_response(request):
    file_path = os.path.join('path_to_file', 'example.txt')
    return FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')

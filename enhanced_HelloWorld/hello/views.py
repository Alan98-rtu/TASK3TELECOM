# hello/views.py

from django.http import HttpResponse

def enhanced_hello_world(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Enhanced Hello World</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: green; }
        </style>
    </head>
    <body>
        <h1>Enhanced Hello, World!</h1>
        <p>This is an enhanced version of the Hello World page.</p>
    </body>
    </html>
    """
    return HttpResponse(html)

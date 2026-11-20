from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from pathlib import Path

def book_cover(request):
    file_path = (
        Path(__file__).parent
        / "static"
        / "templates"
        / "book_cover.html"
    )

    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    return HttpResponse(html_content)
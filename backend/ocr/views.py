from django.shortcuts import render
from PIL import Image
import pytesseract
import numpy as np

# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def logout(request):
    pass


def ocr_view(request):
    pass


# this is funtion that takes in the pdf file and returns the paragraphs of text in the pdf
def text_extraction(request):
    pass

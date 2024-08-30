from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from .forms import WordForm
import os

def preview_word(request):
    form = WordForm()
    word = request.GET.get('word', '')

    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']

    # Path to the fonts directory
    fonts_dir = os.path.join(settings.BASE_DIR, 'static/fonts')

    # Load all TTF font files from the directory
    font_files = [
        f for f in os.listdir(fonts_dir)
        if f.endswith('.ttf')
    ]

    # Collect font data including paths for preview and download
    font_data = []
    for font_file in font_files:
        font_path = os.path.join(fonts_dir, font_file)
        font_name = os.path.splitext(font_file)[0]
        font_data.append({
            'name': font_name,
            'file': font_file,
            'url': os.path.join('/static/fonts/', font_file)
        })

    # Set up pagination (10 fonts per page)
    paginator = Paginator(font_data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'preview/preview.html', {
        'form': form,
        'word': word,
        'page_obj': page_obj,
        'is_paginated': True
    })

import os
from fontTools.ttLib import TTFont

def convert_to_woff_and_woff2(font_path):
    base_name = os.path.splitext(font_path)[0]
    woff_path = f'{base_name}.woff'
    woff2_path = f'{base_name}.woff2'

    # Convert to WOFF
    font = TTFont(font_path)
    font.flavor = 'woff'
    font.save(woff_path)

    # Convert to WOFF2
    font.flavor = 'woff2'
    font.save(woff2_path)

    return woff_path, woff2_path

from PIL import Image
from cairosvg import svg2png
from io import BytesIO
import os

def svg_to_ico(svg_path, ico_path):
    # Dimensioni standard per le icone Windows
    sizes = [(16, 16), (32, 32), (48, 48)]
    images = []
    
    # Converti SVG in PNG per ogni dimensione
    for size in sizes:
        png_data = svg2png(url=svg_path, output_width=size[0], output_height=size[1])
        img = Image.open(BytesIO(png_data))
        images.append(img)
    
    # Salva come ICO
    images[0].save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images], append_images=images[1:])

# Percorsi dei file
src_path = os.path.join('src', 'assets', 'icon.svg')
dst_path = os.path.join('src', 'assets', 'icon.ico')

# Converti l'icona
src_path = os.path.abspath(src_path)
dst_path = os.path.abspath(dst_path)
print(f'Converting {src_path} to {dst_path}')
print('This may take a few seconds...')
print('Please wait...')

try:
    svg_to_ico(src_path, dst_path)
    print('Conversion completed successfully!')
except Exception as e:
    print(f'Error during conversion: {e}')
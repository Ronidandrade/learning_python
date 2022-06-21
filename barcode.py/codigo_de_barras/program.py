from barcode import EAN13;
from barcode.writer import ImageWriter;

with open("codigo_de_barras.png", 'wb') as f:
    EAN13('123456789102', writer = ImageWriter()).write(f);

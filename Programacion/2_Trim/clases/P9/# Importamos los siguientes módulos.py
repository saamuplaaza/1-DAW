# Importamos los siguientes módulos
import qrcode

# Creamos una instancia del QR con la versión (tamaño), la corrección de errores, el box_size (pixeles x casilla) y el border.
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=5)

# Pedimos la url a la que queremos que lleve el QR y añadimos los datos al objeto qr
data = input("Inserta la url a la que quieres que lleve el código QR: ")
qr.add_data(data)

# Aseguramos que se utilice toda la dimensión del código QR 
qr.make(fit=True)

# Convertimos el QR en un archivo de imagen y le damos los parámetros de color de relleno y color de fondo
img = qr.make_image(fill_color="black", back_color="white")

# Guardamos la imagen con el nombre que queramos
img.save("qrcode.png")
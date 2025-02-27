import base64

from io import BytesIO

def convert_bytesio_to_base64(file_bytes: BytesIO) -> bytes:
    file_bytes.seek(0)

    image_base64 = base64.b64encode(file_bytes.read())
    return image_base64
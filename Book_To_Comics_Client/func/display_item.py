from dataclasses import dataclass
from PIL.Image import Image


class ImageBoxItem:
    index: int
    image: Image
    image_url: str
    prompt: str

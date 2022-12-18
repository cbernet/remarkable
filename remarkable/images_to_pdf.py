import pathlib
from PIL import Image
from typing import List, Iterable


def image_files_to_pdf(image_files: List[pathlib.Path], pdf_file: str):
    """Create a pdf file from a list of images"""
    images = [Image.open(image_file) for image_file in image_files]
    first_image = images[0]
    append_images = images[1:]
    first_image.save(
        pdf_file, resolution=100.0, save_all=True, append_images=append_images
    )


def list_images(directory: pathlib.Path) -> List[pathlib.Path]:
    """Build list of images from directory, ordered by name"""
    images = list(directory.glob("*.png"))
    images = sorted(images, key=lambda x: x.name)
    return images

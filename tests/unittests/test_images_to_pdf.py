import pytest
from remarkable.images_to_pdf import *
from remarkable.locate import abspath_data


@pytest.fixture
def image_dir():
    return abspath_data("lambdas")


@pytest.fixture
def output_pdf(image_dir):
    pdf_file = image_dir.with_suffix(".pdf")
    yield pdf_file
    pdf_file.unlink(missing_ok=True)


def test_list_images(image_dir):
    images = list_images(image_dir)
    assert len(images) == 2


def test_image_files_to_pdf(image_dir, output_pdf):
    images = list(list_images(image_dir))
    image_files_to_pdf(images, output_pdf)

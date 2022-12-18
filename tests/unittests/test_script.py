import pytest
from remarkable.script import main
from remarkable.locate import abspath_data


@pytest.fixture
def image_dir():
    return abspath_data("lambdas")


@pytest.fixture
def output_pdf(image_dir):
    pdf_file = image_dir.with_suffix(".pdf")
    yield pdf_file
    pdf_file.unlink(missing_ok=True)


def test_script(image_dir, output_pdf):
    main([image_dir.as_posix()])

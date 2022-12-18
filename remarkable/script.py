import argparse
import pathlib
import shutil
import sys
import tempfile
from typing import List
from remarkable.images_to_pdf import list_images, image_files_to_pdf


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert remarkable output dir to pdf")
    parser.add_argument("folder", type=pathlib.Path, help="Remarkable output folder")
    parser.add_argument(
        "-o", dest="output", type=pathlib.Path, default=None, help="output folder"
    )
    args = parser.parse_args(args)
    return args


def main(args=None):
    if not args:
        args = sys.argv[1:]
    args = parse_args(args)

    folder = args.folder

    images = list_images(args.folder)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_pdf = pathlib.Path(tmpdir) / "out.pdf"
        image_files_to_pdf(images, tmp_pdf)
        output_pdf = folder.with_suffix(".pdf")
        if args.output:
            output_pdf = args.output / output_pdf.name
        shutil.move(tmp_pdf, output_pdf)


if __name__ == "__main__":
    main()

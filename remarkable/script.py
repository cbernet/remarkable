import argparse
import pathlib
import sys
from typing import List
from remarkable.images_to_pdf import list_images, image_files_to_pdf


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert remarkable output dir to pdf")
    parser.add_argument("folder", type=pathlib.Path, help="Remarkable output folder")
    args = parser.parse_args(args)
    return args


def main(args=None):
    if not args:
        args = sys.argv[1:]
    args = parse_args(args)

    folder = args.folder
    images = list_images(args.folder)
    output_pdf = folder.with_suffix(".pdf")

    image_files_to_pdf(images, output_pdf)


if __name__ == "__main__":
    main()

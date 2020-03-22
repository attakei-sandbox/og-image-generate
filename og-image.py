#!/usr/bin/env python
import argparse
from PIL import Image, ImageDraw


IMAGE_SIZE = (1200, 630)
IMAGE_BG = (255, 255, 255, 255)
LOGO_POS = (65, 65)
LOGO_SIZE = (500, 500)

parser = argparse.ArgumentParser()
parser.add_argument("logo", help="Logo image file path")
parser.add_argument("source", help="Source URL")
parser.add_argument("-o", "--out", help="Output path")


def main(args: argparse.Namespace):
    image = Image.new(mode="RGB", size=IMAGE_SIZE)
    # Inject background
    bg = ImageDraw.Draw(image)
    bg.rectangle(((0, 0), IMAGE_SIZE), fill=IMAGE_BG)
    # Past logo image
    logo = Image.open(args.logo).resize(LOGO_SIZE)
    image.paste(logo, LOGO_POS)
    # Saving image
    image.save(args.out)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

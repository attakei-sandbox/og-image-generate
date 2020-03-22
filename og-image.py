#!/usr/bin/env python
import argparse
from PIL import Image, ImageDraw


IMAGE_SIZE = (1200, 630)
IMAGE_BG = (255, 255, 255, 255)


parser = argparse.ArgumentParser()
parser.add_argument("source", help="Source URL")
parser.add_argument("-o", "--out", help="Output path")


def main(args: argparse.Namespace):
    image = Image.new(mode="RGB", size=IMAGE_SIZE)
    bg = ImageDraw.Draw(image)
    bg.rectangle(((0, 0), IMAGE_SIZE), fill=IMAGE_BG)
    image.save(args.out)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)

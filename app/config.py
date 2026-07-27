from os import path

BASE_DIR = path.abspath(path.dirname(path.dirname(__file__)))

ALLOWED_FORMATS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".tif",
    ".webp",
    ".svg",
    ".ico",
    ".heic",
    ".heif",
    ".avif",
    ".raw",
    ".cr2",    # Canon RAW
    ".nef",    # Nikon RAW
    ".arw",    # Sony RAW
    ".dng",    # Adobe Digital Negative
    ".orf",    # Olympus RAW
    ".rw2",    # Panasonic RAW
    ".raf",    # Fujifilm RAW
    ".sr2",    # Sony RAW (older)
    ".psd",    # Adobe Photoshop
    ".xcf",    # GIMP
    ".eps",
    ".ai",
    ".pdf",    # Can contain images
    ".jp2",    # JPEG 2000
    ".j2k",
    ".pbm",
    ".pgm",
    ".ppm",
    ".pnm",
    ".dds",
    ".tga",
    ".icns",
    ".exr",
    ".hdr"
]

from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

# This function returns DateTimeOriginal, DateTimeDigitized or DateTime if it can find it in the exif data
def get_exif_date_time(filename):
    info = Image.open(filename)._getexif()
    if info is not None:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'DateTimeOriginal':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
            elif tag_name == 'DateTimeDigitized':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
            elif tag_name == 'DateTime':
                return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
    return None


def get_exif_gps_data(filename):
    info = Image.open(filename)._getexif()
    gps_data = list()
    if info is not None:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            if str(tag_name).upper().startswith('GPS'):
                gps_data.append((tag_name, value))
        return gps_data
    return None


# TODO: This function deletes the exif data in the file because Pillow cannot preserve it (I believe)
# This is acceptable for our use case, allthough not great, as long as we only perform this AFTER we check for DateTime and GPS info..
def fix_orientation(filename):
    image = Image.open(filename)
    info = image._getexif()
    if info is not None:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == 'Orientation':
                print (value)
                if value == 3:
                    image=image.rotate(180, expand=True)
                elif value == 6:
                    image=image.rotate(270, expand=True)
                elif value == 8:
                    image=image.rotate(90, expand=True)
                image.save(filename)
                image.close()
    return None
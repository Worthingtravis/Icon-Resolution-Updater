import sys
from PIL import Image

# a provided image will inherit the name and resolution of every image of a given directory, and saved into a
# specific directory.


if __name__ == '__main__':
  input_img = sys.argv[1]
  export_dir = sys.argv[2]
  base_dir = sys.argv[3:]

  for image_to_change in base_dir:
    try:

      with Image.open(image_to_change) as im:
        (width, height) = (im.width, im.height)
        name = image_to_change.rsplit(sep='/', maxsplit=1)[1]
        with Image.open(input_img) as open_input_img:
          resized_img = open_input_img.resize((width, height), Image.ANTIALIAS)
          resized_img.save(export_dir + '/' + name)
          print(name, width, height, im)
    except OSError:
      pass


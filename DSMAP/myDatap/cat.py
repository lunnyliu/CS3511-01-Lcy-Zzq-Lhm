import os
import glob
from PIL import Image

imageA_dir = './trainA/'
imageB_dir = './trainB/'

imageA_files = glob.glob(os.path.join(imageA_dir, '*.jpg'))
imageB_files = glob.glob(os.path.join(imageB_dir, '*.jpg'))
 
imageAs = []
for image_file in imageA_files:
    image = Image.open(image_file)
    imageAs.append(image)
imageBs = []
for image_file in imageB_files:
    image = Image.open(image_file)
    imageBs.append(image)

for i in range(len(imageAs)):
    new_image = Image.new('RGB', (2048, 1024), 'white')

    new_image.paste(imageAs[i], (0, 0))
    new_image.paste(imageBs[i], (1024, 0))
    new_image.save(str(i)+'.jpg')
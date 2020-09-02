# 파일 크기 줄이기
import os
from PIL import Image

current_path = os.path.abspath(os.curdir)
print(current_path)

train_path = current_path + '/train_classification/';
test_path = current_path + '/test_classification/';

def size_down(image_path) :
  im = Image.open(image_path)

  # resize 이미지
  size = (224, 224)
  im.thumbnail(size, Image.ANTIALIAS)  
  im.save(image_path)
  print(image_path)


# train folder
os.chdir(train_path)
for current_dir, dirs, files in os.walk('.'):
  for f in files:
    if f.endswith('.jpg'):
      image_path = train_path + current_dir.lstrip('.\\')  +'/' + f
      size_down(image_path)

# test folder
os.chdir(test_path)
for current_dir, dirs, files in os.walk('.'):
  for f in files:
    if f.endswith('.jpg'):
      image_path = test_path + current_dir.lstrip('.\\')  +'/' + f
      size_down(image_path)


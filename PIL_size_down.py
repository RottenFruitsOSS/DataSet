# 파일 크기 줄이기
import os
from PIL import Image

current_path = os.path.abspath(os.curdir)
print(current_path)

train_path = current_path + '/train_classification/';
test_path = current_path + '/test_classification/';

new_train_path = current_path + '/train_224/';
new_test_path = current_path + '/test_224/';

def size_down(image_path, new_path) :
  im = Image.open(image_path)

  # resize 이미지
  size = (224, 224)
  im.thumbnail(size, Image.ANTIALIAS)  
  im.save(image_path)
  print(image_path)


# train에 있는 파일 이름 변경
'''
os.chdir(train_path)
for current_dir, dirs, files in os.walk('.'):
  for f in files:
    if f.endswith('.jpg'):
      image_path = train_path + current_dir.lstrip('.\\')  +'/' + f
      new_path = new_train_path + current_dir.lstrip('.\\')  +'/' + f
      size_down(image_path, new_path)
'''
# test에 있는 파일 이름 변경
os.chdir(test_path)
for current_dir, dirs, files in os.walk('.'):
  for f in files:
    if f.endswith('.jpg'):
      image_path = test_path + current_dir.lstrip('.\\')  +'/' + f
      new_path = new_test_path + current_dir.lstrip('.\\')  +'/' + f
      size_down(image_path, new_path)


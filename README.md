# Custom DataSet
- custom data를 만들어 이미지 데이터를 저장함. 
- 파일 사이즈를 줄이고 압축하여 notebook에서 쉽게 불러와 데이터를 사용할 수 있게함. 

# DatsSet tree구조
```
1. Yolo dataset
├── train
│   ├── damage
│   ├── normal
│   ├── spoiled_early
│   └── spoiled_advanced
└── test
    ├── damage
    ├── normal
    ├── spoiled_early
    └── spoiled_advanced

2. Classification dataset
├── train_classification
│   ├── normal (275)
│   ├── spoiled_early (275)
│   └── spoiled_advanced (275)
└── test_classification
    ├── normal (20)
    ├── spoiled_early (20)
    └── spoiled_advanced (20)
```

Classification dataset를 사용하여 image-classification 진행.

모델 학습: https://github.com/RottenFruitsOSS/image-classification

# 파일 사이즈 줄이기
## 1. 설치 
```
pip3 install pillow
```
## 2. 파일 다운로드
[PIL_size_down.py](https://github.com/RottenFruitsOSS/DataSet/blob/master/PIL_size_down.py)
### PIL_size_down.py 수정
- train_path, test_path 알맞게 수정
```
train_path = current_path + '/train_classification/';
test_path = current_path + '/test_classification/';
```
- 줄일 파일 사이즈 설정
```
size = (224, 224)
```

### 압축하고자 하는 train, test 폴더와 같은 위치에 PIL_size_down.py 위치
```
train_classification/
test_classification/
PIL_size_down.py
```


## 3. 실행
```
python PIL_size_down.py
```





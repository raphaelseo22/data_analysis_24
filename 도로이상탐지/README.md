# 도로 이상 탐지 프로젝트

## 프로젝트 개요
도로의 균열을 자동으로 탐지하는 시스템을 개발하였습니다. 두 가지 접근 방식을 시도하여 성능을 비교하였습니다:

1. 이미지 특징 추출 기반 접근법 (LBP & GLCM)
2. 딥러닝 기반 접근법 (Autoencoder)

## 기술 스택
- Python
- OpenCV
- scikit-learn
- TensorFlow/Keras
- NumPy
- Matplotlib

## 방법론 및 결과

### 1. 이미지 특징 추출 기반 접근법

#### 사용된 특징
- LBP (Local Binary Pattern) 통계값
  - 엔트로피
  - 평균
  - 중앙값
  - 표준편차

- GLCM (Gray Level Co-occurrence Matrix) 특성
  - 동질성 (Homogeneity)
  - 균일성 (Energy)
  - 비유사성 (Dissimilarity)
  - 대비 (Contrast)
  - 상관성 (Correlation)

#### 모델
- RandomForest 분류기 사용 (n_estimators=10)

#### 결과
- GLCM 모든 특성의 표준편차를 활용했을 때 최고 성능 달성
- F1 Score: 0.9
- 특성 중요도 순위:
  1. 동질성
  2. 균일성
  3. 비유사성
  4. 대비
  5. 상관성

### 2. Autoencoder 기반 접근법

#### 모델 구조
- Encoder: Conv2D + MaxPooling2D 층 3개
- Decoder: Conv2D + UpSampling2D 층 3개
- 입력/출력 크기: 360x240x1

#### 이상 탐지 방법
- 정상 이미지로만 학습
- 재구성 오차의 95퍼센타일을 임계값으로 설정
- 임계값 초과 시 균열로 판단

#### 결과
- F1 Score: 0.91

## 결론
두 접근법 모두 우수한 성능을 보였으며, 특히:
- 특징 추출 기반: F1 Score 0.90
- Autoencoder 기반: F1 Score 0.91

Autoencoder가 약간 더 높은 성능을 보였으나, 특징 추출 기반 방식도 비슷한 수준의 성능을 달성했습니다. 특징 추출 기반 방식은 해석 가능성이 높다는 장점이 있어, 실제 적용 시 상황에 따라 적절한 방식을 선택할 수 있습니다.

## 관련 파일
- [autoencoder.ipynb](autoencoder.ipynb): autoencoder 활용 상세 분석 코드 및 결과
- [lbp_glcm.ipynb](lbp_glcm.ipynb): lbp & glcm 활용 상세 분석 코드 및 결과

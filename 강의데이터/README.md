# 강의 데이터 분석 프로젝트

## 프로젝트 개요
- 강의 플랫폼의 주문, 강의, 고객, 환불, 사용자 데이터를 분석하여 비즈니스 인사이트 도출
- 데이터 기간: 2022년 1월 ~ 12월
- 분석 도구: Python (Pandas, Seaborn)

## 데이터셋 구성
- order: 주문 데이터 (284,035건)
- course: 강의 데이터 
- customer: 고객 데이터
- refund: 환불 데이터
- user: 사용자 데이터

## 주요 분석 내용

### 1. 매출 트렌드 분석
- 2022년 월별 매출액 추이 분석
- 비과세 매출액 기준으로 트렌드 파악

### 2. 고객 행동 분석
- 월별 회원가입 추이 분석
- 회원 이탈률 분석
  - 계정 생성부터 마지막 로그인까지 평균 154일 소요

### 3. 환불 패턴 분석
- 월별 환불 금액 추이 분석
- 환불 발생 패턴 파악

## 주요 발견점
1. 회원가입과 매출은 특정 시기에 증가하는 계절성을 보임
2. 환불 금액은 매출 증가 시기와 연관성을 보임
3. 고객 유지 기간이 약 5개월로, 장기 고객 확보 전략 필요

## 제언
1. 회원 이탈 방지를 위한 고객 인게이지먼트 강화 필요
2. 성수기/비수기 매출 격차 완화를 위한 프로모션 전략 수립
3. 환불율 감소를 위한 강의 품질 관리 및 고객 만족도 제고


## 관련 파일
- [강의데이터_분석.ipynb](강의데이터_분석.ipynb): 상세 분석 코드 및 결과

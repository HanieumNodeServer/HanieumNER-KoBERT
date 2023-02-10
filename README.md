# 인공지능(AI)기반 챗봇 주문·예약·예매 시스템, 불러부릉



![image](https://user-images.githubusercontent.com/79521972/215462121-739c08cf-af88-4ee9-b549-b6849c35b1bc.png)


### <br/>
  
  
##   AI 챗봇 알고리즘
### NER 알고리즘
- 미리 정의한 인물명, 장소면, 기관명 등과 같은 **개체명**을 입력 텍스트에 **태깅**하는 NLP 기술
- 텍스트로 변환된 사용자의 발화에서 예매에 필요한 주요 키워드(출발지, 도착지, 날짜 등) 추출
- NER은 문장을 토큰 단위로 나누고, 이 토큰들을 각각 태깅하여 개체명인지 아닌지를
분간할 수 있어 사용자에게 맞춤형 번역을 제공할 수 있도록 도와줌



<img src = "https://user-images.githubusercontent.com/77714083/217755352-3b43900e-8737-4b51-9538-503cabba88ad.png">

### <br/>

## 학습 모델
### KoBERT

- 구글에서 공개한 위키피디아(25억 단어), BooksCorpus(8억 단어)와 같은 레이블 없는 텍스트 데이터로 사전 학습된 모델
- 특정 작업(문서 분류, 번역, 질의 응답)을 위해 **pre-training된 모델**에 **신경망을 추가하여 미세 조정(fine-tuning)** = *"Transfer-Learning"*
- SKTBrain에서 공개한 한국어 문장을 학습한 한국어 BERT인 **KoBERT** 모델 사용

### 학습 흐름도
![image](https://user-images.githubusercontent.com/77714083/217759721-84818334-381c-4e6b-ab70-50ebdbe07a0b.png)




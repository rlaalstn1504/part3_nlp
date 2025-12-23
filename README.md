# 코드잇 KDT PART-3 강의자료

본 저장소는 **코드잇 KDT 강의자료**를 보관·관리하기 위한 공간입니다.  
자료는 **코드잇 내부 전용**이며, **외부 유출을 엄격히 금지합니다.**

---

## 코드 테스트 환경

본 강의자료는 아래 환경에서 테스트되었습니다.

- **OS:** Ubuntu  
- **Python:** 3.10  
- **Frameworks:** PyTorch, Hugging Face Transformers 등

라이브러리 버전에 따라 실행 결과나 구현 방식에 차이가 발생할 수 있습니다.  
**`requirements.txt` 파일을 먼저 설치한 뒤**, 각 실습 파일의 `import` 실행 여부를 확인하는 것을 권장드립니다.

---

## 대부분 GPU 없이도 실행 가능
본 강의는 다양한 수강 환경을 고려해, CPU만으로도 충분히 실습 가능한 모델들을 중심으로 구성했습니다.
로컬 실습 구간에서는 고전적 Seq2Seq 모델부터 Transformer 기반 모델까지 직접 다뤄보며,
"모델 구조를 이해하고 직접 돌려보는 경험"에 초점을 둡니다.

이 과정에서 LLM 파트에는 Google의 **gemma-3-270m-it** 모델을 활용합니다.
Gemma-3는 약 2억 7천만 개 파라미터를 가진 경량 LLM으로,

- Transformer 기반 LLM의 구조적 특징은 그대로 유지하면서,
- GPU 없이도 CPU에서 실행 가능한 실제 LLM 경험을 제공합니다.

즉, 너무 무겁지 않으면서도
"LLM이 어떻게 작동하는지 로컬에서 직접 체감할 수 있는 최적의 모델"이라는 점이 가장 큰 선택 이유입니다. 

- 모델 페이지: https://huggingface.co/google/gemma-3-270m-it  
- Instruction-Tuned(IT) 버전은 지시문 수행에 최적화된 모델입니다.  
---

## Gemma-3 라이선스 및 접근 권한

Gemma 모델은 Google DeepMind에서 제공하며, Hugging Face에서 사용하기 위해서는 **Google의 사용 라이선스에 동의**해야 합니다.  
Hugging Face 계정에 로그인한 후 모델 페이지에서 라이선스에 동의해야 다운로드 및 액세스가 가능합니다. :contentReference[oaicite:4]{index=4}

1. Hugging Face 계정 생성 (https://huggingface.co)  
2. https://huggingface.co/google/gemma-3-270m-it 접속  
3. Google 사용 라이선스 검토 및 **동의(Accept)**  
4. `.env` 파일에 Hugging Face Access Token 저장

```env
HF_TOKEN=your_huggingface_access_token_here
```

---

## 실행 관련 주의사항

- gemma 계열의 모델은 라이선스에 동의하지 않으면 모델 파일 다운로드나 추론 코드 실행이 불가합니다. 
- 실행 환경에 .env 파일을 만들고 HF_TOKEN, API_KEY 등을 저장하고 사용하셔야 합니다. 

---

## 문의

자료 관련 문의는 아래 연락처로 부탁드립니다.

- **강사:** 김민수  
- **이메일:** rlaalstn1504@naver.com

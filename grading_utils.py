from langchain_core.prompts import ChatPromptTemplate # LLM에 전달할 메시지를 템플릿 형태로 구성하기 위한 모듈
from langchain_core.output_parsers import StrOutputParser # LLM의 응답 중 문자열만 깔끔히 추출해주는 파서
from langchain_openai import ChatOpenAI # OpenAI의 챗 모델(GPT-4, GPT-4o 등)을 사용하는 모듈

# 정답 리스트 (총 20개)
answer_key = [
    "오피스 잔혹 동화: 신입 사원 민수",
    "본사 지하 전산실",
    "AI 인턴 하나를 코딩해 달라는 요청",
    "모놀리식(Monolithic) 구조",
    "오래 유지보수할 수 있는 구조여야 함",
    "부서 B-612",
    "회의실 하나보다도 작은 규모의 TF 조직",
    "초기에 정리하지 않으면 시스템 전체를 망가뜨리는 위험 요소",
    "칼퇴",
    "극심한 번아웃 상태를 비유적으로 표현한 것",
    "핵심 프로젝트",
    "기능이 단순하지만 민수에게 의미 있는 프로젝트",
    "실행 중인 프로세스들과 레거시 코드 주석",
    "권위와 지시를 중시하는 낙하산형 관리자",
    "자산을 사용하지 않고 소유와 관리만 하는 인물",
    "서버 모니터링과 로그 확인을 반복하는 역할",
    "뱀",
    "단순한 조직이 아니라 관계를 맺은 동료 관계",
    "없는 정보",
    "없는 정보",
]

def grade_predictions(questions, predicted_answers, model_name="gpt-4o-mini"):
    grading_prompt = ChatPromptTemplate.from_template("""
너는 자동 채점 시스템이야. 아래는 사용자의 질문, 모델이 예측한 답변, 그리고 정답이야.

각 항목마다 다음 기준으로 점수를 매겨줘:
- 정확히 일치하면 1점
- 수치가 아닐 경우 부분적으로 맞지만 누락, 오탈자 등이 있으면 0.5점
- 수치가 조금이라도 틀리거나 전혀 다르면 0점

항목별 점수와 간단한 설명만 출력해줘. 총점은 계산하지 마.
출력 형식은 다음과 같아야 해:
1번: 1점 (설명)
2번: 0점 (설명)
...

질문-답변 리스트:
{qa_pairs}
""")

    llm = ChatOpenAI(model=model_name, temperature=0)
    parser = StrOutputParser()

    qa_string = "\n".join(
        [
            f"{i+1}. 질문: {questions[i]}\n예측: {predicted_answers[i]}\n정답: {answer_key[i]}"
            for i in range(len(questions))
        ]
    )

    grading_chain = grading_prompt | llm | parser
    result = grading_chain.invoke({"qa_pairs": qa_string})
    return result


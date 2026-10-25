# Cross-Domain Skill Composition: 생성식과 전체 대안의 비교

**최소값으로 두 신호를 결합한 큐 정책, 세제곱 스트레스를 반영한 열 관리 정책.** 생성된 식이 어떻게 작동하고, 전체 대안과 비교했을 때 무엇을 검토할 만한지 살펴봅니다.

[국문 핵심 사례 읽기](v1.5.0/case_highlights_ko.md) · [최신 논문 PDF](v1.5.0/paper.pdf) · [전체 대안·이득·손실 분석](v1.5.0/analysis_report.md)

![전체 원래 선택 정책에서 두 사례의 위치](v1.5.0/policy_alternatives.png)

| 사례 | 이번에 확인한 위치 | 후속 판단 |
| --- | --- | --- |
| A1 최소값 결합 | Network 원래 정책 30개 중 선택·시험 평균 5위. 더 작은 중립식과 569/600 경로에서 보상 동률 | 동작 설명 사례로 유지. 평균 보상과 크기로는 단순 대안을 선호 |
| A2 세제곱 스트레스 | Thermal 원래 정책 30개 중 선택·시험 평균 1위. 단순 대안보다 평균은 높지만 210/600 경로에서 손실 | 추가 6노드와 관측 손실을 감수할 가치가 있는지 검토 |
| A5 계수 수정 | 기준식보다 높지만 더 단순한 중립 대안보다 낮음 | 후순위 반례로 유지 |

원래 주제는 생물학·HCI 탐색 관점과 미니멀 디자인 지침을 프롬프트에서 결합하는 것입니다. 모델은 제공된 수학 힌트·문법·변수·피드백 안에서 식을 구성했습니다. 두 핵심 구조가 중립 조건에서도 나타났고 원래 주 대비 X_ROLE−N_ROLE은 **−0.1111**이므로, 이종 도메인 결합의 인과적 우위는 주장하지 않습니다.

## 최신 자료 v1.5.0

- [논문 PDF](v1.5.0/paper.pdf) · [원고 Markdown](v1.5.0/main_submission_final.md) · [LaTeX 소스](v1.5.0/manuscript-source-v1.5.0.zip)
- [국문 핵심 사례](v1.5.0/case_highlights_ko.md) · [분석 보고서](v1.5.0/analysis_report.md) · [분석·재현 코드](v1.5.0/alternatives-analysis-v1.5.0.zip)
- [파일 해시](v1.5.0/SHA256SUMS.txt) · [v1.4 자료](v1.4.0/) · [v1.3 전체 목록·원문·선정 기록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip)
- [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [전체 1,080개 목록 다운로드](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [기존 국문 사례 카드](case_cards_ko.md)

새 분석은 원래 선택 정책 90개를 과제별로 정리하고, A1/A2 각각에 대해 같은 과제의 30개 원래 선택 정책 및 기준식과 비교한 **62개 결과**를 제공합니다. 전체 360개 제출식의 보조 순위에서는 A1 시험값 분모 327, A2 분모 306을 명시하며 미시험을 실패로 세지 않습니다. 600개 시험 경로는 독립적인 모델 생성 표본이 아닙니다. 평균 보상·식 크기·관측 손실은 실제 적용 가치나 실행 속도의 검증이 아닙니다.

이전 공개 파일과 원자료는 보존했습니다. 이번 개정에는 새 연구 모델 호출·환경 평가·통계 시뮬레이션이 없습니다. 내려받은 분석 ZIP README의 명령으로 저장 자료만을 사용해 재현할 수 있습니다.

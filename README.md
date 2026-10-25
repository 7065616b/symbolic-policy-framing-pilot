# Cross-Domain Skill Composition: 입력에서 산출물과 판단까지

생물학·HCI 탐색 관점과 미니멀 디자인 지침을 결합한 프롬프트에서 생성된 정책식을 살펴봅니다. **흥미로운 구조도 전체 대안 앞에서는 후순위가 될 수 있고, 평균이 가장 높은 식도 손실을 함께 봐야 합니다.**

[국문 비교표·A2 계산 예시](v1.6.0/case_highlights_ko.md) · [최신 논문 PDF](v1.6.0/paper.pdf) · [원고](v1.6.0/main_submission_final.md)

| 사례 | 무엇이 나왔나 | 전체 대안과 비교한 판단 |
| --- | --- | --- |
| A1 | 두 신호가 함께 높을 때 기여하는 최소값 결합 | 설명은 쉽지만, 더 작은 중립식과 569/600 경로에서 보상 동률. 평균 보상·크기로는 단순 대안 선호 |
| A2 | 세제곱 스트레스와 제공된 곱 항을 결합한 식 | 원래 선택 정책 30개 중 평균 1위. 단순 대안보다 6노드가 더 필요하고 210/600 경로에서 손실 |

v1.6.0은 제공 입력 → 도출식 → 대안 → 판단 비교표와 가상 입력의 A2 계산 예시를 추가한 편집 개정입니다. 예시는 선택이 달라지는 이유를 보여주며, 새 환경 관측이나 현실 효용을 입증하는 결과가 아닙니다.

## 최신 자료

- [논문 PDF](v1.6.0/paper.pdf) · [LaTeX 소스](v1.6.0/manuscript-source-v1.6.0.zip) · [국문 설명](v1.6.0/case_highlights_ko.md)
- [계산 코드](v1.6.0/worked_example.py) · [계산 결과](v1.6.0/worked_example.json) · [파일 해시](v1.6.0/SHA256SUMS.txt)
- [변경 없는 전체 대안·이득·손실 분석](v1.5.0/analysis_report.md) · [분석·재현 코드](v1.5.0/alternatives-analysis-v1.5.0.zip)
- [v1.5 자료](v1.5.0/) · [v1.4 자료](v1.4.0/) · [전체 목록·출처·선정 기록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip)
- [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [1,080개 제출 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [기존 국문 사례 카드](case_cards_ko.md)

두 핵심 구조는 중립 조건에서도 나타났고, 원래 주 대비 X_ROLE−N_ROLE은 **−0.1111**입니다. 원래 주제를 유지하면서 이종 도메인 결합의 인과적 우위, 내부 추론 과정, 실제 적용 가치를 입증했다는 주장은 하지 않습니다. 미시험 제출은 실패로 세지 않으며 600개 경로를 독립적인 모델 생성으로 취급하지 않습니다.

이전 자료와 원래 분석은 보존했습니다. 이번 개정에는 새 모델 호출·환경 평가·통계 시뮬레이션이 없습니다.

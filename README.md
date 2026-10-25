# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**이종 도메인 스킬 결합: 생성 정책에 관한 탐색적 연구**

생물학·HCI 탐색 관점과 미니멀 디자인 지침을 결합한 프롬프트에서 나온 정책식을 검토합니다. **A2는 후속 검토할 중심 후보**, **A1은 비교 범위를 넓히자 판단이 달라진 사례**로 설명합니다.

[국문 안내·비교표·계산 예시](v1.7.0/case_highlights_ko.md) · [최신 논문 PDF](v1.7.0/paper.pdf) · [원고](v1.7.0/main_submission_final.md)

| 사례 | 논문에서의 역할 | 근거와 남은 한계 |
| --- | --- | --- |
| A2 | 중심 후보: 세제곱 스트레스와 제공된 곱 항을 결합한 Thermal 정책 | 같은 과제 원래 선택 정책 30개 중 선택·시험 평균 1위. 단순 대안보다 6노드가 더 필요하고 210/600 경로에서 손실 |
| A1 | 비교 범위에 따라 판단이 달라진 최소값 결합 사례 | 같은 블록에서는 유리했지만 전체 대안에는 더 작은 중립식이 있음. 이 대안과 569/600 경로에서 보상 동률 |

중심 후보는 다섯 고정 사후 사례 안에서의 설명상 강조입니다. 과제 간 평균을 합쳐 순위를 매기거나 시험값으로 새 정책을 선택하지 않았습니다. A2의 계산 예시는 가상의 정규화 입력으로 선택 차이를 설명하며, 새 환경 관측이나 실제 적용 가치의 증거가 아닙니다.

## 최신 자료 v1.7.0

- [논문 PDF](v1.7.0/paper.pdf) · [LaTeX 소스](v1.7.0/manuscript-source-v1.7.0.zip) · [국문 안내](v1.7.0/case_highlights_ko.md)
- [계산 코드](v1.7.0/worked_example.py) · [계산 결과](v1.7.0/worked_example.json) · [파일 해시](v1.7.0/SHA256SUMS.txt)
- [변경 없는 전체 대안·이득·손실 분석](v1.5.0/analysis_report.md) · [분석·재현 코드](v1.5.0/alternatives-analysis-v1.5.0.zip)
- [v1.6 자료](v1.6.0/) · [v1.5 자료](v1.5.0/) · [전체 목록·출처·선정 기록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip)
- [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [1,080개 제출 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [기존 국문 사례 카드](case_cards_ko.md)

두 핵심 구조는 중립 조건에서도 나타났고 원래 X_ROLE−N_ROLE 주 대비는 **−0.1111**입니다. 이종 도메인 결합이라는 원래 주제를 유지하며, 인과적 우위·내부 지식 연결 과정·현실 효용을 입증했다고 주장하지 않습니다. 미시험 제출은 실패로 세지 않고, 600개 시험 경로는 독립적인 모델 생성 표본이 아닙니다.

이전 자료와 원래 분석은 보존했습니다. 이번 개정에는 새 모델 호출·환경 평가·통계 시뮬레이션이 없습니다.

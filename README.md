# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**이종 도메인 스킬 결합: 생성 정책에 관한 탐색적 연구**

생물학·HCI 탐색과 미니멀 디자인 지침을 결합한 프롬프트에서 나온 정책을 평가합니다. A2는 후속 검토 후보, A1은 비교 범위에 따라 판단이 바뀐 사례입니다. 이종 도메인 결합의 인과 효과나 현실 효용을 입증했다고 주장하지 않습니다.

[쉽게 읽는 핵심 결과](v1.9.0/case_highlights_ko.md) · [최신 논문 PDF](v1.9.0/paper.pdf) · [원고](v1.9.0/main_submission_final.md)

## v1.9.0: 전체 기존 시드에서 확인한 손익

- A2와 세 고정 대안을 기존 600개 시드 전체에서 분석했습니다. 위험 지표 보상 이득이 다른 벌점에서 일부 상쇄됩니다.
- 중립 대안 N 대비 처음 손해여도 최종 이득인 시드는 272개, 반대는 36개입니다. 최초 선택과 전체 경로를 구분합니다.
- 가까운 대안의 식·크기·성능, 선택 전환식, 원시 상태 보상함수를 논문에 함께 제시합니다.
- 2,400개 정책·시드 보상과 기준식 600개는 원기록과 정확히 일치합니다. 새 모델 호출·새 시드·새 독립 표본은 없습니다.

## 자료

- [분석 보고서](v1.9.0/all_seeds_report_ko.md) · [전체 시드 코드·입력·결과](v1.9.0/a2-all-seeds-analysis-v1.9.0.zip)
- [LaTeX 원고 소스](v1.9.0/manuscript-source-v1.9.0.zip) · [검증](v1.9.0/all_seeds_verification.json) · [해시](v1.9.0/SHA256SUMS.txt)
- [이전 실제 경로 재생](v1.8.0/case_highlights_ko.md) · [전체 대안 분석](v1.5.0/analysis_report.md)
- [전체 1,080개 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [원래 사례 카드](case_cards_ko.md)

기존 버전과 원자료를 보존합니다. 원래 전체 대비 −0.1111, 중립 조건의 유사 구조, 제공 힌트·보상식 겹침, 단일 모델·여섯 블록·합성 환경·사후 분석의 한계는 그대로입니다.

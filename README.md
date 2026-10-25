# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**이종 도메인 스킬 결합: 생성 정책에 관한 탐색적 연구**

A2를 후속 검토 후보로, A1을 비교 범위에 따라 판단이 달라진 사례로 설명합니다. 생물학·HCI 탐색과 미니멀 디자인 지침을 결합한 프롬프트에서 나온 산출물을 검토하며, 인과적 우위나 현실 효용을 입증했다고 주장하지 않습니다.

[국문 안내·실제 재생 사례](v1.8.0/case_highlights_ko.md) · [최신 논문 PDF](v1.8.0/paper.pdf) · [원고](v1.8.0/main_submission_final.md)

## v1.8.0의 추가 내용

- A2와 단순식·선택 평균 최상위 중립식·같은 크기의 유사식 비교. 중립식 대비 308승·292패이며, A2가 2노드 작지만 평균 차이는 작습니다.
- 기존 시드의 실제 합성 입력·선택·보상 기록. 이득과 손실을 모두 보여주고, 처음 손해여도 전체 경로에서는 이득인 사례를 포함합니다.
- 네 정책 × 기존 시드 600개 = 2,400개 보상값의 정확한 재생 일치. 새 모델 호출이나 독립 표본 추가는 없습니다.

## 자료

- [논문 PDF](v1.8.0/paper.pdf) · [LaTeX 소스](v1.8.0/manuscript-source-v1.8.0.zip)
- [재생 보고서](v1.8.0/replay_report_ko.md) · [재생 코드·입력·전체 여섯 경로 쌍](v1.8.0/a2-replay-analysis-v1.8.0.zip)
- [재생 검증](v1.8.0/replay_verification.json) · [파일 해시](v1.8.0/SHA256SUMS.txt)
- [기존 전체 대안·이득·손실 분석](v1.5.0/analysis_report.md) · [이전 v1.7 자료](v1.7.0/)
- [전체 1,080개 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [원래 사례 카드](case_cards_ko.md)

재생 사례는 부호에 따라 고른 사후 예시이며 대표 표본이 아닙니다. 최초 선택 차이 이후에는 두 정책의 상태가 달라질 수 있습니다. 곱 항은 제공 힌트 및 보상식과 겹치고 세제곱 구조는 중립 조건에서도 나타납니다. 원래 전체 대비 −0.1111, 단일 모델·여섯 블록·합성 환경·사후 분석의 한계와 이전 자료를 보존했습니다.

# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**이종 도메인 스킬 결합: 생성 정책에 관한 탐색적 연구**

생물학·HCI 탐색과 미니멀 디자인 지침을 결합한 프롬프트에서 나온 정책을 평가합니다. 제공된 요소, 생성된 변화, 확인되지 않은 지식 전이를 구분하고 A2를 조건부 후속 검토 후보로 남깁니다. 이종 도메인 결합의 인과 효과나 현실 효용은 입증하지 않습니다.

[쉽게 읽는 핵심 결과](v1.10.1/case_highlights_ko.md) · [최신 논문 PDF](v1.10.1/paper.pdf) · [원고](v1.10.1/main_submission_final.md)

## 최종 제출용 문장 정리: v1.10.1

초록에서 핵심 판단을 먼저 설명하고, 작업 이력을 연구 방법 표현으로 바꾸며, 예시 개수를 대안별 2쌍·총 6쌍으로 명확히 했습니다. 결과와 한계는 그대로입니다. 새 모델 호출이나 추가 분석은 없습니다. 최종 제출용 파일을 준비한 상태이며 학회 접수를 완료했다는 뜻은 아닙니다.

[제출 파일·마지막 확인 사항](v1.10.1/SUBMISSION_CHECKLIST_KO.md) · [접수용 국문 초록](v1.10.1/easychair_korean_abstract.md)

## v1.10.0: 평가 기준을 바꾸면 A2의 선호도 바뀐다

- 기존 네 정책과 600개 시드를 36개 고정 가중치 설정으로 재평가했습니다. 새 모델 호출·정책·시험 시드는 없습니다.
- 동시 ±25% 변경 27개 조합에서 A2는 22개 1위, 3개 2위, 2개 3위입니다. N에 4개, C에 3개에서 뒤집니다. 이는 격자 개수이며 성공 확률이 아닙니다.
- 위험 지표 보상 가중치를 절반으로 낮추면 네 정책 중 마지막입니다. A2를 기본 대체 정책으로 채택하는 판단은 보류합니다.
- 보상 하한을 단계별로 다시 적용한 86,400개 값이 직접 실행과 정확히 일치하고 원래 보상 2,400개도 보존됩니다. 평가 기록 수는 독립 표본 수가 아닙니다.

## 자료

- [분석 보고서](v1.10.0/sensitivity_report_ko.md) · [코드·고정 입력·전체 결과](v1.10.0/a2-sensitivity-analysis-v1.10.0.zip)
- [제공·생성 요소 구분](v1.10.0/provenance_A2.json) · [원래 A2 프롬프트](v1.10.0/source_prompt_A2.json)
- [LaTeX 소스](v1.10.1/manuscript-source-v1.10.1.zip) · [검증](v1.10.0/sensitivity_verification.json) · [해시](v1.10.0/SHA256SUMS.txt)
- [이전 전체 시드 분석](v1.9.0/case_highlights_ko.md) · [실제 경로 사례](v1.8.0/case_highlights_ko.md) · [전체 대안 비교](v1.5.0/analysis_report.md)
- [전체 1,080개 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [원래 사례 카드](case_cards_ko.md)

기존 버전과 원자료를 보존합니다. 원래 전체 대비 −0.1111, 중립 조건의 유사 구조, 제공 힌트·보상식 겹침, 단일 모델·여섯 블록·합성 환경·사후 분석의 한계는 그대로입니다.

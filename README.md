# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**이종 도메인 스킬 결합: 생성 정책에 관한 탐색적 연구**

서로 다른 분야의 관점을 결합해 AI가 작업에 쓸 스킬을 만들도록 하고, 무엇이 나왔으며 왜 쓸 만한지 살펴봅니다. 여기서 스킬은 여러 선택지 중 무엇을 먼저 처리할지 정하는 작은 실행 규칙입니다. 생물학·HCI·디자인은 아이디어를 얻는 분야이며, 네트워크·열 관리·클라우드는 규칙을 시험한 모의 과제입니다. 도메인 결합의 인과적 우위와 실제 효용은 아직 입증하지 못했습니다.

[쉽게 읽는 핵심 결과](v1.10.3/case_highlights_ko.md) · [최신 논문 PDF](v1.10.3/paper.pdf) · [원고](v1.10.3/main_submission_final.md)

## 연구 질문을 먼저 설명한 수정본: v1.10.3

초록과 도입부를 입력 → 생성된 규칙 → 쓸모에 대한 판단 순서로 고쳤습니다. 수치·표·수식·그림과 한계는 유지했습니다. 본문은 8쪽이며 참고문헌·필수 요약을 포함해 10쪽입니다. 학회 접수번호 54의 PDF와 국문 초록을 갱신했습니다. 새 모델 호출이나 추가 분석은 없습니다.

[접수본 확인 사항](v1.10.3/SUBMISSION_CHECKLIST_KO.md) · [접수용 국문 초록](v1.10.3/easychair_korean_abstract.md)

## v1.10.0: 평가 기준을 바꾸면 A2의 선호도 바뀐다

- 기존 네 정책과 600개 시드를 36개 고정 가중치 설정으로 재평가했습니다. 새 모델 호출·정책·시험 시드는 없습니다.
- 동시 ±25% 변경 27개 조합에서 A2는 22개 1위, 3개 2위, 2개 3위입니다. N에 4개, C에 3개에서 뒤집니다. 이는 격자 개수이며 성공 확률이 아닙니다.
- 위험 지표 보상 가중치를 절반으로 낮추면 네 정책 중 마지막입니다. A2를 기본 대체 정책으로 채택하는 판단은 보류합니다.
- 보상 하한을 단계별로 다시 적용한 86,400개 값이 직접 실행과 정확히 일치하고 원래 보상 2,400개도 보존됩니다. 평가 기록 수는 독립 표본 수가 아닙니다.

## 자료

- [분석 보고서](v1.10.0/sensitivity_report_ko.md) · [코드·고정 입력·전체 결과](v1.10.0/a2-sensitivity-analysis-v1.10.0.zip)
- [제공·생성 요소 구분](v1.10.0/provenance_A2.json) · [원래 A2 프롬프트](v1.10.0/source_prompt_A2.json)
- [LaTeX 소스](v1.10.3/manuscript-source-v1.10.3.zip) · [검증](v1.10.0/sensitivity_verification.json) · [해시](v1.10.0/SHA256SUMS.txt)
- [이전 전체 시드 분석](v1.9.0/case_highlights_ko.md) · [실제 경로 사례](v1.8.0/case_highlights_ko.md) · [전체 대안 비교](v1.5.0/analysis_report.md)
- [전체 1,080개 목록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [원자료](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip) · [원래 사례 카드](case_cards_ko.md)

기존 버전과 원자료를 보존합니다. 원래 전체 대비 −0.1111, 중립 조건의 유사 구조, 제공 힌트·보상식 겹침, 단일 모델·여섯 블록·합성 환경·사후 분석의 한계는 그대로입니다.

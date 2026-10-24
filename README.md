# Cross-Domain Skill Composition: Generated Artifacts

생물학·HCI의 탐색 관점과 미니멀 산업디자인의 간결성 지침을 **프롬프트 안에서 결합**한 파일럿입니다. 어떤 식이 생성됐는지, 입력과 어떻게 다른지, 무엇을 후속 검토할 만하다고 판단했는지를 공개합니다. 도메인 관점은 사람이 프롬프트에 명시했고, 모델은 제공된 문법·과제 정보·수학 힌트·이전 피드백 안에서 식을 만들었습니다.

## 먼저 결과물 보기

1. [전체 1,080개 제출식 검색 HTML 다운로드](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html): 저장 후 브라우저에서 열면 인터넷 없이 검색·필터·원문 확인이 됩니다. 사례 카드까지 함께 보려면 아래 분석 묶음을 내려받으세요.
2. [대표 사례 5개와 사용 설명 읽기](case_cards_ko.md): 실제 식, 입력 H, 이전 라운드에서 달라진 점, 선정 이유, 같은 블록 대안, 활용 가능성과 한계.
3. [수정 논문 PDF](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/paper.pdf): **Cross-Domain Skill Composition for Policy Generation: An Artifact-Centered Pilot**.
4. [전체 분석·코드·선정/제외 기록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip): CSV/JSON과 국·영문 카드, 표·재현 코드 포함.

## 실제로 나온 식과 판단

| 사례 | 실제 생성식 | 생성 조건 | 시험 U | 후속 검토 판단 |
| --- | --- | --- | ---: | --- |
| A1 | `queue+min(drift,burst)-0.5*idle` | X_ROLE | 1.003905 | 우선 검토 후보 |
| A2 | `temp+(0.5*(soc*imped)+stress*stress*stress)` | X_ROLE | 1.011170 | 성능·크기 절충 검토 |
| A3 | `idle-0.35*min(freq-0.5,0.25)+0.2*jitter` | X_ROLE | 1.000466 | 낮은 우선순위 진단 |
| A4 | `temp+soc*imped+2*max(stress-0.5,0)` | X_FLAT | 1.009928 | 제공 힌트의 조립·대조 사례 |
| A5 | `queue*(0.35+drift)-0.25*idle` | X_ROLE | 1.002104 | 더 단순한 중립 대안보다 후순위 |

위 판단은 후속 검토를 위한 **저자의 탐색적 판단**입니다. 다섯 개의 발명이나 실용성이 입증된 제품을 뜻하지 않습니다. U=1은 해당 합성 과제의 단순 기준식이며, 작은 수치 초과는 실질적 효용의 증명이 아닙니다. A1/A2의 min 결합·세제곱 항은 H에 그대로 제시되지 않았지만 같은 세션의 이전 라운드에서 먼저 나타났고, 선정 식은 그 후의 수정입니다. A3–A5는 제공 힌트 재사용이 큽니다. A5보다 같은 블록의 N_ROLE 식이 더 단순하고 시험 점수도 높습니다.

## 범위와 불리한 결과도 함께 보기

- 90세션 × 4라운드 × 3식 = 1,080개 제출입니다. 도메인·원문 문자열 조합은 822개이며 독립적인 새 아이디어 수가 아닙니다.
- 시험값은 944개이고 136개는 미시험입니다. 원래 선택된 정책 90개와 행동 성분 대표 916개를 보존했습니다.
- 사례 규칙은 기존 시험 결과를 본 뒤 만든 사후 규칙입니다. 함수는 selection 필드로 ID를 고정한 뒤 saved test를 붙이며, 전역 최고 5개나 성공률 추정이 아닙니다.
- 원래 주 결과 X_ROLE−N_ROLE은 **−0.1111** 근접 성능 성분/세션입니다. 엄격 기준 초과 대비 **+0.3333**은 별도 결과이며 주 결과를 대체하지 않습니다.
- 단일 모델, 고정 문구, 합성 환경, 공유된 수학 힌트, 적은 반복, 개별 모듈 제거 대조군 부재라는 한계가 남습니다. 도메인별 지식 기여·결합 시너지·현실 효용·실행 시간 효율은 입증되지 않았습니다.

## 자료와 재현

[v1.3.0 전체 릴리스](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.3.0) · [파일 해시](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/SHA256SUMS.txt) · [논문 소스](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/manuscript-source-v1.3.0.zip)

원자료 [public-supplement-v1.0.0.zip](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/public-supplement-v1.0.0.zip)와 이전 분석 [composition-analysis-v1.2.0.zip](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/composition-analysis-v1.2.0.zip)은 이전 공개 버전과 바이트 단위로 같습니다. 세 분석 폴더를 나란히 풀고 artifact 묶음 README의 Python 표준 라이브러리 명령을 실행하면 목록·사례·카드를 재구성할 수 있습니다. 새 모델 호출이나 시뮬레이터 실행은 필요하지 않습니다.

원자료 SHA-256: `01073c19bad8d4bb2e5ab330508e35588fb9adc9011eb2bac6ce84f95b701500`.

서버 스냅샷과 샘플링 시드가 없어 동일한 모델 출력을 다시 생성할 수 있다는 주장은 하지 않습니다. 공개 projection의 해시는 비공개 원본 저널 봉인을 검증하지 않습니다. 이전 [v1.0.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.0.0), [v1.1.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.1.0), [v1.2.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.2.0)은 유지합니다. 이번 개정에는 새 연구 모델 호출·환경 trace·통계 시뮬레이션이 없습니다.

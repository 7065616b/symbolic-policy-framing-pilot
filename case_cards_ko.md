# 생성 정책식: 선정 사례와 사용 설명

이 다섯 건은 사후 규칙으로 고른 설명용 사례이며, 다섯 개의 새로운 발명이나 검증된 제품이 아니다. 입력·출력·측정값과 저자 해석을 구분한다. 원래 선택 자료로 IDs를 고정한 뒤 저장된 시험 결과를 붙였으며, 규칙을 정하기 전 전체 파일럿 시험 결과를 열람한 이력이 있다.

[전체 1,080개 제출식 보기](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/catalog.html) · [선정 규칙](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip) · [선정/제외 기록](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.3.0/artifact-analysis-v1.3.0.zip)

모든 사용 설명은 저자가 식을 해석한 것이다. 모델은 식 배열만 출력했으므로 발상 이유나 내부 추론을 보고한 것으로 쓰지 않는다. U=1은 해당 합성 과제의 고정 기준식이다. 시험값은 정책당 600개 저장 trace의 평균 보상 비율이며 600개의 독립 모델 생성이 아니다.

## A1. 두 신호의 작은 값을 반영하는 큐 우선순위

`queue+min(drift,burst)-0.5*idle`

- **출처:** Network / X_ROLE / block 4 / round 3 / slot 7
- **ID:** `pilot-Network-04-X_ROLE-slot7`
- **선정 이유:** 해당 도메인 X_ROLE의 원래 선택 정책 중 selection utility 최대
- **기록된 구조:** 9 nodes, implemented depth 2; min

**무엇을 하는 식인가 — 저자 해석**
queue를 기본 점수로 두고 drift와 burst 중 작은 값만 추가한다. 어느 한 신호만 커도 점수가 크게 증가하는 것을 제한하고 idle에는 음의 가중치를 준다.

**입력과 출력의 차이**
H에는 queue*(0.45+drift), max(burst-idle,0), 음의 idle 항이 있었다. 이 식의 min(drift,burst)는 해당 H에 직접 제시된 조합은 아니다. 이것이 생물학적 면역 원리에서 유래했다는 증거는 없으며 새 알고리즘의 발명이라는 뜻도 아니다.

> Common mathematical hints H: consider queue*(0.45+drift), max(burst-idle,0), and a negative idle term. These are optional engineering templates. All constants remain subject to the same grammar and complexity limits.

**같은 세션에서 관측된 변화**
아래 이전 출력과 feedback은 선택된 응답 직전 요청에 포함됐다. 최종 식과의 비교는 관측 가능한 수정 이력이며, 모델이 수정한 이유를 추정한 것이 아니다. 최초 도메인 관점은 프롬프트에 명시되었고 모델이 도메인 자체를 고른 것은 아니다.

- R2/S6: `queue+min(drift,burst)-0.25*idle` — `pilot-Network-04-X_ROLE-slot6`, response line 198
- 선정 식: `queue+min(drift,burst)-0.5*idle`

**활용 방법**
네 개 합성 큐의 정규화된 특성으로 점수를 계산하고 최고 점수 큐를 선택하는 후보 규칙이다. 두 신호가 함께 높은 경우를 우선하려는 해석이 가능하다.

모든 입력 특성은 음수를 0으로 자른 뒤 x/(1+x)로 정규화한다. 각 옵션의 점수를 계산하고 최대 점수 옵션을 고른다. 동일 점수에서는 평가기처럼 첫 옵션을 유지한다. 이 설명을 위해 새 환경 trace를 실행하지 않았다.

| 조건 | Selection U | Test U | Nodes | Depth |
| --- | ---: | ---: | ---: | ---: |
| N_FLAT | 1.002993 | 1.003228 | 9 | 2 |
| N_ROLE | 1.000482 | 1.000870 | 13 | 3 |
| X_FLAT | 1.001797 | 1.002284 | 9 | 2 |
| X_ROLE | 1.003469 | 1.003905 | 9 | 2 |
| DOMAIN_V2 | 1.000724 | 1.001215 | 11 | 4 |

동일 도메인·블록의 원래 선택 정책 비교다. 사례를 고른 뒤 붙인 설명용 비교이며 일반적인 순위나 확증 검정이 아니다.

**판정과 한계**
선택한 단일 블록의 관측이다. 작은 기준 초과나 이 사례의 비교 우위를 전체 프롬프트의 효과로 확대하지 않는다.

**후속 검토 판단 — 저자의 탐색적 판단**
우선 검토 후보. H에 없는 min 결합과 9노드 구조를 갖고 같은 블록의 N_ROLE/X_FLAT보다 저장 시험 점수가 높다. 추가 검증 대상으로 남긴다는 저자 판단이며, 실제 활용 효과 판정은 아니다.

**기준식:** `queue+0.45*drift+0.15*burst-0.15*idle`

**추적 경로 — 원자료 폴더 기준**
- Prompt: `data/prompts/pilot-Network-04-X_ROLE.json`
- Request and preceding answers/feedback: `data/requests/pilot-Network-04-X_ROLE-r3-a1.request.json`
- Response: `data/response-projection.jsonl`, line 199
- Selection/test: `data/selection.json` / `data/final.json`, session `pilot-Network-04-X_ROLE`, slot `pilot-Network-04-X_ROLE-slot7`

## A2. 곱 상호작용과 세제곱 스트레스의 열제어 점수

`temp+(0.5*(soc*imped)+stress*stress*stress)`

- **출처:** Thermal / X_ROLE / block 5 / round 4 / slot 10
- **ID:** `pilot-Thermal-05-X_ROLE-slot10`
- **선정 이유:** 해당 도메인 X_ROLE의 원래 선택 정책 중 selection utility 최대
- **기록된 구조:** 13 nodes, implemented depth 2; variable-product

**무엇을 하는 식인가 — 저자 해석**
온도에 0.5*soc*imped와 stress의 세제곱을 더한다. [0,1] 범위에서 세제곱 항은 낮은 스트레스를 작게 반영하고 높은 스트레스에 상대적으로 더 무게를 둔다.

**입력과 출력의 차이**
soc*imped와 온도 항은 이미 H에 있었다. H의 max(stress-0.5,0)와 달리 stress*stress*stress를 사용한다. 따라서 힌트 일부 재사용과 다른 스트레스 표현이 공존한다.

> Common mathematical hints H: consider soc*imped, max(stress-0.5,0), and a temperature term. These are optional engineering templates. All constants remain subject to the same grammar and complexity limits.

**같은 세션에서 관측된 변화**
아래 이전 출력과 feedback은 선택된 응답 직전 요청에 포함됐다. 최종 식과의 비교는 관측 가능한 수정 이력이며, 모델이 수정한 이유를 추정한 것이 아니다. 최초 도메인 관점은 프롬프트에 명시되었고 모델이 도메인 자체를 고른 것은 아니다.

- R3/S9: `temp+(soc*imped+stress*stress*stress)` — `pilot-Thermal-05-X_ROLE-slot9`, response line 339
- 선정 식: `temp+(0.5*(soc*imped)+stress*stress*stress)`

**활용 방법**
네 합성 모듈 중 출력 감소 우선순위를 정하는 점수로 넣을 수 있다. 높은 스트레스 모듈의 상대적 순위를 바꾸는 방식을 설명하기 쉽다.

모든 입력 특성은 음수를 0으로 자른 뒤 x/(1+x)로 정규화한다. 각 옵션의 점수를 계산하고 최대 점수 옵션을 고른다. 동일 점수에서는 평가기처럼 첫 옵션을 유지한다. 이 설명을 위해 새 환경 trace를 실행하지 않았다.

| 조건 | Selection U | Test U | Nodes | Depth |
| --- | ---: | ---: | ---: | ---: |
| N_FLAT | 1.009853 | 1.008839 | 13 | 4 |
| N_ROLE | 1.009537 | 1.008923 | 11 | 3 |
| X_FLAT | 1.010594 | 1.009897 | 7 | 2 |
| X_ROLE | 1.011889 | 1.011170 | 13 | 2 |
| DOMAIN_V2 | 1.008165 | 1.007917 | 9 | 4 |

동일 도메인·블록의 원래 선택 정책 비교다. 사례를 고른 뒤 붙인 설명용 비교이며 일반적인 순위나 확증 검정이 아니다.

**판정과 한계**
같은 블록의 X_FLAT에는 temp+stress*stress*stress라는 7노드 식도 있다. A2는 13노드이며 더 높은 시험 utility와 더 큰 식 크기를 함께 보고해야 한다. 현실 배터리 안전성 검증은 아니다.

**후속 검토 판단 — 저자의 탐색적 판단**
복잡도와 성능의 절충을 검토할 후보. 더 높은 시험 점수와 13노드 크기를 함께 고려하며, 7노드 X_FLAT 세제곱 식과 비교할 가치가 있다.

**기준식:** `temp+0.4*soc+0.35*imped+0.25*stress`

**추적 경로 — 원자료 폴더 기준**
- Prompt: `data/prompts/pilot-Thermal-05-X_ROLE.json`
- Request and preceding answers/feedback: `data/requests/pilot-Thermal-05-X_ROLE-r4-a1.request.json`
- Response: `data/response-projection.jsonl`, line 340
- Selection/test: `data/selection.json` / `data/final.json`, session `pilot-Thermal-05-X_ROLE`, slot `pilot-Thermal-05-X_ROLE-slot10`

## A3. 상한이 있는 빈도 보정의 슬롯 회수 점수

`idle-0.35*min(freq-0.5,0.25)+0.2*jitter`

- **출처:** Cloud / X_ROLE / block 1 / round 3 / slot 7
- **ID:** `pilot-Cloud-01-X_ROLE-slot7`
- **선정 이유:** 해당 도메인 X_ROLE의 원래 선택 정책 중 selection utility 최대
- **기록된 구조:** 13 nodes, implemented depth 4; min

**무엇을 하는 식인가 — 저자 해석**
idle을 기본으로 freq-0.5의 상한을 0.25로 두어 빼고 jitter를 더한다. freq가 0.5보다 작으면 min 항은 음수여서 가산점이 생긴다. freq가 0.75 이상이면 그 보정은 -0.0875로 일정하다.

**입력과 출력의 차이**
min(freq-0.5,0.25), 양의 jitter 항, idle은 이미 H에 있었다. 이 식은 계수 선택과 cost*freq 항의 생략을 보여주며, 상한 구조 자체의 자율 발견 사례로 부르면 안 된다.

> Common mathematical hints H: consider cost*freq, min(freq-0.5,0.25), and a positive jitter term together with idle. The min expression is an upper cap, not a lower clamp. These are optional engineering templates. All constants remain subject to the same grammar and complexity limits.

**같은 세션에서 관측된 변화**
아래 이전 출력과 feedback은 선택된 응답 직전 요청에 포함됐다. 최종 식과의 비교는 관측 가능한 수정 이력이며, 모델이 수정한 이유를 추정한 것이 아니다. 최초 도메인 관점은 프롬프트에 명시되었고 모델이 도메인 자체를 고른 것은 아니다.

- R1/S2: `idle-min(freq-0.5,0.25)+0.2*jitter` — `pilot-Cloud-01-X_ROLE-slot2`, response line 17
- R2/S5: `idle-0.6*min(freq-0.5,0.25)+0.2*jitter` — `pilot-Cloud-01-X_ROLE-slot5`, response line 18
- 선정 식: `idle-0.35*min(freq-0.5,0.25)+0.2*jitter`

**활용 방법**
여섯 합성 슬롯의 회수 우선순위를 정하는 후보 규칙이다. 음수 영역을 허용하는 상한과 0으로 막는 하한의 차이를 검토할 수 있다.

모든 입력 특성은 음수를 0으로 자른 뒤 x/(1+x)로 정규화한다. 각 옵션의 점수를 계산하고 최대 점수 옵션을 고른다. 동일 점수에서는 평가기처럼 첫 옵션을 유지한다. 이 설명을 위해 새 환경 trace를 실행하지 않았다.

| 조건 | Selection U | Test U | Nodes | Depth |
| --- | ---: | ---: | ---: | ---: |
| N_FLAT | 0.999586 | 0.999435 | 13 | 4 |
| N_ROLE | 0.997716 | 0.997854 | 11 | 3 |
| X_FLAT | 0.999678 | 0.999661 | 15 | 4 |
| X_ROLE | 1.000470 | 1.000466 | 13 | 4 |
| DOMAIN_V2 | 1.000236 | 1.000096 | 9 | 4 |

동일 도메인·블록의 원래 선택 정책 비교다. 사례를 고른 뒤 붙인 설명용 비교이며 일반적인 순위나 확증 검정이 아니다.

**판정과 한계**
시험 utility가 1을 매우 조금 넘는다. 깊이 4는 soft 목표 3보다 크지만 hard gate 5 안에 있다. 실제 클라우드 비용 절감을 입증한 결과는 아니다.

**후속 검토 판단 — 저자의 탐색적 판단**
낮은 우선순위의 진단 사례. H의 상한을 재사용하고 기준 초과 폭이 작아, 활용 후보보다 입력 재사용과 상한 해석을 설명하는 데 적합하다.

**기준식:** `idle`

**추적 경로 — 원자료 폴더 기준**
- Prompt: `data/prompts/pilot-Cloud-01-X_ROLE.json`
- Request and preceding answers/feedback: `data/requests/pilot-Cloud-01-X_ROLE-r3-a1.request.json`
- Response: `data/response-projection.jsonl`, line 19
- Selection/test: `data/selection.json` / `data/final.json`, session `pilot-Cloud-01-X_ROLE`, slot `pilot-Cloud-01-X_ROLE-slot7`

## A4. 힌트 조합에 임계 스트레스 가중치를 둔 점수

`temp+soc*imped+2*max(stress-0.5,0)`

- **출처:** Thermal / X_FLAT / block 3 / round 3 / slot 9
- **ID:** `pilot-Thermal-03-X_FLAT-slot9`
- **선정 이유:** 고정 도메인 순서에서 핵심 사례와 다른 태그 조합을 가진 X_FLAT 원래 선택 정책
- **기록된 구조:** 13 nodes, implemented depth 4; max, variable-product

**무엇을 하는 식인가 — 저자 해석**
온도와 soc*imped를 더하고, stress가 0.5를 넘는 양의 부분에 가중치 2를 적용한다.

**입력과 출력의 차이**
온도 항, soc*imped, max(stress-0.5,0) 모두 H에 있다. 결과물의 기록상 가치는 이를 조립하고 가중치를 선택한 데 있으며 새로운 도메인 간 연결을 확인한 사례는 아니다.

> Common mathematical hints H: consider soc*imped, max(stress-0.5,0), and a temperature term. These are optional engineering templates. All constants remain subject to the same grammar and complexity limits.

**같은 세션에서 관측된 변화**
아래 이전 출력과 feedback은 선택된 응답 직전 요청에 포함됐다. 최종 식과의 비교는 관측 가능한 수정 이력이며, 모델이 수정한 이유를 추정한 것이 아니다. 최초 도메인 관점은 프롬프트에 명시되었고 모델이 도메인 자체를 고른 것은 아니다.

- R2/S5: `temp+2*max(stress-0.5,0)` — `pilot-Thermal-03-X_FLAT-slot5`, response line 294
- R2/S6: `temp+soc*imped+max(stress-0.5,0)` — `pilot-Thermal-03-X_FLAT-slot6`, response line 294
- 선정 식: `temp+soc*imped+2*max(stress-0.5,0)`

**활용 방법**
임계값 이하와 이상의 스트레스를 다르게 처리하는 간단한 합성 모듈 순위 규칙으로 읽을 수 있다.

모든 입력 특성은 음수를 0으로 자른 뒤 x/(1+x)로 정규화한다. 각 옵션의 점수를 계산하고 최대 점수 옵션을 고른다. 동일 점수에서는 평가기처럼 첫 옵션을 유지한다. 이 설명을 위해 새 환경 trace를 실행하지 않았다.

| 조건 | Selection U | Test U | Nodes | Depth |
| --- | ---: | ---: | ---: | ---: |
| N_FLAT | 1.009734 | 1.008823 | 13 | 3 |
| N_ROLE | 1.009851 | 1.009589 | 13 | 3 |
| X_FLAT | 1.010947 | 1.009928 | 13 | 4 |
| X_ROLE | 1.009537 | 1.008923 | 11 | 3 |
| DOMAIN_V2 | 1.008601 | 1.008183 | 9 | 4 |

동일 도메인·블록의 원래 선택 정책 비교다. 사례를 고른 뒤 붙인 설명용 비교이며 일반적인 순위나 확증 검정이 아니다.

**판정과 한계**
X_FLAT 사례다. X_ROLE의 성과로 표기하지 않는다. 비교 X_ROLE은 11노드·깊이3이고 A4는 13노드·깊이4다. 계수 2를 산업디자인 원리의 결과라고 단정하지 않는다.

**후속 검토 판단 — 저자의 탐색적 판단**
힌트 조립의 대조 사례로 유지. 제공된 구조의 조립과 가중치 조정을 보여주며 새로운 도메인 연결이나 역할 효과의 증거로 쓰지 않는다.

**기준식:** `temp+0.4*soc+0.35*imped+0.25*stress`

**추적 경로 — 원자료 폴더 기준**
- Prompt: `data/prompts/pilot-Thermal-03-X_FLAT.json`
- Request and preceding answers/feedback: `data/requests/pilot-Thermal-03-X_FLAT-r3-a1.request.json`
- Response: `data/response-projection.jsonl`, line 295
- Selection/test: `data/selection.json` / `data/final.json`, session `pilot-Thermal-03-X_FLAT`, slot `pilot-Thermal-03-X_FLAT-slot9`

## A5. 범위를 좁힌 대기량–추세 곱 점수

`queue*(0.35+drift)-0.25*idle`

- **출처:** Network / X_ROLE / block 5 / round 4 / slot 10
- **ID:** `pilot-Network-05-X_ROLE-slot10`
- **선정 이유:** 고정 도메인 순서에서 중복을 제외한 X_ROLE 원래 선택 정책 중 selection utility 최소
- **기록된 구조:** 9 nodes, implemented depth 3; variable-product

**무엇을 하는 식인가 — 저자 해석**
queue에 drift에 따라 달라지는 가중치를 주고 idle을 뺀다. burst는 사용하지 않는다.

**입력과 출력의 차이**
H의 queue*(0.45+drift)에서 상수를 0.35로 바꾸고 음의 idle 항을 붙인 형태다. 미지의 구조 발견보다 주어진 틀의 변형에 가깝다.

> Common mathematical hints H: consider queue*(0.45+drift), max(burst-idle,0), and a negative idle term. These are optional engineering templates. All constants remain subject to the same grammar and complexity limits.

**같은 세션에서 관측된 변화**
아래 이전 출력과 feedback은 선택된 응답 직전 요청에 포함됐다. 최종 식과의 비교는 관측 가능한 수정 이력이며, 모델이 수정한 이유를 추정한 것이 아니다. 최초 도메인 관점은 프롬프트에 명시되었고 모델이 도메인 자체를 고른 것은 아니다.

- R3/S7: `queue*(0.4+drift)-0.3*idle` — `pilot-Network-05-X_ROLE-slot7`, response line 219
- 선정 식: `queue*(0.35+drift)-0.25*idle`

**활용 방법**
변수를 세 개만 사용하는 합성 큐 순위 규칙의 예다. 짧은 설명은 가능하지만 간결함만으로 유용성이 정해지지는 않는다.

모든 입력 특성은 음수를 0으로 자른 뒤 x/(1+x)로 정규화한다. 각 옵션의 점수를 계산하고 최대 점수 옵션을 고른다. 동일 점수에서는 평가기처럼 첫 옵션을 유지한다. 이 설명을 위해 새 환경 trace를 실행하지 않았다.

| 조건 | Selection U | Test U | Nodes | Depth |
| --- | ---: | ---: | ---: | ---: |
| N_FLAT | 0.998743 | 0.998685 | 9 | 2 |
| N_ROLE | 1.003469 | 1.003917 | 7 | 2 |
| X_FLAT | 1.001004 | 1.001018 | 11 | 3 |
| X_ROLE | 1.001418 | 1.002104 | 9 | 3 |
| DOMAIN_V2 | 1.003553 | 1.004020 | 11 | 2 |

동일 도메인·블록의 원래 선택 정책 비교다. 사례를 고른 뒤 붙인 설명용 비교이며 일반적인 순위나 확증 검정이 아니다.

**판정과 한계**
규칙상 Network X_ROLE 원래 선택 정책 중 선택 점수가 낮은 사례로 골랐다. 시험에서는 기준을 넘지만 같은 블록의 더 단순한 N_ROLE보다 낮다. 구문 실패나 시험 실패로 부르면 안 된다.

**후속 검토 판단 — 저자의 탐색적 판단**
후속 후보에서는 우선순위를 낮춘다. 같은 블록의 N_ROLE 식이 더 단순하고 저장 시험 점수도 높다. 기준식 초과만으로 채택하지 않는다.

**기준식:** `queue+0.45*drift+0.15*burst-0.15*idle`

**추적 경로 — 원자료 폴더 기준**
- Prompt: `data/prompts/pilot-Network-05-X_ROLE.json`
- Request and preceding answers/feedback: `data/requests/pilot-Network-05-X_ROLE-r4-a1.request.json`
- Response: `data/response-projection.jsonl`, line 220
- Selection/test: `data/selection.json` / `data/final.json`, session `pilot-Network-05-X_ROLE`, slot `pilot-Network-05-X_ROLE-slot10`

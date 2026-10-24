# Cross-Domain Skill Composition for LLM Policy Search

**An exploratory pilot of combining biological/HCI relationship exploration with minimalist-design simplicity guidance.** Public paper and supplementary evidence for reviewers.

## Start here

| What you need | Open |
| --- | --- |
| Read the revised paper (7 pages) | [Paper PDF](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/paper.pdf) |
| Inspect data, prompts and verification code | [Public supplement ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/public-supplement-v1.0.0.zip) |
| Edit or rebuild the paper | [Manuscript source ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/manuscript-source-v1.1.0.zip) |
| Check file integrity and release notes | [Version 1.1.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.1.0) · [SHA-256 checksums](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/SHA256SUMS.txt) |
| Inspect the previous paper | [Version 1.0.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.0.0) |

The revised PDF contains 5 pages of main text, 1 page of references, and a 1-page summary. Release v1.1.0 restores the original skill-composition motivation and clarifies what the pilot tested. Numerical results and evidence are unchanged: the evidence archive is byte-identical to v1.0.0 and retains its original filename.

All evidence files are in the release assets; GitHub's automatically generated source archives contain only the repository landing files.

## What does “skill composition” mean here?

The idea pairs two instruction functions: biological and human-computer interaction (HCI) analogies encourage exploration of relationships; minimalist industrial-design guidance encourages simpler expressions. In this pilot, a **skill is a textual instruction module within a shared prompt**. Separate skill files, independent agents, and a structural-isomorphism compiler were not executed.

All four factorial conditions contain exploration and simplicity guidance. The experiment varies cross-domain versus neutral framing and combined versus role-organized wording under shared mathematical hints. It therefore does **not** compare the presence versus absence of the modules or isolate their individual contributions or synergy.

## What was observed?

Three synthetic tasks × six paired blocks × five prompt conditions produced 90 sessions, 360 responses, and 1,080 valid expressions.

- **Primary framing difference: −0.11** near-reference behavioral components per session (X_ROLE minus N_ROLE). Domain directions differ, with substantial block variation.
- **Auxiliary organization difference: −0.56** (X_ROLE minus X_FLAT).
- **Secondary strict-exceedance framing difference: +0.33.** Changing the performance threshold changes the interpretation.
- **Cloud: 126 near-reference passes, 8 strict exceedances**, among 304 session-level representative instances. These are not globally unique policies.

![All 18 paired block differences and domain means](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/paired_differences.png)

![Cloud representatives by test utility threshold](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.1.0/cloud_thresholds.png)

These observations do not establish a consistent benefit from the tested composition, prompt equivalence, a general failure of cross-domain skill composition, or superiority over published search methods. There was one requested model and one wording per condition, with six paired blocks per domain and handcrafted environments. Additional controls and independent replications are needed to assess module contributions and generalization.

## Verify without model calls

Download and unzip the public supplement. From its root, using Node.js 22 or later:

```sh
node tools/verify-public.cjs
```

Expected: `valid: true`, 90 sessions, 360 responses, 1,080 slots, 15 distinct prompt texts, and primary contrast `-0.11111111111111112`.

This reads saved records and reaggregates results. It does not call a model, run an environment, or rerun statistical simulations. The archive's README explains each file and the distinction between public hashes and the original private journal seal. Local machine paths and CLI identifiers were removed from metadata and response projections; original selection, final outcomes and experimental requests are preserved. Exact server snapshots and sampling seeds were unavailable, so regenerating identical model outputs is not claimed.

## Reading guide (한국어)

이 연구의 주제는 **생물학·HCI의 관계 탐색 지침과 미니멀 디자인의 단순화 지침을 결합하는 이종 도메인 스킬 결합**입니다. 현재 파일럿은 이를 한 프롬프트 안의 지시 모듈로 구현해 시험했습니다. 결합의 효과나 개별 모듈의 기여를 입증한 연구로 주장하지 않습니다.

1. 초록·서론에서 결합하려는 두 지침과 연구 질문을 확인합니다.
2. 2.1절에서 원래 아이디어와 실제로 실행한 프롬프트의 범위를 구분합니다.
3. 결과의 그림 1에서 블록별 변동을, 그림 2에서 기준 성능 근접과 실제 초과의 차이를 확인합니다.
4. 마지막 요약 쪽에서 기여·결과·한계를 함께 읽습니다.
5. 세부 검증이 필요하면 보충자료 ZIP의 `README.md`와 `docs/PROMPT_PROTOCOL.md`를 읽습니다.

No new experimental model calls were made for this revision. This repository is a research artifact release, not a claim of conference acceptance.

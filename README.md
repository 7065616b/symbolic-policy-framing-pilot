# Testing Cross-Domain Framing in LLM Policy Search

**A 90-session exploratory pilot.** Public paper and supplementary evidence for reviewers.

## Start here

| What you need | Open |
| --- | --- |
| Read the paper (6 pages) | [Paper PDF](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/paper.pdf) |
| Inspect data, prompts and verification code | [Public supplement ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/public-supplement-v1.0.0.zip) |
| Edit or rebuild the paper | [Manuscript source ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/manuscript-source-v1.0.0.zip) |
| Check file integrity and release notes | [Version 1.0.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.0.0) · [SHA-256 checksums](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/SHA256SUMS.txt) |

The PDF contains 4 pages of main text, 1 page of references, and a 1-page summary. All evidence files are in the release assets; GitHub's automatically generated source archives contain only the repository landing files.

## What was observed?

Three synthetic tasks × six paired blocks × five prompt conditions produced 90 sessions and 1,080 valid expressions. The primary comparison tests cross-domain versus neutral wording with the same mathematical hints and within-response role instructions.

- **Primary difference: −0.11** near-reference behavioral components per session (X_ROLE minus N_ROLE). Domain directions differ, with substantial block variation.
- **Secondary strict-exceedance difference: +0.33.** Changing the performance threshold changes the interpretation.
- **Cloud: 126 near-reference passes, 8 strict exceedances**, among 304 session-level representative instances. These are not globally unique policies.

![All 18 paired block differences and domain means](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/paired_differences.png)

![Cloud representatives by test utility threshold](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.0.0/cloud_thresholds.png)

These descriptive observations do not establish prompt equivalence, a general absence of analogical benefit, or superiority over published search methods. There was one requested model and one wording per condition, with six paired blocks per domain and handcrafted environments.

## Verify without model calls

Download and unzip the public supplement. From its root, using Node.js 22 or later:

```sh
node tools/verify-public.cjs
```

Expected: `valid: true`, 90 sessions, 360 responses, 1,080 slots, 15 distinct prompt texts, and primary contrast `-0.11111111111111112`.

This reads saved records and reaggregates results. It does not call a model, run an environment, or rerun statistical simulations. The archive's README explains each file and the distinction between public hashes and the original private journal seal. Local machine paths and CLI identifiers were removed from metadata and response projections; original selection, final outcomes and experimental requests are preserved. Exact server snapshots and sampling seeds were unavailable, so regenerating identical model outputs is not claimed.

## Reading guide (한국어)

1. 논문 1쪽에서 질문과 핵심 결과를 확인합니다.
2. 3쪽의 그림 1에서 블록별 변동을, 그림 2에서 기준 성능 근접과 실제 초과의 차이를 확인합니다.
3. 세부 검증이 필요하면 보충자료 ZIP의 `README.md`와 `docs/PROMPT_PROTOCOL.md`를 읽습니다.

No new experimental model calls were made to prepare this release. This repository is a research artifact release, not a claim of conference acceptance.

# Cross-Domain Skill Composition for LLM Policy Search

**An exploratory pilot of combining biological/HCI relationship exploration with minimalist-design simplicity guidance.** Public paper and evidence for reviewers.

## Start here

| What you need | Open |
| --- | --- |
| Read the revised paper (8 pages) | [Paper PDF](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/paper.pdf) |
| Compare exact prompts and inspect the new output profiles | [Analysis addendum ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/composition-analysis-v1.2.0.zip) |
| Inspect original data, requests and verification code | [Unchanged evidence ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/public-supplement-v1.0.0.zip) |
| Edit or rebuild the paper | [Manuscript source ZIP](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/manuscript-source-v1.2.0.zip) |
| Check integrity and release notes | [Version 1.2.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.2.0) · [SHA-256 checksums](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/SHA256SUMS.txt) |
| Inspect earlier papers | [Version 1.1.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.1.0) · [Version 1.0.0](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/tag/v1.0.0) |

The PDF contains 6 pages of main text, 1 reference page and a 1-page summary. Version 1.2.0 adds a verbatim prompt comparison and retrospective complexity, diversity and selected-policy performance profiles. **The original primary result and evidence are unchanged.** The evidence archive is byte-identical to v1.0.0 and retains its original filename. The new analysis is a separate addendum.

Research files are in the release assets. GitHub's automatically generated source archives contain only the repository landing files.

## What does “skill composition” mean here?

The idea pairs two instruction functions: biological and human-computer interaction (HCI) analogies encourage exploration of relationships; minimalist industrial-design guidance encourages simpler expressions. Here a **skill is a textual instruction module within a shared prompt**. Separate skill files, independent agents and a structural-isomorphism compiler were not executed.

All four factorial conditions contain exploration and simplicity guidance. The experiment varies cross-domain versus neutral framing and combined versus role-organized wording under shared mathematical hints. It does not isolate the modules' individual contributions or synergy. DOMAIN_V2 omits the hints and changes guidance, so it is descriptive.

## What was observed?

Three synthetic tasks × six paired blocks × five conditions produced 90 sessions, 360 responses and 1,080 valid expressions.

- **Original primary framing difference: −0.11** near-reference behavioral components per session (X_ROLE minus N_ROLE), with mixed domain directions and substantial block variation.
- **Auxiliary organization difference: −0.56** (X_ROLE minus X_FLAT).
- **Secondary strict-exceedance framing difference: +0.33.** This answers a different question from the primary near-reference count.
- **Cloud: 126 near-reference passes and 8 strict exceedances** among 304 session-level representative instances. These are not globally unique policies.

The new retrospective profiles are:

| Within-block comparison, averaged equally across domains | Mean nodes | Pre-threshold behavioral components | Originally selected policy test utility |
| --- | ---: | ---: | ---: |
| X_ROLE minus N_ROLE | +0.5370 | −0.3889 | +0.000998 |
| X_ROLE minus X_FLAT | +0.8148 | −0.4444 | −0.000144 |

X_ROLE has larger aggregate expressions and fewer pre-threshold components than both controls. Its small utility difference is positive against N_ROLE and negative against X_FLAT. The size increase is mainly in Thermal; domain directions differ. These metrics have different units and are not a single improvement score. The utility difference is not a relative percentage gain.

![All 90 session profiles by domain and condition](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/composition_profiles.png)

Each panel contains 30 sessions; the same sessions appear in both rows. Mean nodes include all 12 submitted expressions per session. Components are saved selection-stage groups before a utility threshold. Test utility belongs to the policy originally chosen on selection data. No new winner was selected using test outcomes. These are descriptive joint profiles, not estimates of a complexity effect.

![Original 18 paired block differences and domain means](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/paired_differences.png)

![Cloud representatives by test utility threshold](https://github.com/7065616b/symbolic-policy-framing-pilot/releases/download/v1.2.0/cloud_thresholds.png)

The pilot does not establish a consistent composition benefit, prompt equivalence, a general failure of cross-domain skill composition or superiority over published search methods. It uses one requested model and one wording per condition, six paired blocks per domain, shared hints and handcrafted environments. Actual token use was not exactly matched. The new analyses are post hoc and do not identify a module mechanism; no new inferential tests or uncertainty intervals are claimed.

## Verify without model calls

Extract the unchanged evidence ZIP into `public_supplement`. From that directory, using Node.js 22 or later:

```sh
node tools/verify-public.cjs
```

Expected: `valid: true`, 90 sessions, 360 responses, 1,080 slots, 15 distinct prompt texts and primary contrast `-0.11111111111111112`.

Extract the new addendum into a sibling `composition_analysis_v1.2.0` directory. From that directory, using Python 3.12 or later:

```sh
python -m unittest -v test_analysis.py
python analysis.py --evidence ../public_supplement
python prompt_build_comparison.py --evidence ../public_supplement --output .
python independent_check.py --evidence ../public_supplement
```

Expected: six passing tests, 90 sessions, 1,080 slots, 15 exact prompt texts and `AUDIT PASS`. `README.md` explains the metrics and optional plotting; `tables.md` reports all domains/conditions; `REPORT_KO.md` explains the results in Korean. Each archive has its own file-hash manifest.

These commands read saved records and reaggregate results. They do not call a research model, run an environment or rerun statistical simulations. Public response/metadata projections remove local paths and CLI identifiers; original requests, selection and final outcomes are preserved. Public hashes do not verify the original private journal seal. Exact server snapshots and sampling seeds were unavailable, so regenerating identical model responses is not claimed.

## Reading guide (한국어)

연구 주제는 **생물학·HCI의 관계 탐색 지침과 미니멀 디자인의 단순화 지침을 결합하는 이종 도메인 스킬 결합**입니다. 이를 한 프롬프트 안의 지시 모듈로 구현한 파일럿이며, 결합의 효과나 개별 모듈의 기여를 입증했다고 주장하지 않습니다.

1. 표 2에서 실제로 달라진 지시문을 비교합니다. 전체 문장과 공통 지침은 분석 묶음의 `prompt_comparison.md`에 있습니다.
2. 표 6과 그림 2에서 복잡도·다양성·성능을 함께 봅니다. X_ROLE의 전반적 우위는 관찰되지 않았으며 도메인별 차이가 있습니다.
3. 그림 1은 기존 주지표의 블록별 변동, 그림 3은 Cloud의 근접 성능과 엄격 초과의 차이입니다.
4. 마지막 요약 쪽에서 기여와 한계를 확인합니다. 숫자를 자세히 검토하려면 분석 묶음의 `REPORT_KO.md`, `tables.md`, `sessions.csv`를 읽습니다.

No new experimental model calls were made for this revision. This is a research artifact release, not a claim of conference acceptance.

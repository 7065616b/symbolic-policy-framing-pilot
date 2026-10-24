# Cross-Domain Skill Composition: Minimum Coupling and Cubic Stress in Generated Policies

**Bogyun Kim**  
Department of Computer Engineering, Mokpo National University, Muan, Republic of Korea  
`s11s45@naver.com`

## Abstract

What makes a generated policy worth examining beyond its average score? We study artifacts from a recorded pilot combining biological/HCI exploration with minimalist-design guidance. Two outputs make this question concrete: a queue rule that couples drift and burst through their minimum, and a thermal rule that uses cubic stress. These structures are absent from the supplied mathematical hints, but also occur in neutral conditions. In saved paired tests, the queue case exceeds its matched neutral policy on 402 of 600 traces with fewer syntax nodes; the thermal case exceeds a simpler cross-domain alternative on 390 traces while using more nodes. A third case illustrates rejection: an above-reference rule loses to a simpler neutral alternative. The complete catalogue retains 1,080 submissions and five fixed retrospective cases. The original aggregate primary contrast remains negative and domain-dependent. The contribution is a reproducible account of candidate behavior, input overlap and adoption tradeoffs, not evidence of cross-domain causation or real-world utility.

**Keywords:** Cross-domain skill composition, generated artifacts, symbolic policies, exploratory evaluation.

## 1. Introduction and Related Work

An interesting generated rule should be something a reader can inspect, explain and compare with an alternative. Our motivating question is whether combining perspectives from unrelated domains can help an LLM produce such rules. We combine biological immune-adaptation and human-computer interaction (HCI) reframing with minimalist industrial-design guidance. The source domains are named by the prompt; the model chooses expressions within a supplied grammar, task facts, mathematical hints H and feedback. Here skill composition means textual guidance in one prompt, not independently executed agents or unconstrained discovery of source domains.

Consider `queue+min(drift,burst)-0.5*idle`. Its minimum term rewards the joint presence of two signals: a large value of one cannot compensate for a small value of the other. A second output, `temp+(0.5*(soc*imped)+stress*stress*stress)`, suppresses the contribution of low stress relative to high stress. These are recognizable decision rules rather than abstract improvements in an output count. They are the focus of this paper because their behavior can be explained and their tradeoffs examined.

We ask what these artifacts do, whether their saved results justify further examination, and how much of their structure was already supplied. A1 and A2 receive editorial emphasis among the five cases fixed in v1.3; this is not a new selection rule. A5 shows why exceeding a simple reference is insufficient for adoption. The other cases, the full catalogue and the original unfavorable aggregate result remain visible.

LLM-driven executable search has precedents in FunSearch [1], Evolution of Heuristics [2] and ReEvo [3]. Analogical prompting [10] and cross-domain scientific search [7] motivate source perspectives; CreativeDC [6] combines divergent and convergent instructions. HSEvo [4], Language Model Crossover [5] and MAP-Elites [9] address diversity alongside quality; persona effects are task-dependent [8]. Our contribution is a traceable case study of generated structures and decisions about their value, not a new search or analogy algorithm. An older 414-expression corpus is excluded because its generation requests are unavailable.

## 2. Two Candidate Structures and an Adoption Counterexample

### 2.1 A1: Require Two Signals Together

A1 scores synthetic queues as `queue+min(drift,burst)-0.5*idle`. A low drift or low burst limits the added priority. This exact coupling is absent from H, which instead supplies `queue*(0.45+drift)`, `max(burst-idle,0)` and a negative idle term. The observable difference is a new combination relative to those hints, not mathematical novelty or a demonstrated biological mechanism.

The rule can change a decision in an intelligible way. Take two invented normalized queues with queue=0.6 and idle=0.1. P has drift=0.8 and burst=0.1; Q has drift=0.5 and burst=0.5. A1 scores them 0.65 and 1.05, selecting Q. The reference scores them 0.960 and 0.885, selecting P. This illustrates a preference for both signals being present; it does not establish that Q is the better real-world choice.

The saved evidence supplies a separate reason to examine A1. In the same block it uses nine syntax nodes versus 13 for the N_ROLE winner, with test utility 1.003905 versus 1.000870. It has higher reward on 402 of their 600 paired traces and lower reward on 198. Thus this fixed case combines an inspectable rule, smaller syntax and a favorable saved comparison. Syntax size is not measured runtime, and these results are specific to the selected case and synthetic task.

The record also shows how the expression changed. In round 2, slot 6, the model had already produced `queue+min(drift,burst)-0.25*idle`. A1 is the round-3 variant with coefficient -0.5, after that output and its feedback were supplied. This is an observed revision, not a reconstruction of the model's reasoning.

![Behavior of the two emphasized structures](interesting_structures.png)

*Figure 1. Mathematical illustrations, not new environment observations. Left: the contribution min(drift,burst) is large only when both signals are large. Right: on [0,1], cubic stress downweights low stress relative to high stress. The straight line is a shape reference, not a tested full-policy comparator. Whole-policy saved comparisons are in Table 2.*

### 2.2 A2: Spend Complexity Only When the Added Term Helps

A2 scores synthetic modules for derating using temperature, half the supplied soc*imped interaction and cubic stress. At stress 0.2 the cubic contribution is 0.008; at 0.8 it is 0.512. On [0,1], cubing decreases the value except at the endpoints; the interesting property is the changed response shape, not amplification above the original stress value. H supplies a positive-part threshold `max(stress-0.5,0)`, rather than a cubic term.

A2's test utility is 1.011170. However, the matched X_FLAT winner `temp+stress*stress*stress` achieves 1.009897 with seven nodes instead of 13. A2 wins on 390 of 600 paired traces and loses on 210. The remaining question is whether this small saved reward increment warrants the extra interaction and nodes. The paper does not assume that the larger expression should be adopted, or that a simpler expression executes faster.

Within the session, `temp+(soc*imped+stress*stress*stress)` first appears in round 3, slot 9. The round-4 A2 halves the product coefficient after that output and its feedback are supplied. The cubic structure also appears in neutral and X_FLAT sessions (Section 3.2), so its appearance cannot be attributed uniquely to the cross-domain roles. Battery safety and physical thermal behavior were not tested.

### 2.3 A5: Above Reference Does Not Mean Worth Adopting

A5, `queue*(0.35+drift)-0.25*idle`, changes the coefficients of a supplied template and omits burst. Its test utility is 1.002104, above the simple reference. Yet the same-block N_ROLE policy `queue+drift-0.5*idle` reaches 1.003917 with seven nodes/depth 2 versus A5's nine nodes/depth 3. A5 wins 270 paired traces, ties two and loses 328 against that alternative. This makes it a useful counterexample to equating reference exceedance with an adoption recommendation.

A5 was fixed by the low-selection rule, not selected for a poor test outcome. The preceding round already contains `queue*(0.4+drift)-0.3*idle`; A5 changes its coefficients after feedback. It is a valid, above-reference output, not a failed generation. Our author judgment is to deprioritize it relative to the simpler matched alternative.

### 2.4 The Other Cases and the Final Judgment

A3, the Cloud case in Table 1, adjusts idle with an upper-capped frequency term and positive jitter. For freq below 0.5, subtracting the negative min term adds a bonus; at freq at least 0.75 the frequency contribution is fixed at -0.0875. This cap and jitter were supplied in H. Earlier rounds use cap weights 1 and 0.6; A3 uses 0.35. Its test utility is only 1.000466, and depth 4 exceeds the soft target of 3. We retain it as a low-priority diagnostic, not evidence of cloud-cost savings.

A4 combines the supplied temperature, soc*imped and threshold terms, with weight two on the threshold. The preceding round contains both the doubled threshold without the product and the product with weight one. Its test utility is 1.009928, versus 1.008923 for the matched X_ROLE winner, at 13 nodes/depth 4 versus 11/depth 3. We retain A4 as an assembly/control example; it is an X_FLAT output, not an X_ROLE success or a newly discovered domain connection.

| Case | Exact submitted expression | Author judgment and reason |
| --- | --- | --- |
| A1 | `queue+min(drift,burst)-0.5*idle` | Examine first: inspectable coupling; smaller and higher-scoring than matched N_ROLE |
| A2 | `temp+(0.5*(soc*imped)+stress*stress*stress)` | Compare with simpler cubic rule: small reward increment costs six nodes |
| A3 | `idle-0.35*min(freq-0.5,0.25)+0.2*jitter` | Low priority: supplied cap; tiny reference margin |
| A4 | `temp+soc*imped+2*max(stress-0.5,0)` | Assembly/control: supplied terms; no new source connection established |
| A5 | `queue*(0.35+drift)-0.25*idle` | Deprioritize: simpler matched neutral alternative scores higher |

*Table 1. All five fixed cases remain visible. Judgments combine behavior, input overlap, saved reward and syntax cost; they are exploratory author decisions, not validated usefulness ratings. A1/A2/A3/A5 are X_ROLE; A4 is X_FLAT. Full provenance and selection utilities are in the unchanged case cards.*

## 3. What the Saved Records Add

### 3.1 Paired Rewards Make the Tradeoffs Concrete

We join the saved test records by identical seed within the same task and block. Each row of Table 2 compares two fixed policies on the same 600 traces. A win means the raw-reward difference is greater than 1e-12; differences within that tolerance are ties. The mean margin is the mean of paired raw-reward differences, not a percentage or a normalized utility difference. Its scale is task-specific and must not be compared across tasks. All five conditions' matched winners, medians, lower-tail differences and worst observed differences are included in the new saved-data supplement.

| Case | Comparator | Wins/ties/losses | Mean raw margin |
| --- | --- | --- | ---: |
| A1 | Reference | 514/0/86 | +0.003800 |
| A1 | N_ROLE | 402/0/198 | +0.002953 |
| A2 | Reference | 599/0/1 | +0.014354 |
| A2 | X_FLAT | 390/0/210 | +0.001635 |
| A3 | Reference | 359/0/241 | +0.000412 |
| A4 | Reference | 599/0/1 | +0.012758 |
| A5 | N_ROLE | 270/2/328 | -0.001764 |

*Table 2. Descriptive paired comparisons from already stored test rewards. N_ROLE/X_FLAT are original winners of the same domain/block, not newly selected comparators. The supplement reports all matched conditions to avoid limiting inspection to favorable rows. Six hundred traces describe variation for a fixed policy, not 600 independent model generations or a prospective validation of the selected examples.*

The evidence supports different decisions. A1 warrants follow-up under this simulator. A2 requires a complexity tradeoff judgment. A3's small average edge comes with losses on 241 traces. A4 shows that useful-looking assembly need not be a new connection. A5 shows why a stronger alternative matters. None of these observations establishes a minimum practically important improvement or real deployment benefit.

### 3.2 Interesting Structures Are Not Exclusive to Cross-Domain Roles

We also audit two explicitly defined motifs throughout the complete saved catalogue. After removing whitespace, we search for the exact substrings `min(drift,burst)` in Network and `stress*stress*stress` in Thermal. This is a narrow, reproducible string census, not semantic clustering or an exhaustive search for algebraically equivalent rules. Counts are retrospective and were chosen because of A1/A2.

The minimum motif appears in four X_ROLE submissions from one session, one N_ROLE submission from one session and one X_FLAT submission from one session. It is absent under this literal rule in N_FLAT and DOMAIN_V2. The cubic motif appears in seven X_FLAT submissions from five sessions, three N_FLAT submissions from one session and two X_ROLE submissions from one session; it is absent under the rule in N_ROLE and DOMAIN_V2. Each task/condition has six sessions and 72 submissions. Repeated submissions from a session are not independent discoveries.

These records sharpen the main distinction: a structure can be absent from H, interpretable and promising in a selected comparison without being specific to the cross-domain package. The minimum and cubic motifs are not evidence that biological, HCI or design knowledge caused the corresponding terms. Their neutral-condition occurrence is part of the finding, not an example to omit.

### 3.3 Complete Collection and Retrospective Selection

All 1,080 submissions pass the recorded validity gate. Within domains there are 822 distinct exact expression strings; spacing and algebraic variants remain separate. We retain every occurrence, including repeats, with its session, condition, block, round, slot, exact prompt, prior-answer/feedback request, and response line. The catalogue also records nodes/depth, original selection status, behavioral component, and saved scores. There are 916 component representative instances and 90 original session winners. Test outcomes exist for 944 submissions; the other 136 remain untested, not zero-scoring failures.

The offline catalogue supports expression search and domain, condition, test-availability and original-selection filters. Syntactic tags identify variable-bearing products, min/max, abs, division, or additive-affine forms. They help locate examples but do not establish semantic novelty or a cognitive process. The input comparison keeps the exact H beside each case so that supplied building blocks are not credited as discoveries.

We fix three core cases: the original X_ROLE session winner with highest selection utility in each domain. Ties use nodes, depth, session ID and slot ID in ascending order. One X_FLAT complement is selected from original winners with a tag combination absent from the core cases, using Network-Thermal-Cloud domain order and the same ranking within the first eligible domain. One low-selection X_ROLE example uses that domain order, minimum selection utility, and the same tie rules after excluding already used domain/expression pairs. A missing eligible complement would be omitted.

The selection function receives only selection/provenance/syntax fields. It writes case IDs and a rule hash before attaching test values, without replacing cases after attachment. Nevertheless, the rule was devised after pilot results had been inspected: these are **post-hoc descriptive cases, not five prevalidated successes or the global best five outputs**. Matched comparison rows are the original winners of all five conditions in the same domain/block. Full inclusion/exclusion logs are public.

## 4. Inputs, Generation, and Evaluation

### 4.1 Source Perspectives and Target Tasks

The source perspectives and target tasks play different roles. Biological/HCI and design language supplies guidance; Network, Thermal, and Cloud are the tasks receiving generated rules. Network ranks four synthetic queues, Thermal ranks four synthetic modules for derating, and Cloud ranks six synthetic slots for reclamation. In each task, the expression assigns scores to options and the highest score determines the selected option. Features are normalized to [0,1] by clipping negative raw values at zero and applying x/(1+x). Ties retain the first option.

Expressions use four task variables, constants, arithmetic, min, max, and abs. All conditions share a hard gate of 25 AST nodes and implemented depth 5, with soft targets of 14 nodes and depth 3. Recorded depth flattens additive/subtractive and multiplication chains; it is not ordinary binary-tree height. Nodes and depth describe syntax, not measured runtime or memory efficiency. Each environment trace has 320 steps, with handcrafted transitions and rewards; task names do not imply validated physical or production systems.

The four factorial conditions share the hints in Table 4. The cross-domain instruction asks the model to interpret them through biological immune-adaptation and HCI reframing analogies, using minimalist industrial-design inspiration for concise expressions. ROLE assigns exploration and simplicity distinct functions within the same response; FLAT presents both together. These are prompt instructions, not observed internal stages. DOMAIN_V2 omits H and changes the guidance procedure, so it is descriptive rather than a single-module ablation.

| Condition | Framing | Organization | H |
| --- | --- | --- | --- |
| N_FLAT | Neutral | Combined | Yes |
| N_ROLE | Neutral | Roles | Yes |
| X_FLAT | Cross-domain | Combined | Yes |
| X_ROLE | Cross-domain | Roles | Yes |
| DOMAIN_V2 | Domain | Base | No |

*Table 3. Conditions. Every factorial arm includes exploration and simplicity guidance. Roles are textual within one response.*

| Task | Shared mathematical hints H |
| --- | --- |
| Network | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle term |
| Thermal | `soc*imped`; `max(stress-0.5,0)`; temperature term |
| Cloud | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle |

*Table 4. H is supplied to all four factorial conditions within a task. The Cloud min term is an upper cap, not a lower clamp. Exact complete prompts and their verbatim differences are public.*

### 4.2 Recorded Generation and Evaluation

The pilot ran on 24 October 2026 (KST), requesting gpt-6.1-sol with low reasoning effort through Codex CLI 0.162.1. Three domains, six paired blocks per domain, and five conditions give 90 separately initialized sessions. Randomized condition order within domain/block and four rounds of three expressions yield 360 responses and 1,080 slots. Each session receives only its own prior answers and feedback. The required response is an expression array without explanatory commentary, so the record does not reveal the model's internal rationale.

The experimental message roles were serialized into one CLI input rather than sent as native API roles. Actual prompt length, semantics, and token use were not exactly matched; the requested 2,048-token output cap was not enforced. Thus the contrasts concern the recorded instruction packages, not perfectly resource-matched interventions or verified server snapshots.

Feedback, selection and test use disjoint base seeds: 48 (1000001-1000048), 96 (1100001-1100096), and 600 (1200001-1200600), with fixed Thermal/Cloud offsets. Selection starts after generation, and selected policies and representatives are frozen before test access. The generation unit is a session, not one of its 12 dependent submissions or its simulator traces.

The reference expressions are queue+0.45*drift+0.15*burst-0.15*idle for Network, temp+0.4*soc+0.35*imped+0.25*stress for Thermal, and idle for Cloud. Historical labels Adaptive-PI, PID-lite, and Fixed-TTL denote simplified synthetic formulas, not full implementations of those methods. Utility U is the policy's mean trace reward divided by the reference's mean reward on the same domain/split; the reference has U=1. This ratio is not an average of per-trace ratios. References are comparison points, not optima or tuned published competitors.

Behavioral groups use the saved graph on a fixed four-value-per-coordinate grid and 500 diagnostic option panels. An edge requires Spearman score correlation above 0.98 and top-action agreement of at least 95 percent. Connected components may contain transitive chains; they are finite-probe groups within a session, not globally unique ideas. Each representative and the overall session winner are chosen by selection mean reward, with expression-hash and slot tie breaks, then evaluated on test. The original primary outcome counts representatives with U at least 0.99. This near-reference criterion permits below-reference policies and is not a practical improvement threshold. Strict exceedance uses U greater than 1+1e-9. The analysis was locally frozen before test access, not publicly preregistered.

## 5. Aggregate Evidence and Boundaries

Selected examples do not replace the original experiment. Equal-domain averaging of six within-block contrasts gives -0.1111 near-reference components per session for X_ROLE minus N_ROLE. The Network, Thermal and Cloud means are -0.6667, +0.1667 and +0.1667, with paired SDs 2.9439, 2.2286 and 4.4907. Figure 2 retains all 18 differences. Six paired blocks per domain are the generation comparisons; test traces do not enlarge that sample.

![Original paired near-reference differences](paired_differences.png)

*Figure 2. Original X_ROLE minus N_ROLE near-reference counts by block and domain. Selected artifact examples must be read alongside this mixed aggregate result.*

| Outcome | X_ROLE−N_ROLE | X_ROLE−X_FLAT | Interaction |
| --- | ---: | ---: | ---: |
| Primary count | −0.1111 | −0.5556 | −1.2222 |
| Strict-exceedance count | +0.3333 | +0.6667 | +0.3889 |
| All-pairs count | −0.0556 | −0.4444 | −1.1111 |
| Selected-policy utility | +0.000998 | −0.000144 | +0.000062 |

*Table 5. Preserved aggregate comparisons. Interaction is (X_ROLE−X_FLAT)−(N_ROLE−N_FLAT). Counts and utility answer different questions. The utility contrast is not a relative percentage gain.*

The v1.2 retrospective profiles also remain relevant. Relative to N_ROLE, X_ROLE has 0.5370 more mean nodes and 0.3889 fewer pre-threshold components per session; relative to X_FLAT, the differences are +0.8148 and -0.4444. The node difference is mainly Thermal (+1.5556), with Network -0.1667 and Cloud +0.2222. All 12 submissions contribute to session means, including repeats. These profiles do not support an aggregate simplicity-diversity advantage and do not identify a compression process. Full tables and figures remain in the supplement.

Cloud further separates usable-looking artifacts from broad performance claims. Of 304 representative instances, 178 are below 0.99, 118 lie from 0.99 through 1, and eight strictly exceed 1+1e-9, between 1.000012 and 1.000541. Thus 126 meet the near-reference threshold, but only eight exceed the reference; 25 of 30 originally selected Cloud policies are below it. No representatives cross either threshold between saved selection and test splits. This does not rule out selection bias or explain the source of the generated rules.

The study has one requested model/effort, one wording per condition, shared H overlapping reward features, handcrafted tasks and simple references. All factorial arms already contain both guidance functions; there are no exploration-only, design-only or bare-length controls. Actual token budgets were not matched. Finite-probe components and syntax tags are operational descriptions. The retrospective case rule favors particular selection outcomes and is not representative sampling. No pilot p-values, confidence intervals, equivalence decisions, user ratings, deployment studies, or new environment evaluations are added.

Accordingly, the catalogue supports inspection of outputs and selection decisions. It does not show which source-domain knowledge the model used, whether roles were internally executed, or whether cross-domain prompting caused the displayed structures. Input overlap is a necessary caution when interpreting autonomous combination. Future evidence for that broader claim would require controls that separate supplied templates from source perspectives and independently specified replication; such evidence is not manufactured by reinterpreting these saved cases.

## 6. Conclusion and Reproduction

The most informative outputs of this pilot are concrete decision rules. A1 couples two queue signals through a minimum and offers a favorable saved size/reward comparison. A2 changes the stress-response shape, but a simpler cubic alternative makes the added complexity debatable. A5 demonstrates that exceeding a simple reference does not make an output the preferred choice. A3 and A4 document the substantial reuse of supplied templates.

The resulting contribution is a case-based account of behavior and adoption tradeoffs with complete provenance. The two emphasized motifs also occur in neutral conditions, and the original aggregate comparison does not support cross-domain superiority. Interesting artifacts, hint-absent structure and causal benefit are separate claims. These saved data support inspection and prioritization for further study; practical utility and the source of the structures remain unresolved.

The public repository links the v1.4.0 paper, source and new saved-data analysis: [https://github.com/7065616b/symbolic-policy-framing-pilot](https://github.com/7065616b/symbolic-policy-framing-pilot). Begin with the case highlights, then the complete offline catalogue and bilingual v1.3 case cards. Original evidence, selection records and earlier analyses remain unchanged. Reproduction uses saved data without model or environment execution. Source hashes establish file identity, not identical model-output regeneration; server snapshots and sampling seeds are unavailable. Public projections do not verify the private journal seal. This revision adds no research model calls, environment traces or statistical simulations.

## References

- **[1]** B. Romera-Paredes, M. Barekatain, A. Novikov, M. Balog, M. P. Kumar, E. Dupont, F. J. R. Ruiz, J. S. Ellenberg, P. Wang, O. Fawzi, P. Kohli, and A. Fawzi, "Mathematical Discoveries from Program Search with Large Language Models," *Nature*, vol. 625, pp. 468–475, 2024.
- **[2]** F. Liu, X. Tong, M. Yuan, X. Lin, F. Luo, Z. Wang, Z. Lu, and Q. Zhang, "Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model," in *Proc. Int. Conf. Machine Learning (ICML)*, 2024.
- **[3]** H. Ye, J. Wang, Z. Cao, F. Berto, C. Hua, H. Kim, J. Park, and G. Song, "ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution," in *Advances in Neural Information Processing Systems*, vol. 37, 2024. [Proceedings](https://papers.nips.cc/paper_files/paper/2024/hash/4ced59d480e07d290b6f29fc8798f195-Abstract-Conference.html).
- **[4]** P. V. T. Dat, L. Doan, and H. T. T. Binh, "HSEvo: Elevating Automatic Heuristic Design with Diversity-Driven Harmony Search and Genetic Algorithm Using LLMs," in *Proc. AAAI Conf. Artificial Intelligence*, vol. 39, no. 25, pp. 26931–26938, 2025. [doi:10.1609/aaai.v39i25.34898](https://doi.org/10.1609/aaai.v39i25.34898).
- **[5]** E. Meyerson, M. J. Nelson, H. Bradley, A. Gaier, A. Moradi, A. K. Hoover, and J. Lehman, "Language Model Crossover: Variation through Few-Shot Prompting," *ACM Transactions on Evolutionary Learning and Optimization*, vol. 4, no. 4, Art. 27, 2024. [doi:10.1145/3694791](https://doi.org/10.1145/3694791).
- **[6]** M. H. Nguyen, S. Tschiatschek, and A. Singla, "Enhancing Diversity of LLM-Generated Educational Tasks," *arXiv:2512.23601v2*, 2026; author-reported EDM 2026 poster paper. [Consulted version](https://arxiv.org/abs/2512.23601v2).
- **[7]** A. Shen, S. Druckmann, and J. Zou, "Unlocking LLM Creativity in Science through Analogical Reasoning," *arXiv preprint arXiv:2605.11258v1*, 2026. [Consulted version](https://arxiv.org/abs/2605.11258v1).
- **[8]** P. H. Luz de Araujo, P. Röttger, D. Hovy, and B. Roth, "Principled Personas: Defining and Measuring the Intended Effects of Persona Prompting on Task Performance," in *Proc. Conf. Empirical Methods in Natural Language Processing*, pp. 26857–26886, 2025. [doi:10.18653/v1/2025.emnlp-main.1364](https://doi.org/10.18653/v1/2025.emnlp-main.1364).
- **[9]** J.-B. Mouret and J. Clune, "Illuminating search spaces by mapping elites," *arXiv preprint arXiv:1504.04909*, 2015. [Original preprint](https://arxiv.org/abs/1504.04909).
- **[10]** M. Yasunaga, X. Chen, Y. Li, P. Pasupat, J. Leskovec, P. Liang, E. H. Chi, and D. Zhou, "Large Language Models as Analogical Reasoners," in *Proc. Int. Conf. Learning Representations (ICLR)*, 2024.

## Summary of This Paper

### Problem Setup

We study generated symbolic policies under prompt-level composition of biological/HCI exploration and minimalist-design guidance. The model receives named perspectives, mathematical hints, grammar and feedback. We ask which outputs merit examination and why, while keeping source-domain causation separate from artifact value.

### Novelty

The contribution is a traceable case study of generated structures, their overlap with inputs and decisions about their value. Minimum-coupled queue priority (A1) and cubic-stress thermal priority (A2) are explained through their actual formulas, observed revisions and saved paired comparisons. An above-reference rule (A5) is deprioritized because a simpler neutral alternative performs better. This is not a new search algorithm, a claim of mathematical novelty or proof of module synergy.

### Algorithms

The existing pilot contains 90 sessions, four rounds and three submissions per round. Original selection and independent test splits are retained. The v1.3 retrospective rule fixes five examples from original winners; v1.4 emphasizes A1/A2 editorially without replacing any case. New analysis joins already saved test rewards by seed and counts two exact whitespace-normalized motifs in the complete catalogue. It performs no model generation, environment evaluation, semantic clustering or inferential testing.

### Experiments

The catalogue retains 1,080 valid submissions, 822 distinct domain/string pairs, 916 component representative instances and 944 test-evaluated occurrences. A1 uses nine nodes versus 13 for its matched N_ROLE alternative and wins 402 of 600 saved paired traces. A2 uses 13 nodes versus seven for a matched X_FLAT cubic rule, winning 390 traces. A5 loses 328 traces to its simpler neutral alternative, with 270 wins and two ties. These are fixed-policy descriptive comparisons, not 600 independent generation replicates. Both emphasized motifs also occur in neutral conditions. The original X_ROLE minus N_ROLE primary contrast remains -0.1111 near-reference components per session; the strict-exceedance contrast is +0.3333 and does not replace it. One model, fixed wording, shared hints, six paired blocks per task, synthetic rewards, simple references and post-hoc selection limit interpretation. Real utility and causal cross-domain effects remain unestablished.

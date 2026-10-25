# Cross-Domain Skill Composition: Minimum Coupling and Cubic Stress in Generated Policies

**Bogyun Kim**  
Department of Computer Engineering, Mokpo National University, Muan, Republic of Korea  
`s11s45@naver.com`

## Abstract

Prompt-level composition of biological/HCI exploration and minimalist-design guidance produced symbolic policies whose appeal changes when alternatives and losses are examined. We trace five fixed retrospective cases from supplied hints to exact outputs, comparators and author judgments. Two findings organize the analysis. A minimum-coupled queue rule (A1) is interpretable, yet a smaller neutral rule has slightly higher saved means and ties its reward on 569 of 600 traces. A cubic-stress thermal rule (A2) has the highest observed selection and test mean among 30 original Thermal winners, yet loses to a smaller alternative on 210 traces. An explicitly invented calculation shows how A2 can change a priority choice; it is not a new environment observation. Comparisons retain all original winners and disclose incomplete test coverage among other submissions. Both highlighted structures occur in neutral conditions, and the original framing contrast remains -0.11 near-reference components per session. The contribution is a reproducible case study of generated outputs and adoption tradeoffs; cross-domain causation and practical utility remain unresolved.

**Keywords:** Cross-domain skill composition, generated artifacts, symbolic policies, exploratory evaluation.

## 1. Introduction and Related Work

An interesting generated rule should be something a reader can inspect, explain and compare with an alternative. Our motivating question is whether combining perspectives from unrelated domains can help an LLM produce such rules. We combine biological immune-adaptation and human-computer interaction (HCI) reframing with minimalist industrial-design guidance. The source domains are named by the prompt; the model chooses expressions within a supplied grammar, task facts, mathematical hints H and feedback. Here skill composition means textual guidance in one prompt, not independently executed agents or unconstrained discovery of source domains.

For reading the comparisons, **X** names cross-domain wording and **N** neutral wording. **ROLE** assigns exploration and simplicity distinct functions; **FLAT** combines the guidance. These are prompt conditions, not separate agents. **H** denotes supplied mathematical hints. A **block** contains one session per condition on the same task. Each session has one **original winner**, chosen on selection data before test access. **Utility U** is mean reward divided by the same task's reference mean; U=1 is the simple reference and larger is better. **Nodes** measure expression size, not runtime. A **trace** is one 320-step synthetic environment run; it is not an independent model generation.

Two findings guide the paper: an interpretable structure can lose its adoption case when the comparison set expands, and the highest observed mean can conceal losses against a simpler alternative. Section 2 connects the supplied input to exact outputs and explains their decisions; Section 3 provides the saved evidence. The five retrospective cases and the original aggregate outcome remain fixed.

LLM-driven executable search has precedents in FunSearch [1], Evolution of Heuristics [2] and ReEvo [3]. Analogical prompting [10] and cross-domain scientific search [7] motivate source perspectives; CreativeDC [6] combines divergent and convergent instructions. HSEvo [4], Language Model Crossover [5] and MAP-Elites [9] address diversity alongside quality; persona effects are task-dependent [8]. Our contribution is a traceable case study of generated structures and decisions about their value, not a new search or analogy algorithm. An older 414-expression corpus is excluded because its generation requests are unavailable.

## 2. From Supplied Input to Adoption Judgment

The common cross-domain instruction names biological immune-adaptation and HCI reframing for exploration, with minimalist industrial-design guidance for concise expressions. It asks the model to interpret supplied templates; it adds no physical laws or mathematical rules. Table 1 separates those templates from the submitted expressions and the alternatives used to judge them. A1/A2/A3/A5 use X_ROLE; A4 uses X_FLAT. Their presence here records outputs under those prompts, not the origin of the model's internal knowledge.

| Case | Supplied input H | Exact generated expression | Comparison alternative | Author judgment |
| --- | --- | --- | --- | --- |
| A1 | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle | `queue+min(drift,burst)-0.5*idle` | `queue+drift-0.5*idle` (neutral; 7 nodes) | Explain the minimum coupling; prefer the smaller alternative under mean reward and size |
| A2 | `soc*imped`; `max(stress-0.5,0)`; temperature | `temp+(0.5*(soc*imped)+stress*stress*stress)` | `temp+stress*stress*stress` (X_FLAT; 7 nodes) | Follow-up candidate: highest observed mean, with extra size and losses |
| A3 | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle | `idle-0.35*min(freq-0.5,0.25)+0.2*jitter` | `idle` (reference) | Low-priority diagnostic: supplied cap and tiny reference margin |
| A4 | Same Thermal H as A2 | `temp+soc*imped+2*max(stress-0.5,0)` | `temp+soc*imped+max(stress-0.5,0)` (matched X_ROLE) | Assembly/control example: supplied terms, with higher size and mean |
| A5 | Same Network H as A1 | `queue*(0.35+drift)-0.25*idle` | `queue+drift-0.5*idle` (matched N_ROLE) | Deprioritize: the smaller alternative scores higher |

*Table 1. Input, exact output, comparison and judgment for all five fixed cases. H entries summarize the supplied mathematical hints; the source-domain instruction above, task facts, grammar and session feedback are also inputs. Input-output differences do not identify a biological/HCI mechanism. A1's alternative comes from the full winner set; A2/A4/A5 use matched-block alternatives and A3 uses the reference. These are reasons for further examination or deprioritization, not deployment decisions.*

### 2.1 A1: An Interpretable Rule Can Have a Better Alternative

A1 ranks synthetic queues by adding the smaller of drift and burst to queue, then subtracting half idle. Both signals must be high for a large added priority. This exact minimum coupling is absent from H. Take two invented normalized queues with queue=0.6 and idle=0.1: P has drift=0.8 and burst=0.1; Q has drift=0.5 and burst=0.5. A1 scores them 0.65 and 1.05, selecting Q, whereas the reference scores them 0.960 and 0.885, selecting P. This is a decision illustration, not evidence that Q is better in practice.

The same-block comparison initially favors A1: nine nodes and test U=1.003905 versus 13 nodes and U=1.000870 for N_ROLE. Expanding to all original winners reveals the seven-node neutral alternative in Table 1. Section 3 shows why the larger comparison set weakens the adoption judgment even though the minimum rule is easy to explain.

The saved sequence records a coefficient change: round 2 slot 6 contains `queue+min(drift,burst)-0.25*idle`; round 3 changes -0.25 to -0.5 after that output and its feedback are supplied. The sequence establishes the visible revision, not its internal rationale.

![Behavior of the two emphasized structures](interesting_structures.png)

*Figure 1. Mathematical illustrations, not new environment observations. Left: min(drift,burst) is large only when both signals are large. Right: on [0,1], cubic stress downweights low stress relative to high stress. The straight line is a shape reference, not a tested full-policy comparator. Table 2 gives an A2 choice calculation; Tables 3 and 4 contain saved-policy comparisons.*

### 2.2 A2: Highest Mean Leaves an Adoption Tradeoff

A2 ranks synthetic modules for derating, using temperature, half the supplied soc*imped interaction and cubic stress. Here soc denotes state of charge and imped impedance. Cubing stress changes its response shape: 0.2 becomes 0.008 and 0.8 becomes 0.512. On [0,1] it reduces the value except at the endpoints. H supplies a positive-part threshold rather than a cubic term.

The simpler cubic alternative in Table 1 omits the product. Table 2 shows how adding it can reverse a choice. For invented normalized modules P and Q, the simpler rule selects P because its stress is higher at the same temperature. A2 instead selects Q: its larger soc*imped contribution outweighs the cubic-stress gap. Specifically, Q minus P is -0.169 for the simpler rule; the product adds 0.300, making the A2 difference +0.131.

| Module | temp | soc | imped | stress | Simpler score | A2 score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P | 0.6 | 0.2 | 0.2 | 0.8 | 1.112 | 1.132 |
| Q | 0.6 | 0.8 | 0.8 | 0.7 | 0.943 | 1.263 |

*Table 2. Invented normalized inputs and direct arithmetic. Simpler score is temp+stress*stress*stress; A2 adds 0.5*(soc*imped). Larger scores receive priority, so the pairwise choice changes from P to Q. Scores are not rewards. This is not a sampled test trace or a full four-module environment run, and establishes neither better derating nor safety. Both rules already contain the cubic term: the example explains the added supplied product's effect, not a cubic-term performance effect or a source-domain discovery.*

The example explains a possible decision difference; the saved comparisons in Section 3 determine its observed tradeoff. In the generation record, round 3 slot 9 first contains `temp+(soc*imped+stress*stress*stress)`; round 4 halves the product coefficient after that output and its feedback are supplied. The record provides no physical thermal validation.

### 2.3 A5: Above Reference Is an Incomplete Adoption Argument

A5 changes a supplied queue template's coefficients and omits burst. Its test U=1.002104 exceeds the simple reference, but the matched neutral expression in Table 1 reaches 1.003917 with seven nodes/depth 2 versus nine/depth 3. This comparison motivates deprioritization rather than labeling A5 a failed generation. Paired outcomes are retained in Section 3.2.

A5 was fixed by the low-selection rule, not chosen for a poor test outcome. The preceding round has `queue*(0.4+drift)-0.3*idle`; A5 revises the coefficients after feedback.

### 2.4 A3 and A4: Supplied Structures Remain Visible

A3 adjusts idle with an upper-capped frequency term and positive jitter, both supplied in H. For freq below 0.5, subtracting the negative min term adds a bonus; at freq at least 0.75 the contribution is fixed at -0.0875. Earlier rounds use cap weights 1 and 0.6; A3 uses 0.35. Test U=1.000466 and depth 4, above the soft target of 3, make it a low-priority diagnostic rather than evidence of cloud-cost savings.

A4 combines the supplied temperature, soc*imped and threshold terms, doubling the threshold weight. The preceding round contains both the doubled threshold without the product and the product with weight one. Test U=1.009928 exceeds the matched X_ROLE winner's 1.008923, with 13 nodes/depth 4 versus 11/depth 3. It is an X_FLAT assembly/control example, not a newly established domain connection.

## 3. Comparison with All Original Winners

### 3.1 Position among Original Winners and All Submissions

We first place each fixed case among all 30 original winners in its own task: six blocks times five conditions. We audit all 90 winners, but do not pool Network, Thermal and Cloud utilities. Duplicate expressions remain separate session outcomes; the 30 Network and Thermal winners contain 28 and 26 distinct exact strings. A rank is one plus the number of strictly higher utilities, with 1e-12 tolerance and ties retained. Selection and test ranks are computed separately. These descriptive ranks do not select new policies or estimate a generation effect.

We also compare expression size and utility. An alternative dominates a policy when it uses no more nodes and has no lower utility, with at least one strict difference. We assess this relation first on selection data and separately on saved test data. This numerical rule has no minimum practical effect threshold; a tiny score difference can change the status.

| Case | Winner rank: selection/test | Size-reward dominated: selection/test | All submissions: selection rank | Tested submissions: test rank |
| --- | --- | --- | --- | --- |
| A1 | 5/30; 5/30 | Yes; Yes | 7/360 | 7/327 |
| A2 | 1/30; 1/30 | No; No | 1/360 | 1/306 |

*Table 3. Same-task positions of fixed cases. The final two columns retain submitted occurrences, including repeats; 33 Network and 54 Thermal submissions have no saved test value. Ranks among available test values are not ranks over all 360 submissions. The analysis does not treat missing values as failures or claim a global optimum.*

A1's two dominators are instances of the same seven-node expression, from Network N_ROLE block 5 and N_FLAT block 6. Its test U=1.003917 is only about 0.000012 above A1; the selection advantage is approximately 4.38e-8. Expression size, rather than a demonstrated practically important score increment, drives the preference. We describe the first instance by session ID; both have identical formulas and stored traces. A2 is not dominated: its test U=1.011170 exceeds the simpler cubic alternative's 1.009897, with 13 rather than seven nodes.

![All original winners in the two focal tasks](policy_alternatives.png)

*Figure 2. All 30 original winners per focal task plotted by saved test utility and syntax nodes. Duplicate points overlap; outlined circles mark policies not dominated on selection data, then displayed at their saved test values. Stars mark the fixed cases; squares mark the discussed smaller alternatives. The figure is descriptive and does not reselect policies on test data.*

The secondary ranks in Table 3 cover all 360 submissions per task, with test denominators restricted to available values. Coverage depends on the original evaluation procedure, not random sampling. The analysis files give ranks, exact strings and dominators for all 90 winners, plus their positions and task coverage among submitted occurrences. Per-seed comparisons concern the 30 winners per task; the 360-submission view supplies ranks only.

### 3.2 Average Gains and Observed Downside

For each case, we subtract each same-task alternative's raw reward on the identical saved seed. This gives 30 comparisons including self, plus the reference, or 62 comparisons across A1/A2. The within-block contrast remains identifiable, while comparisons to other blocks describe fixed policies rather than paired generation interventions. All joins require 600 matching seeds and equal reference rewards.

A win has a difference above 1e-12; a tie is within that tolerance. Table 4 shows the mean difference, the mean of the 30 lowest differences (observed bottom 5%) and the largest observed loss. These are task-specific raw-reward quantities, not percentages. They describe this set of traces, not a bound on future risk or 600 independent model generations.

| Case | Comparator | Wins/ties/losses | Mean difference | Lowest-30 mean | Largest loss |
| --- | --- | --- | ---: | ---: | ---: |
| A1 | Reference | 514/0/86 | +0.003800 | -0.003681 | 0.007333 |
| A1 | N_ROLE B4: same block | 402/0/198 | +0.002953 | -0.004802 | 0.009958 |
| A1 | N_ROLE B5: simpler | 9/569/22 | -0.000012 | -0.000306 | 0.001276 |
| A2 | Reference | 599/0/1 | +0.014354 | +0.005077 | 0.000154 |
| A2 | X_FLAT B5: simpler | 390/0/210 | +0.001635 | -0.006591 | 0.010608 |

*Table 4. Gain and downside on saved common-seed traces. B denotes block. A negative lowest-30 mean indicates losses in that tail; largest loss is reported as a positive magnitude. The A1 seven-node comparator is identified by the selection-data dominance relation, not by searching test outcomes. The full supplement retains all 62 comparisons, medians, fifth percentiles and conditional gains/losses.*

The earlier comparisons for the other fixed cases are retained: A3 versus reference has 359 wins, no ties and 241 losses, with mean raw margin +0.000412; A4 has 599/0/1 and +0.012758. A5 versus its same-block N_ROLE alternative has 270/2/328 and -0.001764. Their complete matched-condition records remain in the v1.4 analysis.

Gain/loss contributions explain the averages. Against the same-block N_ROLE winner, A1's +0.003617 gain contribution minus 0.000664 loss contribution leaves +0.002953. Against the smaller cross-block rule, +0.00000355 minus 0.00001530 gives -0.00001176. For A2 versus the simpler cubic rule, +0.002580 minus 0.000945 gives +0.001635. Contributions divide all positive and absolute negative differences by 600, including differences within the tie tolerance; the supplement also gives conditional averages over only the corresponding signed cases.

These results support the two findings in Section 1. Expanding A1's comparator set changes the adoption judgment; A2's positive mean coexists with losses against a smaller policy. Equal total rewards do not establish identical actions. No acceptable loss or minimum useful gain was specified, so neither tradeoff is labeled practically acceptable. Whole-formula reward differences do not isolate the effect of min or the cubic term.

### 3.3 Interesting Structures Are Not Exclusive to Cross-Domain Roles

We also audit two explicitly defined motifs throughout the complete saved catalogue. After removing whitespace, we search for the exact substrings `min(drift,burst)` in Network and `stress*stress*stress` in Thermal. This is a narrow, reproducible string census, not semantic clustering or an exhaustive search for algebraically equivalent rules. Counts are retrospective and were chosen because of A1/A2.

The minimum motif appears in four X_ROLE submissions from one session, one N_ROLE submission from one session and one X_FLAT submission from one session. It is absent under this literal rule in N_FLAT and DOMAIN_V2. The cubic motif appears in seven X_FLAT submissions from five sessions, three N_FLAT submissions from one session and two X_ROLE submissions from one session; it is absent under the rule in N_ROLE and DOMAIN_V2. Each task/condition has six sessions and 72 submissions. Repeated submissions from a session are not independent discoveries.

These records sharpen the main distinction: a structure can be absent from H, interpretable and promising in a selected comparison without being specific to the cross-domain package. The minimum and cubic motifs are not evidence that biological, HCI or design knowledge caused the corresponding terms. Their neutral-condition occurrence is part of the finding, not an example to omit.

### 3.4 Complete Collection and Retrospective Selection

All 1,080 submissions pass the recorded validity gate. Within domains there are 822 distinct exact expression strings; spacing and algebraic variants remain separate. We retain every occurrence, including repeats, with its session, condition, block, round, slot, exact prompt, prior-answer/feedback request, and response line. The catalogue also records nodes/depth, original selection status, behavioral component, and saved scores. There are 916 component representative instances and 90 original session winners. Test outcomes exist for 944 submissions; the other 136 remain untested, not zero-scoring failures.

The offline catalogue supports expression search and domain, condition, test-availability and original-selection filters. Syntactic tags identify variable-bearing products, min/max, abs, division, or additive-affine forms. They help locate examples but do not establish semantic novelty or a cognitive process. The public case cards retain the exact H beside each case so that supplied building blocks are not credited as discoveries.

We fix three core cases: the original X_ROLE session winner with highest selection utility in each domain. Ties use nodes, depth, session ID and slot ID in ascending order. One X_FLAT complement is selected from original winners with a tag combination absent from the core cases, using Network-Thermal-Cloud domain order and the same ranking within the first eligible domain. One low-selection X_ROLE example uses that domain order, minimum selection utility, and the same tie rules after excluding already used domain/expression pairs. A missing eligible complement would be omitted.

The selection function receives only selection/provenance/syntax fields. It writes case IDs and a rule hash before attaching test values, without replacing cases after attachment. Nevertheless, the rule was devised after pilot results had been inspected: these are **post-hoc descriptive cases, not five prevalidated successes or the global best five outputs**. Matched comparison rows are the original winners of all five conditions in the same domain/block. Full inclusion/exclusion logs are public.

## 4. Inputs, Generation, and Evaluation

### 4.1 Source Perspectives and Target Tasks

The source perspectives and target tasks play different roles. Biological/HCI and design language supplies guidance; Network, Thermal, and Cloud are the tasks receiving generated rules. Network ranks four synthetic queues, Thermal ranks four synthetic modules for derating, and Cloud ranks six synthetic slots for reclamation. In each task, the expression assigns scores to options and the highest score determines the selected option. Features are normalized to [0,1] by clipping negative raw values at zero and applying x/(1+x). Ties retain the first option.

Expressions use four task variables, constants, arithmetic, min, max, and abs. All conditions share a hard gate of 25 AST nodes and implemented depth 5, with soft targets of 14 nodes and depth 3. Recorded depth flattens additive/subtractive and multiplication chains; it is not ordinary binary-tree height. Each environment trace has 320 steps, with handcrafted transitions and rewards; task names do not imply validated physical or production systems.

The four factorial conditions share the hints in Table 6. The cross-domain instruction asks the model to interpret them through biological immune-adaptation and HCI reframing analogies, using minimalist industrial-design inspiration for concise expressions. ROLE assigns exploration and simplicity distinct functions within the same response; FLAT presents both together. These are prompt instructions, not observed internal stages. DOMAIN_V2 omits H and changes the guidance procedure, so it is descriptive rather than a single-module ablation.

| Condition | Framing | Organization | H |
| --- | --- | --- | --- |
| N_FLAT | Neutral | Combined | Yes |
| N_ROLE | Neutral | Roles | Yes |
| X_FLAT | Cross-domain | Combined | Yes |
| X_ROLE | Cross-domain | Roles | Yes |
| DOMAIN_V2 | Domain | Base | No |

*Table 5. Conditions. Every factorial arm includes exploration and simplicity guidance. Roles are textual within one response.*

| Task | Shared mathematical hints H |
| --- | --- |
| Network | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle term |
| Thermal | `soc*imped`; `max(stress-0.5,0)`; temperature term |
| Cloud | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle |

*Table 6. H is supplied to all four factorial conditions within a task. The Cloud min term is an upper cap, not a lower clamp. Exact complete prompts and their verbatim differences are public.*

### 4.2 Recorded Generation and Evaluation

The pilot ran on 24 October 2026 (KST), requesting gpt-6.1-sol with low reasoning effort through Codex CLI 0.162.1. Three domains, six paired blocks per domain, and five conditions give 90 separately initialized sessions. Randomized condition order within domain/block and four rounds of three expressions yield 360 responses and 1,080 slots. Each session receives only its own prior answers and feedback. The required response is an expression array without explanatory commentary, so the record does not reveal the model's internal rationale.

The experimental message roles were serialized into one CLI input rather than sent as native API roles. Actual prompt length, semantics, and token use were not exactly matched; the requested 2,048-token output cap was not enforced. Thus the contrasts concern the recorded instruction packages, not perfectly resource-matched interventions or verified server snapshots.

Feedback, selection and test use disjoint base seeds: 48 (1000001-1000048), 96 (1100001-1100096), and 600 (1200001-1200600), with fixed Thermal/Cloud offsets. Selection starts after generation, and selected policies and representatives are frozen before test access. Independent generation comparisons use sessions; each session's 12 submissions are dependent.

The reference expressions are queue+0.45*drift+0.15*burst-0.15*idle for Network, temp+0.4*soc+0.35*imped+0.25*stress for Thermal, and idle for Cloud. Historical labels Adaptive-PI, PID-lite, and Fixed-TTL denote simplified synthetic formulas, not full implementations of those methods. Utility U is the policy's mean trace reward divided by the reference's mean reward on the same domain/split; the reference has U=1. This ratio is not an average of per-trace ratios. References are comparison points, not optima or tuned published competitors.

Behavioral groups use the saved graph on a fixed four-value-per-coordinate grid and 500 diagnostic option panels. An edge requires Spearman score correlation above 0.98 and top-action agreement of at least 95 percent. Connected components may contain transitive chains; they are finite-probe groups within a session, not globally unique ideas. Each representative and the overall session winner are chosen by selection mean reward, with expression-hash and slot tie breaks, then evaluated on test. The original primary outcome counts representatives with U at least 0.99. This near-reference criterion permits below-reference policies and is not a practical improvement threshold. Strict exceedance uses U greater than 1+1e-9. The analysis was locally frozen before test access, not publicly preregistered.

## 5. Aggregate Evidence and Boundaries

Selected examples do not replace the original experiment. Equal-domain averaging of six within-block contrasts gives -0.1111 near-reference components per session for X_ROLE minus N_ROLE. The Network, Thermal and Cloud means are -0.6667, +0.1667 and +0.1667, with paired SDs 2.9439, 2.2286 and 4.4907. Figure 3 retains all 18 differences. Six paired blocks per domain are the generation comparisons; test traces do not enlarge that sample.

![Original paired near-reference differences](paired_differences.png)

*Figure 3. Original X_ROLE minus N_ROLE near-reference counts by block and domain. Selected artifact examples must be read alongside this mixed aggregate result.*

| Outcome | X_ROLE−N_ROLE | X_ROLE−X_FLAT | Interaction |
| --- | ---: | ---: | ---: |
| Primary count | −0.1111 | −0.5556 | −1.2222 |
| Strict-exceedance count | +0.3333 | +0.6667 | +0.3889 |
| All-pairs count | −0.0556 | −0.4444 | −1.1111 |
| Selected-policy utility | +0.000998 | −0.000144 | +0.000062 |

*Table 7. Preserved aggregate comparisons. Interaction is (X_ROLE−X_FLAT)−(N_ROLE−N_FLAT). Counts and utility answer different questions. The utility contrast is not a relative percentage gain.*

The v1.2 retrospective profiles also remain relevant. Relative to N_ROLE, X_ROLE has 0.5370 more mean nodes and 0.3889 fewer pre-threshold components per session; relative to X_FLAT, the differences are +0.8148 and -0.4444. The node difference is mainly Thermal (+1.5556), with Network -0.1667 and Cloud +0.2222. All 12 submissions contribute to session means, including repeats. These profiles do not support an aggregate simplicity-diversity advantage and do not identify a compression process. Full tables and figures remain in the supplement.

Cloud further separates usable-looking artifacts from broad performance claims. Of 304 representative instances, 178 are below 0.99, 118 lie from 0.99 through 1, and eight strictly exceed 1+1e-9, between 1.000012 and 1.000541. Thus 126 meet the near-reference threshold, but only eight exceed the reference; 25 of 30 originally selected Cloud policies are below it. No representatives cross either threshold between saved selection and test splits. This does not rule out selection bias or explain the source of the generated rules.

The common limits apply to all case interpretations. The study uses one requested model/effort, one wording per condition, six paired blocks per task, shared H overlapping reward features, handcrafted transitions/rewards and simple references. Actual token budgets were not matched. Every factorial arm already contains both guidance functions; there are no exploration-only, design-only or bare-length controls. The case rule is retrospective and not representative sampling. Test ranks and observed downside are descriptive; no confidence intervals, equivalence decisions, user ratings or deployment evidence are added.

The catalogue supports inspection of outputs and follow-up priorities. It does not reveal which source-domain knowledge was used or show that cross-domain wording caused the structures. Neutral-condition occurrences and the original mixed aggregate result constrain that claim. Separating supplied templates from domain guidance, isolating individual expression terms and validating practical benefit would require evidence beyond these saved comparisons.

## 6. Conclusion and Reproduction

The contribution is a traceable assessment of outputs from prompt-level cross-domain skill composition. The cases show why interpretation, comparison and adoption are separate judgments: expanding the alternatives weakens A1's adoption case, and accounting for losses qualifies A2's highest observed mean. Table 1 connects those judgments to the supplied hints; the worked examples explain decisions without inventing empirical evidence. The neutral-condition motifs and original aggregate result do not support cross-domain superiority.

The public repository provides the v1.6.0 paper, source, worked example and Korean highlights: [https://github.com/7065616b/symbolic-policy-framing-pilot](https://github.com/7065616b/symbolic-policy-framing-pilot). The v1.5 alternative/loss analysis, earlier catalogues, case cards, exact prompts and evidence archives remain unchanged. Saved-data scripts reproduce the summaries without model or environment execution; identical model regeneration is not claimed because server snapshots and sampling seeds are unavailable. This editorial revision adds no model calls, environment traces or statistical simulations.

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

We examine generated symbolic policies under prompt-level composition of biological/HCI exploration and minimalist-design guidance. Source perspectives are named by the prompt; task facts, mathematical hints, grammar and feedback also constrain the outputs. We ask which outputs merit further examination and how alternatives change that judgment.

### Novelty

The contribution is a traceable case study linking supplied input, exact generated expressions, alternatives and author judgments. Two fixed cases show that an interpretable rule can lose its adoption case and that the highest observed mean can conceal losses against a simpler rule. This is not a new search algorithm, mathematical invention or demonstration of module synergy.

### Algorithms

The original 90 sessions yield 1,080 submissions, with separate feedback, selection and test data. All five retrospective cases and original winners remain fixed. A1/A2 are compared with all 30 winners in their own task, with separate selection/test positions and 62 common-seed comparisons. Secondary ranks disclose missing test values among all 360 task submissions. An invented two-module calculation illustrates an A2 choice reversal; it adds no environment observation and selects no new policy.

### Experiments

A1 ranks fifth among 30 Network winners on both splits. Two instances of the same smaller neutral rule have slightly higher means; its paired results against that rule are 9 wins, 569 ties and 22 losses. A2 ranks first among 30 Thermal winners. Against the seven-node cubic alternative, its 13-node expression has mean raw margin +0.001635 and 390 wins versus 210 losses; the largest observed loss is 0.010608. Among all submissions, A1 ranks seventh of 360 on selection and seventh of 327 tested occurrences; A2 ranks first of 360 and first of 306. The original X_ROLE minus N_ROLE primary contrast remains -0.1111 near-reference components per session, with strict exceedance +0.3333. Neutral-condition occurrences, shared hints, one requested model, six blocks per task, synthetic environments and retrospective case selection limit interpretation. Practical utility and causal cross-domain effects remain unresolved.

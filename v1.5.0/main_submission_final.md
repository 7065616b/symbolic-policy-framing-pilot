# Cross-Domain Skill Composition: Minimum Coupling and Cubic Stress in Generated Policies

**Bogyun Kim**  
Department of Computer Engineering, Mokpo National University, Muan, Republic of Korea  
`s11s45@naver.com`

## Abstract

We examine which generated policies merit further study under prompt-level composition of biological/HCI exploration and minimalist-design guidance. Two fixed retrospective cases make the question concrete: minimum-coupled queue priority (A1) and cubic-stress thermal priority (A2). Saved-data comparisons place each case among all 30 original session winners in its task. A1 ranks fifth, but a seven-node neutral rule is slightly higher-scoring than its nine-node expression and ties its reward on 569 of 600 traces. A2 has the highest observed selection and test mean among the 30 Thermal winners; compared with a seven-node cubic alternative, its 13-node expression gains on average but loses on 210 traces. We report gain/loss magnitudes, full alternative tables and incomplete test coverage among all submissions. Both highlighted structures also occur in neutral conditions, and the original aggregate framing contrast remains -0.11 near-reference components per session. The contribution is a reproducible assessment of behavior, alternatives and adoption tradeoffs. Practical utility and cross-domain causation remain unresolved.

**Keywords:** Cross-domain skill composition, generated artifacts, symbolic policies, exploratory evaluation.

## 1. Introduction and Related Work

An interesting generated rule should be something a reader can inspect, explain and compare with an alternative. Our motivating question is whether combining perspectives from unrelated domains can help an LLM produce such rules. We combine biological immune-adaptation and human-computer interaction (HCI) reframing with minimalist industrial-design guidance. The source domains are named by the prompt; the model chooses expressions within a supplied grammar, task facts, mathematical hints H and feedback. Here skill composition means textual guidance in one prompt, not independently executed agents or unconstrained discovery of source domains.

For reading the comparisons, **X** names cross-domain wording and **N** neutral wording. **ROLE** assigns exploration and simplicity distinct functions; **FLAT** combines the guidance. These are prompt conditions, not separate agents. **H** denotes supplied mathematical hints. A **block** contains one session per condition on the same task. Each session has one **original winner**, chosen on selection data before test access. **Utility U** is mean reward divided by the same task's reference mean; U=1 is the simple reference and larger is better. **Nodes** measure expression size, not runtime. A **trace** is one 320-step synthetic environment run; it is not an independent model generation.

Consider `queue+min(drift,burst)-0.5*idle`. Its minimum term rewards the joint presence of two signals: a large value of one cannot compensate for a small value of the other. A second output, `temp+(0.5*(soc*imped)+stress*stress*stress)`, suppresses the contribution of low stress relative to high stress. These are recognizable decision rules rather than abstract improvements in an output count. They are the focus of this paper because their behavior can be explained and their tradeoffs examined.

We ask what these artifacts do, whether their saved results justify further examination, and how much of their structure was already supplied. A1 and A2 are emphasized within the same five fixed retrospective cases; the expanded comparisons do not replace them. A5 shows why exceeding a simple reference is insufficient for adoption. The other cases, the full catalogue and the original unfavorable aggregate result remain visible.

LLM-driven executable search has precedents in FunSearch [1], Evolution of Heuristics [2] and ReEvo [3]. Analogical prompting [10] and cross-domain scientific search [7] motivate source perspectives; CreativeDC [6] combines divergent and convergent instructions. HSEvo [4], Language Model Crossover [5] and MAP-Elites [9] address diversity alongside quality; persona effects are task-dependent [8]. Our contribution is a traceable case study of generated structures and decisions about their value, not a new search or analogy algorithm. An older 414-expression corpus is excluded because its generation requests are unavailable.

## 2. Two Candidate Structures and an Adoption Counterexample

### 2.1 A1: Require Two Signals Together

A1 scores synthetic queues as `queue+min(drift,burst)-0.5*idle`. A low drift or low burst limits the added priority. This exact coupling is absent from H, which instead supplies `queue*(0.45+drift)`, `max(burst-idle,0)` and a negative idle term. This is an observable combination absent from those hints.

The rule can change a decision in an intelligible way. Take two invented normalized queues with queue=0.6 and idle=0.1. P has drift=0.8 and burst=0.1; Q has drift=0.5 and burst=0.5. A1 scores them 0.65 and 1.05, selecting Q. The reference scores them 0.960 and 0.885, selecting P. This illustrates a preference for both signals being present; it does not establish that Q is the better real-world choice.

The initial same-block comparison is favorable: A1 uses nine nodes versus 13 for N_ROLE, with test U=1.003905 versus 1.000870 and 402 wins versus 198 losses. The full alternative set changes the adoption judgment. A1 ranks fifth among the 30 Network winners, and `queue+drift-0.5*idle` uses seven nodes with slightly higher selection and test means. Against that simpler rule, A1 wins nine traces, ties 569 and loses 22. Equal total rewards do not establish identical actions. A1 remains an interpretable example of minimum coupling, but its average reward does not justify preferring it to this smaller alternative.

The record also shows how the expression changed. In round 2, slot 6, the model had already produced `queue+min(drift,burst)-0.25*idle`. A1 is the round-3 variant with coefficient -0.5, after that output and its feedback were supplied. This records a visible change after feedback.

![Behavior of the two emphasized structures](interesting_structures.png)

*Figure 1. Mathematical illustrations, not new environment observations. Left: the contribution min(drift,burst) is large only when both signals are large. Right: on [0,1], cubic stress downweights low stress relative to high stress. The straight line is a shape reference, not a tested full-policy comparator. Whole-policy positions and saved reward differences are in Tables 2 and 3.*

### 2.2 A2: Spend Complexity Only When the Added Term Helps

A2 scores synthetic modules for derating using temperature, half the supplied soc*imped interaction and cubic stress. At stress 0.2 the cubic contribution is 0.008; at 0.8 it is 0.512. On [0,1], cubing decreases the value except at the endpoints; the interesting property is the changed response shape, not amplification above the original stress value. H supplies a positive-part threshold `max(stress-0.5,0)`, rather than a cubic term.

A2's test utility is 1.011170. However, the matched X_FLAT winner `temp+stress*stress*stress` achieves 1.009897 with seven nodes instead of 13. A2 wins on 390 of 600 paired traces and loses on 210. A2 also ranks first in both selection and test mean among all 30 Thermal winners. Its mean advantage over the simpler cubic rule is +0.001635 raw reward, but the worst observed loss is 0.010608 and the mean difference on the 30 most unfavorable traces is -0.006591. The highest observed mean therefore makes A2 a follow-up candidate, while the extra six nodes and observed losses leave adoption dependent on the application's tolerance for these costs.

Within the session, `temp+(soc*imped+stress*stress*stress)` first appears in round 3, slot 9. The round-4 A2 halves the product coefficient after that output and its feedback are supplied. The cubic structure also appears in neutral and X_FLAT sessions, as the motif census below records. The simulated task does not establish battery safety or physical thermal behavior.

### 2.3 A5: Above Reference Does Not Mean Worth Adopting

A5, `queue*(0.35+drift)-0.25*idle`, changes the coefficients of a supplied template and omits burst. Its test utility is 1.002104, above the simple reference. Yet the same-block N_ROLE policy `queue+drift-0.5*idle` reaches 1.003917 with seven nodes/depth 2 versus A5's nine nodes/depth 3. A5 wins 270 paired traces, ties two and loses 328 against that alternative. This separates reference exceedance from a reason to prefer an output.

A5 was fixed by the low-selection rule, not selected for a poor test outcome. The preceding round already contains `queue*(0.4+drift)-0.3*idle`; A5 changes its coefficients after feedback. It is a valid, above-reference output, not a failed generation. Our author judgment is to deprioritize it relative to the simpler matched alternative.

### 2.4 The Other Cases and the Final Judgment

A3, the Cloud case in Table 1, adjusts idle with an upper-capped frequency term and positive jitter. For freq below 0.5, subtracting the negative min term adds a bonus; at freq at least 0.75 the frequency contribution is fixed at -0.0875. This cap and jitter were supplied in H. Earlier rounds use cap weights 1 and 0.6; A3 uses 0.35. Its test utility is only 1.000466, and depth 4 exceeds the soft target of 3. We retain it as a low-priority diagnostic, not evidence of cloud-cost savings.

A4 combines the supplied temperature, soc*imped and threshold terms, with weight two on the threshold. The preceding round contains both the doubled threshold without the product and the product with weight one. Its test utility is 1.009928, versus 1.008923 for the matched X_ROLE winner, at 13 nodes/depth 4 versus 11/depth 3. We retain A4 as an assembly/control example; it is an X_FLAT output, not an X_ROLE success or a newly discovered domain connection.

| Case | Exact submitted expression | Author judgment and reason |
| --- | --- | --- |
| A1 | `queue+min(drift,burst)-0.5*idle` | Explain the coupling; prefer the simpler neutral alternative under mean reward and size |
| A2 | `temp+(0.5*(soc*imped)+stress*stress*stress)` | Highest observed task mean; weigh extra nodes and losses against the simpler cubic rule |
| A3 | `idle-0.35*min(freq-0.5,0.25)+0.2*jitter` | Low priority: supplied cap; tiny reference margin |
| A4 | `temp+soc*imped+2*max(stress-0.5,0)` | Assembly/control: supplied terms; no new source connection established |
| A5 | `queue*(0.35+drift)-0.25*idle` | Deprioritize: simpler matched neutral alternative scores higher |

*Table 1. All five fixed cases remain visible. Judgments combine behavior, input overlap, saved reward and syntax cost. They prioritize further examination, not deployment. A1/A2/A3/A5 are X_ROLE; A4 is X_FLAT. Full provenance and selection utilities are in the unchanged case cards.*

## 3. Comparison with All Original Winners

### 3.1 Position among Original Winners and All Submissions

We first place each fixed case among all 30 original winners in its own task: six blocks times five conditions. We audit all 90 winners, but do not pool Network, Thermal and Cloud utilities. Duplicate expressions remain separate session outcomes; the 30 Network and Thermal winners contain 28 and 26 distinct exact strings. A rank is one plus the number of strictly higher utilities, with 1e-12 tolerance and ties retained. Selection and test ranks are computed separately. These descriptive ranks do not select new policies or estimate a generation effect.

We also compare expression size and utility. An alternative dominates a policy when it uses no more nodes and has no lower utility, with at least one strict difference. We assess this relation first on selection data and separately on saved test data. This numerical rule has no minimum practical effect threshold; a tiny score difference can change the status.

| Case | Winner rank: selection/test | Size-reward dominated: selection/test | All submissions: selection rank | Tested submissions: test rank |
| --- | --- | --- | --- | --- |
| A1 | 5/30; 5/30 | Yes; Yes | 7/360 | 7/327 |
| A2 | 1/30; 1/30 | No; No | 1/360 | 1/306 |

*Table 2. Same-task positions of fixed cases. The final two columns retain submitted occurrences, including repeats; 33 Network and 54 Thermal submissions have no saved test value. Ranks among available test values are not ranks over all 360 submissions. The analysis does not treat missing values as failures or claim a global optimum.*

A1 has two dominating winner instances, both the same seven-node expression `queue+drift-0.5*idle`, generated by Network N_ROLE block 5 and N_FLAT block 6. Its test U=1.003917 is only about 0.000012 above A1; its selection advantage is approximately 4.38e-8. The smaller expression, rather than a demonstrated practically important score increment, drives the preference. We use the first instance by session ID to describe its paired outcomes; the formula and stored traces are identical for both. A2 is not dominated and has the highest observed mean among the 30 Thermal winners on both splits. The seven-node cubic alternative remains a meaningful size/performance tradeoff.

![All original winners in the two focal tasks](policy_alternatives.png)

*Figure 2. All 30 original winners per focal task plotted by saved test utility and syntax nodes. Duplicate points overlap; outlined circles mark policies not dominated on selection data, then displayed at their saved test values. Stars mark the fixed cases; squares mark the discussed smaller alternatives. The figure is descriptive and does not reselect policies on test data.*

The secondary census covers all 360 submissions per task. A1 is seventh by selection utility and seventh among 327 tested occurrences. A2 is first by selection utility and first among 306 tested occurrences. Test coverage depends on the original evaluation procedure and is not random sampling. The analysis files provide ranks, exact strings and dominators for all 90 winners, plus focal-case positions and task coverage among submitted occurrences. Per-seed alternative comparisons concern the 30 winners per task; the 360-submission view supplies ranks only.

### 3.2 Average Gains and Observed Downside

For each case, we subtract each same-task alternative's raw reward on the identical saved seed. This gives 30 comparisons including self, plus the reference, or 62 comparisons across A1/A2. The within-block contrast remains identifiable, while comparisons to other blocks describe fixed policies rather than paired generation interventions. All joins require 600 matching seeds and equal reference rewards.

A win has a difference above 1e-12; a tie is within that tolerance. Table 3 shows the mean difference, the mean of the 30 lowest differences (observed bottom 5%) and the largest observed loss. These are task-specific raw-reward quantities, not percentages. They describe this set of traces, not a bound on future risk or 600 independent model generations.

| Case | Comparator | Wins/ties/losses | Mean difference | Lowest-30 mean | Largest loss |
| --- | --- | --- | ---: | ---: | ---: |
| A1 | Reference | 514/0/86 | +0.003800 | -0.003681 | 0.007333 |
| A1 | N_ROLE B4: same block | 402/0/198 | +0.002953 | -0.004802 | 0.009958 |
| A1 | N_ROLE B5: simpler | 9/569/22 | -0.000012 | -0.000306 | 0.001276 |
| A2 | Reference | 599/0/1 | +0.014354 | +0.005077 | 0.000154 |
| A2 | X_FLAT B5: simpler | 390/0/210 | +0.001635 | -0.006591 | 0.010608 |

*Table 3. Gain and downside on saved common-seed traces. B denotes block. A negative lowest-30 mean indicates losses in that tail; largest loss is reported as a positive magnitude. The A1 seven-node comparator is identified by the selection-data dominance relation, not by searching test outcomes. The full supplement retains all 62 comparisons, medians, fifth percentiles and conditional gains/losses.*

The earlier comparisons for the other fixed cases are retained: A3 versus reference has 359 wins, no ties and 241 losses, with mean raw margin +0.000412; A4 has 599/0/1 and +0.012758. A5 versus its same-block N_ROLE alternative has 270/2/328 and -0.001764. Their complete matched-condition records remain in the v1.4 analysis.

The decomposition makes the average easier to interpret. For A1 versus the original same-block N_ROLE winner, positive differences contribute +0.003617 per trace and negative differences cost 0.000664, leaving +0.002953. Against the simpler cross-block rule, the contributions are only +0.00000355 and -0.00001530, yielding -0.00001176, with 569 reward ties. For A2 versus the simpler cubic rule, +0.002580 minus 0.000945 yields +0.001635, while 210 traces lose and the lowest-30 mean is negative. Contributions divide positive and absolute negative sums by all 600 traces; conditional averages divide by only the corresponding positive or negative cases and are reported separately. Contributions include all signed differences, including those within the tie tolerance.

These comparisons revise the author judgment: A1 is useful for explaining a generated structure, but offers little reward-based reason to displace its simpler neutral alternative. A2 is a candidate for examining whether a small mean gain justifies additional syntax and occasional losses. No application-specific acceptable loss or minimum useful gain was specified, so the paper does not label either tradeoff practically acceptable. Differences between whole formulas do not isolate the effect of min or the cubic term.

### 3.3 Interesting Structures Are Not Exclusive to Cross-Domain Roles

We also audit two explicitly defined motifs throughout the complete saved catalogue. After removing whitespace, we search for the exact substrings `min(drift,burst)` in Network and `stress*stress*stress` in Thermal. This is a narrow, reproducible string census, not semantic clustering or an exhaustive search for algebraically equivalent rules. Counts are retrospective and were chosen because of A1/A2.

The minimum motif appears in four X_ROLE submissions from one session, one N_ROLE submission from one session and one X_FLAT submission from one session. It is absent under this literal rule in N_FLAT and DOMAIN_V2. The cubic motif appears in seven X_FLAT submissions from five sessions, three N_FLAT submissions from one session and two X_ROLE submissions from one session; it is absent under the rule in N_ROLE and DOMAIN_V2. Each task/condition has six sessions and 72 submissions. Repeated submissions from a session are not independent discoveries.

These records sharpen the main distinction: a structure can be absent from H, interpretable and promising in a selected comparison without being specific to the cross-domain package. The minimum and cubic motifs are not evidence that biological, HCI or design knowledge caused the corresponding terms. Their neutral-condition occurrence is part of the finding, not an example to omit.

### 3.4 Complete Collection and Retrospective Selection

All 1,080 submissions pass the recorded validity gate. Within domains there are 822 distinct exact expression strings; spacing and algebraic variants remain separate. We retain every occurrence, including repeats, with its session, condition, block, round, slot, exact prompt, prior-answer/feedback request, and response line. The catalogue also records nodes/depth, original selection status, behavioral component, and saved scores. There are 916 component representative instances and 90 original session winners. Test outcomes exist for 944 submissions; the other 136 remain untested, not zero-scoring failures.

The offline catalogue supports expression search and domain, condition, test-availability and original-selection filters. Syntactic tags identify variable-bearing products, min/max, abs, division, or additive-affine forms. They help locate examples but do not establish semantic novelty or a cognitive process. The input comparison keeps the exact H beside each case so that supplied building blocks are not credited as discoveries.

We fix three core cases: the original X_ROLE session winner with highest selection utility in each domain. Ties use nodes, depth, session ID and slot ID in ascending order. One X_FLAT complement is selected from original winners with a tag combination absent from the core cases, using Network-Thermal-Cloud domain order and the same ranking within the first eligible domain. One low-selection X_ROLE example uses that domain order, minimum selection utility, and the same tie rules after excluding already used domain/expression pairs. A missing eligible complement would be omitted.

The selection function receives only selection/provenance/syntax fields. It writes case IDs and a rule hash before attaching test values, without replacing cases after attachment. Nevertheless, the rule was devised after pilot results had been inspected: these are **post-hoc descriptive cases, not five prevalidated successes or the global best five outputs**. Matched comparison rows are the original winners of all five conditions in the same domain/block. Full inclusion/exclusion logs are public.

## 4. Inputs, Generation, and Evaluation

### 4.1 Source Perspectives and Target Tasks

The source perspectives and target tasks play different roles. Biological/HCI and design language supplies guidance; Network, Thermal, and Cloud are the tasks receiving generated rules. Network ranks four synthetic queues, Thermal ranks four synthetic modules for derating, and Cloud ranks six synthetic slots for reclamation. In each task, the expression assigns scores to options and the highest score determines the selected option. Features are normalized to [0,1] by clipping negative raw values at zero and applying x/(1+x). Ties retain the first option.

Expressions use four task variables, constants, arithmetic, min, max, and abs. All conditions share a hard gate of 25 AST nodes and implemented depth 5, with soft targets of 14 nodes and depth 3. Recorded depth flattens additive/subtractive and multiplication chains; it is not ordinary binary-tree height. Each environment trace has 320 steps, with handcrafted transitions and rewards; task names do not imply validated physical or production systems.

The four factorial conditions share the hints in Table 5. The cross-domain instruction asks the model to interpret them through biological immune-adaptation and HCI reframing analogies, using minimalist industrial-design inspiration for concise expressions. ROLE assigns exploration and simplicity distinct functions within the same response; FLAT presents both together. These are prompt instructions, not observed internal stages. DOMAIN_V2 omits H and changes the guidance procedure, so it is descriptive rather than a single-module ablation.

| Condition | Framing | Organization | H |
| --- | --- | --- | --- |
| N_FLAT | Neutral | Combined | Yes |
| N_ROLE | Neutral | Roles | Yes |
| X_FLAT | Cross-domain | Combined | Yes |
| X_ROLE | Cross-domain | Roles | Yes |
| DOMAIN_V2 | Domain | Base | No |

*Table 4. Conditions. Every factorial arm includes exploration and simplicity guidance. Roles are textual within one response.*

| Task | Shared mathematical hints H |
| --- | --- |
| Network | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle term |
| Thermal | `soc*imped`; `max(stress-0.5,0)`; temperature term |
| Cloud | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle |

*Table 5. H is supplied to all four factorial conditions within a task. The Cloud min term is an upper cap, not a lower clamp. Exact complete prompts and their verbatim differences are public.*

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

*Table 6. Preserved aggregate comparisons. Interaction is (X_ROLE−X_FLAT)−(N_ROLE−N_FLAT). Counts and utility answer different questions. The utility contrast is not a relative percentage gain.*

The v1.2 retrospective profiles also remain relevant. Relative to N_ROLE, X_ROLE has 0.5370 more mean nodes and 0.3889 fewer pre-threshold components per session; relative to X_FLAT, the differences are +0.8148 and -0.4444. The node difference is mainly Thermal (+1.5556), with Network -0.1667 and Cloud +0.2222. All 12 submissions contribute to session means, including repeats. These profiles do not support an aggregate simplicity-diversity advantage and do not identify a compression process. Full tables and figures remain in the supplement.

Cloud further separates usable-looking artifacts from broad performance claims. Of 304 representative instances, 178 are below 0.99, 118 lie from 0.99 through 1, and eight strictly exceed 1+1e-9, between 1.000012 and 1.000541. Thus 126 meet the near-reference threshold, but only eight exceed the reference; 25 of 30 originally selected Cloud policies are below it. No representatives cross either threshold between saved selection and test splits. This does not rule out selection bias or explain the source of the generated rules.

The common limits apply to all case interpretations. The study uses one requested model/effort, one wording per condition, six paired blocks per task, shared H overlapping reward features, handcrafted transitions/rewards and simple references. Actual token budgets were not matched. Every factorial arm already contains both guidance functions; there are no exploration-only, design-only or bare-length controls. The case rule is retrospective and not representative sampling. Test ranks and observed downside are descriptive; no confidence intervals, equivalence decisions, user ratings or deployment evidence are added.

The catalogue supports inspection of outputs and follow-up priorities. It does not reveal which source-domain knowledge was used or show that cross-domain wording caused the structures. Neutral-condition occurrences and the original mixed aggregate result constrain that claim. Separating supplied templates from domain guidance, isolating individual expression terms and validating practical benefit would require evidence beyond these saved comparisons.

## 6. Conclusion and Reproduction

Comparison with all original winners refines the artifact judgments. A1 illustrates minimum coupling, but the smaller neutral alternative weakens its adoption case. A2 has the highest observed task mean among original winners, with additional complexity and observed losses. A5 reinforces that a reference exceedance does not settle adoption; A3/A4 show substantial template reuse.

This is an exploratory account of outputs from cross-domain skill composition, their input overlap and reasons to examine or deprioritize them. Interesting structure, average reward and practical value remain distinct. Both highlighted motifs also occur in neutral conditions, and the original aggregate result does not support cross-domain superiority.

The public repository provides the v1.5.0 paper, source, complete alternative/loss analysis and Korean highlights: [https://github.com/7065616b/symbolic-policy-framing-pilot](https://github.com/7065616b/symbolic-policy-framing-pilot). Earlier catalogues, case cards, exact prompts and evidence archives remain unchanged. Scripts reproduce saved-data summaries without model or environment execution. Identical model regeneration is not claimed because server snapshots and sampling seeds are unavailable. This revision adds no research model calls, environment traces or statistical simulations.

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

We study generated policy expressions under prompt-level composition of biological/HCI exploration and minimalist-design guidance. The model receives named perspectives, mathematical hints, grammar and feedback. We ask what outputs emerge and which merit further examination, keeping source-domain causation separate from artifact value.

### Novelty

The contribution is a traceable case study linking exact outputs, input overlap, all saved alternatives and adoption tradeoffs. A1 minimum coupling and A2 cubic stress remain fixed retrospective cases. The full comparison revises the initial judgment about A1 and exposes the losses hidden by A2's positive mean. This is not a new algorithm, mathematical invention or demonstration of module synergy.

### Algorithms

The original 90 sessions produce 1,080 submissions, with separate feedback, selection and test splits. We retain original winners and all five posthoc cases. Each focal case is compared to the 30 original winners in its own task, with selection/test ranks and size-reward dominance computed separately. Secondary positions among all 360 task submissions retain missing test values. Sixty-two common-seed comparisons report gains, losses and observed tails. The new analysis uses saved files only and does not select policies on test outcomes.

### Experiments

A1 ranks fifth of 30 Network winners on both selection and test mean. Two instances of the same seven-node neutral rule have slightly higher means than its nine-node expression; A1 wins nine traces, ties 569 and loses 22 against this rule. A2 ranks first of 30 Thermal winners on both splits and is not size-reward dominated. Against the seven-node cubic alternative, its 13-node expression has mean raw margin +0.001635, 390 wins and 210 losses; the observed worst loss is 0.010608. Among all submissions, A1 ranks seventh of 360 on selection and seventh of 327 tested occurrences; A2 ranks first of 360 and first of 306 tested occurrences. Missing tests are not failures. The original primary X_ROLE minus N_ROLE contrast remains -0.1111 near-reference components per session; strict exceedance +0.3333 does not replace it. Both highlighted motifs also occur in neutral conditions. One model, fixed wording, shared hints, synthetic tasks, simple references and retrospective case emphasis limit interpretation. Practical utility and causal cross-domain effects remain unresolved.

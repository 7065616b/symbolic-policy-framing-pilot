# Cross-Domain Skill Composition: An Exploratory Study of Generated Policies

**Bogyun Kim**  
Department of Computer Engineering, Mokpo National University, Muan, Republic of Korea  
`s11s45@naver.com`

## Abstract

This study examines what an AI produces when asked to combine perspectives from different fields to build task skills. Here a skill is a small executable rule for choosing which option to act on. We combine biological and human-computer interaction guidance for exploration with minimalist-design guidance for simpler rules, while also supplying task facts and mathematical hints. We inspect five retrospectively selected examples and compare them with alternatives using existing data. A thermal-control candidate has the highest original mean among 30 selected rules, but beats the strongest selection-ranked neutral alternative in only 308 of 600 saved runs. Its small average gain comes with losses. Its ranking changes across 36 reward-weight settings; halving hazard-credit weight puts it last among four rules. A network candidate loses its initial appeal under broader comparison. The contribution is a record of what was generated, what changed from the supplied inputs, and why a candidate merits further examination. Cross-domain superiority, causal knowledge transfer and practical usefulness remain unestablished.

**Keywords:** Cross-domain skill composition, symbolic policies, exploratory study, candidate evaluation.

## 1. Introduction and Related Work

We ask an AI to combine perspectives from different fields to build task skills, then examine which outputs are worth keeping. A skill here is an executable rule that scores options and selects one. These rules are mathematical expressions, not complete applications or independent agents.

The source perspectives are biological immune-adaptation, human-computer interaction (HCI) reframing and minimalist industrial design. Biology/HCI guide exploration; design guides simplification. We also supply task facts, a grammar, mathematical hints H and feedback. The model chooses expressions within these constraints, not the source fields. The synthetic tasks are selecting a network queue, a module for load reduction, or a cloud slot to reclaim.

For each example, we show the supplied input, the generated rule and a reason to retain or deprioritize it. The thermal rule A2 changes rank with scoring weights; the network rule A1 loses its initial appeal under broader comparison. The five case IDs and original winners stay fixed. These examples alone cannot establish knowledge transfer.

LLM-driven executable search has precedents in FunSearch [1], Evolution of Heuristics [2] and ReEvo [3]. Analogical prompting [10] and cross-domain scientific search [7] motivate source perspectives; CreativeDC [6] combines divergent and convergent instructions. HSEvo [4], Language Model Crossover [5] and MAP-Elites [9] address diversity alongside quality; persona effects are task-dependent [8]. Our contribution is a traceable case study of generated structures and decisions about their value, not a new search or analogy algorithm. An older 414-expression corpus is excluded because its generation requests are unavailable.

## 2. Generated Rules and Reasons for Further Study

Table 1 links supplied hints H, generated rules, alternatives and judgments. A1/A2/A3/A5 use X_ROLE; A4 uses X_FLAT (Section 4). Domain labels do not establish the origin of a term.

| Case | Supplied input H | Exact generated expression | Comparison alternative | Author judgment |
| --- | --- | --- | --- | --- |
| A2 | `soc*imped`; `max(stress-0.5,0)`; temperature | `temp+(0.5*(soc*imped)+stress*stress*stress)` | `temp+stress*stress*stress` (X_FLAT; 7 nodes) | Conditional follow-up: favorable original mean; preference changes with reward weights |
| A1 | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle | `queue+min(drift,burst)-0.5*idle` | `queue+drift-0.5*idle` (neutral; 7 nodes) | Broader comparison weakens the initial adoption argument; a smaller alternative scores slightly higher |
| A3 | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle | `idle-0.35*min(freq-0.5,0.25)+0.2*jitter` | `idle` (reference) | Low-priority diagnostic: supplied cap and tiny reference margin |
| A4 | Same Thermal H as A2 | `temp+soc*imped+2*max(stress-0.5,0)` | `temp+soc*imped+max(stress-0.5,0)` (matched X_ROLE) | Assembly/control example: supplied terms, with higher size and mean |
| A5 | Same Network H as A1 | `queue*(0.35+drift)-0.25*idle` | `queue+drift-0.5*idle` (matched N_ROLE) | Deprioritize: the smaller alternative scores higher |

*Table 1. Supplied input, exact output, alternative and judgment for the five fixed cases, with A2 first. H summarizes mathematical hints; inputs also include domain instructions, task facts, grammar and feedback. A1 uses an alternative from all winners; A2/A4/A5 use matched-block alternatives and A3 the reference. Input-output differences do not establish a biological/HCI mechanism or justify deployment. Table 2 gives A2's nearby alternatives.*

### 2.1 A2: Choosing a Module for Load Reduction

A2 scores four synthetic modules using temperature, charge (soc), impedance (imped) and stress. It selects the highest-scoring module for a simulated derating action that reduces temperature and stress. We separate the supplied input, generated changes and explanations the record cannot establish.

**Supplied:** the prompt names biological immune-adaptation, HCI reframing and minimalist design, and gives the four variables, grammar, feedback, temperature term, soc*imped and max(stress-0.5,0). It does not prescribe A2's complete formula.

**Generated:** A2 retains temperature and the product, weights the product by 0.5, omits the supplied threshold and uses cubic stress. Cubing normalized [0,1] stress reduces its value except at the endpoints. The saved sequence contains product weight 1 in round 3 slot 9 and weight 0.5 in round 4 after feedback. These are observed expression changes relative to H and the preceding response.

**Unestablished:** the record establishes neither a biological/HCI origin for the cubic term, its mathematical novelty nor the model's reasoning. The cubic motif also occurs under neutral wording, leaving causal domain transfer unresolved.

| Policy | Exact score expression | Nodes | Selection U | Test U |
| --- | --- | ---: | ---: | ---: |
| A2 | `temp+(0.5*(soc*imped)+stress*stress*stress)` | 13 | 1.011889 | 1.011170 |
| S | `temp+stress*stress*stress` | 7 | 1.010594 | 1.009897 |
| N | `temp+0.5*soc*imped+1.5*max(stress-0.5,0)` | 15 | 1.011573 | 1.011015 |
| C | `temp+stress*stress*stress+0.1*soc*imped` | 13 | 1.011253 | 1.010659 |

*Table 2. S is the matched-block seven-node X_FLAT winner; N is the highest selection-mean neutral Thermal winner (N_FLAT block 6); C is the highest selection-mean other 13-node Thermal winner with the literal cubic motif (X_FLAT block 2). These retrospective choices use original winners and selection data, without a coefficient search. U is a ratio of means; nodes measure size, not speed.*

We replay all 600 original 320-step seeds, recording inputs, choices and rewards without changing transitions or random draws. All 2,400 policy-seed means and 600 references exactly match saved values and the original simulator. Replay adds no independent tests.

For each alternative, we select the smallest base seed with a positive A2 margin and the smallest with a negative margin (tolerance 1e-12): two trace pairs per alternative, six in total. We inspect their first differing actions. This retrospective selection by outcome sign is not representative sampling. Table 3 shows S comparisons; all four inputs and full trajectories are public.

| Trace / step | Module (chosen by) | temp | soc | imped | stress | S score | A2 score |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Gain / 25 | 3 (A2) | 0.456673 | 0.576453 | 0.224144 | 0.317894 | 0.488798 | 0.553402 |
| Gain / 25 | 4 (S) | 0.461809 | 0.571182 | 0.185761 | 0.308865 | 0.491274 | 0.544326 |
| Loss / 30 | 1 (S) | 0.540988 | 0.593125 | 0.262826 | 0.348180 | 0.583197 | 0.661141 |
| Loss / 30 | 4 (A2) | 0.462533 | 0.613333 | 0.301407 | 0.482664 | 0.574977 | 0.667408 |

*Table 3. Recorded normalized inputs and scores at the first action divergence from S. Gain is base seed 1200003, step 25; loss is seed 1200001, step 30. Steps and modules are one-based. Both policies have identical pre-action states at these points; values are rounded from full precision. The selected module has the highest score among all four modules. Scores are not rewards, and these are synthetic replay states, not physical measurements.*

In the gain trace, the added product moves A2 from S's module 4 to module 3: immediate reward rises from 0.757709 to 0.777924, and the full-trace mean margin is +0.004218. In the loss trace, A2 selects module 4 with higher soc, imped and stress instead of hotter module 1: reward falls from 0.884275 to 0.792774, and the full mean margin is -0.005861. Both examples have zero unnecessary-derating penalty and no floor clipping at that step.

The switching rule is explicit. Let t and x be normalized temperature and stress, p=soc*imped, and B=t+x cubed. For S's selected module b and A2's selected module a, a strict switch requires:

$$0 < B_b-B_a < 0.5(p_a-p_b).$$

The product advantage exceeds S's score disadvantage: 0.011553 versus 0.002476 in the gain example; 0.014487 versus 0.008220 in the loss. The same rule accompanies either outcome. Relative to C, the added score is 0.4*p; relative to N it is x cubed minus 1.5*max(x-0.5,0). In each case the difference of these added terms between a and b must overcome the alternative's score gap. This describes the selected pair; each policy still takes the maximum over all four modules. Exact ties retain the first module.

The reward uses raw states, whereas policy scores use normalized inputs. Write T, Q, I and X for raw temperature, charge, impedance and stress. For the chosen module, the code computes h=T+0.75*Q*I+0.45*max(X-0.95,0) before acting and D=0.50 only when both X<0.85 and T<0.75 (otherwise zero). The action multiplies its T by 0.45 and X by 0.5. Then P sums 0.4*T+0.28*Q*I across all four post-action modules. The step reward is:

$$r=\max(0.05,\;0.50+0.42h-D-0.14P).$$

Here h is a designed credit for selecting a high-index module, not measured heat removal. D penalizes an action on a low-state module; P penalizes remaining pack state. Let F be the amount added by the 0.05 floor. A2-minus-alternative mean reward decomposes exactly into 0.42 times the mean h difference, minus the mean D difference, minus 0.14 times the mean P difference, plus the mean F difference. These are signed accounting contributions along the observed paths, not causal interventions on individual terms or validated thermal protection.

![Replayed choices and cumulative reward differences](a2_replay.png)

*Figure 1. Cumulative raw reward differences from deterministic replay of existing test seeds. Dashed lines and dots mark the first differing action. Panels use the stated sign-conditioned rule, not the largest gains/losses. The N trace starts with an immediate loss at divergence but ends positive; the mean margin is the final cumulative difference divided by 320. Later paths may contain different states. All six trace pairs are available in the supplement.*

### 2.2 What All 600 Existing Seeds Show

We analyze reward components and the first differing action for all 600 saved seeds. Diagnostic definitions were fixed before analysis; the study and policy choices remain retrospective. Every A2/S, A2/N and A2/C pair eventually differs in action. First differences occur at median steps 14, 13 and 16 (ranges 1-90, 1-100 and 1-93). All 1,800 pairs have identical states before that action and satisfy strict score-gap identities, with no near ties or pairs that never diverge.

| A2 minus | Hazard credit | Action penalty | Pack penalty | Floor | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| S | +0.003572 | -0.000419 | -0.001517 | 0.000000 | +0.001635 |
| N | +0.000750 | -0.000471 | -0.000080 | 0.000000 | +0.000198 |
| C | +0.002263 | -0.000388 | -0.001219 | 0.000000 | +0.000656 |

*Table 4. Mean signed reward contributions over all 600 original seeds and all 320 steps, in raw reward units. Positive favors A2; a negative penalty contribution means A2 incurred more of that penalty. The four terms sum to the total before rounding, with maximum numerical residual 2.79e-15. The reward floor contributes zero under the original weights. Values are accounting under the fixed synthetic reward, not percentages or physical benefits.*

Against S, hazard credit improves on 500/600 seeds, but pack penalties worsen on 594/600. Penalties reduce the credit gain of +0.003572 to a net +0.001635. The net gain against N is only +0.000198; against C it is +0.000656.

The reward difference at the first differing action has the opposite sign to the full-path difference in 295/600 S, 308/600 N and 301/600 C comparisons. Against N, 272 of 528 initially losing traces finish ahead, versus 36 of 72 initially winning traces (51.5% versus 50.0%). These outcomes do not establish that A2 sacrifices an immediate gain for a later one: states can differ after the first different action. The supplement provides the full 3x3 matrices, all 1,800 first-difference records and component means grouped by overall gain or loss.

### 2.3 Reward-Weight Sensitivity and Final A2 Judgment

We rescore the same fixed trajectories with:

$$r_{a,b,c}=\max(0.05,\;0.50+0.42a h-bD-0.14cP).$$

We change only the three outer weights, keeping the internal definitions, constant, floor and policies fixed. Neither the policies nor the state transitions use reward as an input, so the same trajectories remain valid under the changed objectives. This retrospective analysis tests sensitivity to the objective; it does not retrain policies or model physical uncertainty.

Before calculation, we fixed one-at-a-time factors {0.5,0.75,1,1.25,1.5,2}, with the other two at 1, and all 27 joint combinations of {0.75,1,1.25}: 36 configurations after deduplication. We reapply the 0.05 floor at each step; reweighting Table 4 alone would miss clipping. All 86,400 policy-seed-configuration means exactly match direct reward-modified simulation, and the 2,400 original means remain exact. Changed objectives are compared using raw rewards, not the original-reference U.

Figure 2 shows the one-at-a-time results. Halving hazard-credit weight makes A2 last among the four policies: margins against S/N/C are -0.000140/-0.000163/-0.000466. Raising the action penalty to 1.5 times its weight puts N ahead (A2 margin -0.000024); doubling the pack penalty puts C ahead (-0.000561). Each individual +/-25% weight change keeps A2's mean first, but simultaneous changes need not. In the joint cube, A2 is first in 22 configurations, second in three and third in two. Its mean exceeds S in 27/27, N in 23/27 and C in 24/27; there are no mean ties. These counts describe chosen grid points, not robustness probabilities or a continuous guarantee.

![Reward-weight sensitivity of fixed policies](reward_sensitivity.png)

*Figure 2. Mean A2-minus-alternative raw reward under all six one-at-a-time factors, using the same 600 seeds per point. Values are multiplied by 1,000 for legibility, not percentages. Dotted vertical lines mark original weights; horizontal zero marks equal mean. Lines connect evaluated grid points without certifying intervening behavior. The complete 36 configurations, clipping counts and per-seed results are public.*

**Final judgment:** A2 merits further study under a specified objective in this synthetic setting. Compared with S, it has a higher mean reward under the original weights, but uses six more nodes and loses on some seeds. Compared with N, it uses two fewer nodes and has a small mean advantage. A2 and C have equal size but different weights. The preferences over N and C can reverse even within the joint +/-25% grid, so A2 is not a default replacement or a reward-independent winner. We have not established an acceptable-loss threshold or a deployment-cost benefit. A1's evaluation changes with the set of alternatives; A2's changes with the objective.

### 2.4 A1: Broader Comparison Changes the Judgment

A1 ranks synthetic queues by adding the smaller of drift and burst to queue, then subtracting half idle. Both signals must be high for a large added priority. This exact minimum coupling is absent from H. 

Within the same block, A1 initially looks preferable: nine nodes and test U=1.003905 versus 13 nodes and U=1.000870 for N_ROLE. Comparing all original winners reveals the seven-node neutral alternative in Table 1. This broader comparison weakens the case for adopting A1, even though its minimum rule is easy to explain (Section 3).

The saved sequence shows `queue+min(drift,burst)-0.25*idle` in round 2 slot 6. After this output and its feedback are supplied, round 3 changes -0.25 to -0.5. We can observe the revision but cannot infer the model's internal rationale.

### 2.5 A5: Above Reference Is an Incomplete Adoption Argument

A5 changes the coefficients of a supplied queue template and omits burst. Its test U=1.002104 exceeds the simple reference, but the matched neutral expression in Table 1 reaches 1.003917 with seven nodes/depth 2 versus nine/depth 3. We therefore give A5 lower priority for further study; this does not make it a failed generation. Section 3.2 reports the paired outcomes.

A5 was fixed by the low-selection rule, not chosen for a poor test outcome. The preceding round has `queue*(0.4+drift)-0.3*idle`; A5 revises the coefficients after feedback.

### 2.6 A3 and A4: Supplied Structures Remain Visible

A3 adjusts idle with an upper-capped frequency term and positive jitter, both supplied in H. For freq below 0.5, subtracting the negative min term adds a bonus; at freq at least 0.75 the contribution is fixed at -0.0875. Earlier rounds use cap weights 1 and 0.6; A3 uses 0.35. Test U=1.000466 and depth 4, above the soft target of 3, make it a low-priority diagnostic rather than evidence of cloud-cost savings.

A4 combines the supplied temperature, soc*imped and threshold terms, doubling the threshold weight. The preceding round contains both the doubled threshold without the product and the product with weight one. Test U=1.009928 exceeds the matched X_ROLE winner's 1.008923, with 13 nodes/depth 4 versus 11/depth 3. It is an X_FLAT assembly/control example, not a newly established domain connection.

## 3. Comparison with All Original Winners

### 3.1 Position among Original Winners and All Submissions

We rank the fixed cases among 30 original winners per task, separately on selection and test data, keeping each task's utilities separate. Duplicate outcomes remain: Network and Thermal have 28 and 26 distinct strings. Rank is one plus the number of strictly higher utilities (tolerance 1e-12). These ranks describe the saved policies; they do not estimate the effect of a generation condition.

An alternative dominates a policy in size and reward if it uses no more nodes and has no lower utility, with a strict advantage in at least one measure. We assess each split separately. Even tiny differences can change this status because the rule has no threshold for practical importance.

A2 ranks 1/30 on both splits and is not size-reward dominated on either; A1 ranks 5/30 and is dominated on both. Among all submitted occurrences, A2 ranks 1/360 on selection and 1/306 available tests; A1 ranks 7/360 and 7/327. The 54 Thermal and 33 Network submissions without tests are not failures. Available-test ranks are not ranks over all 360 submissions.

A2's test U=1.011170 exceeds the simpler cubic alternative's 1.009897, but it uses 13 rather than seven nodes; neither dominates the other. A1's two dominators are instances of the same seven-node expression, from Network N_ROLE block 5 and N_FLAT block 6. Its test U=1.003917 is only about 0.000012 above A1, and the selection advantage is approximately 4.38e-8. The smaller expression drives the preference; the score difference has no demonstrated practical importance. We identify the first instance by session ID. Both have identical formulas and stored traces.

Test coverage follows the original evaluation procedure, not random sampling. Public files retain all 90 winner ranks/dominators. The 360-submission view supplies ranks only; per-seed comparisons concern original winners.

### 3.2 Average Gains and Observed Downside

For each case, we subtract each same-task alternative's raw reward using the identical saved seed. There are 30 comparisons including self, plus the reference, giving 62 comparisons across A1/A2. We distinguish within-block contrasts from comparisons with other blocks: the latter compare fixed policies rather than paired generation interventions. Each comparison requires 600 matching seeds and equal references.

A win has a difference above 1e-12; a tie is within that tolerance. Table 5 shows the mean difference, the mean of the 30 lowest differences (observed bottom 5%) and the largest observed loss. These are task-specific raw-reward quantities, not percentages. They describe this set of traces, not a bound on future risk or 600 independent model generations.

| Case | Comparator | Wins/ties/losses | Mean difference | Lowest-30 mean | Largest loss |
| --- | --- | --- | ---: | ---: | ---: |
| A2 | Reference | 599/0/1 | +0.014354 | +0.005077 | 0.000154 |
| A2 | S: X_FLAT B5, 7 nodes | 390/0/210 | +0.001635 | -0.006591 | 0.010608 |
| A2 | N: N_FLAT B6, 15 nodes | 308/0/292 | +0.000198 | -0.006281 | 0.008701 |
| A2 | C: X_FLAT B2, 13 nodes | 342/0/258 | +0.000656 | -0.006834 | 0.012074 |
| A1 | Reference | 514/0/86 | +0.003800 | -0.003681 | 0.007333 |
| A1 | N_ROLE B4: same block | 402/0/198 | +0.002953 | -0.004802 | 0.009958 |
| A1 | N_ROLE B5: simpler | 9/569/22 | -0.000012 | -0.000306 | 0.001276 |

*Table 5. Gain and downside on saved common-seed traces. B denotes block. A negative lowest-30 mean indicates losses in that tail; largest loss is reported as a positive magnitude. The A1 seven-node comparator is identified by the selection-data dominance relation, not by searching test outcomes. The full supplement retains all 62 comparisons, medians, fifth percentiles and conditional gains/losses. S/N/C do not add comparisons to that set; their new step records come from local replay.*

For the other fixed cases, A3 versus reference has 359 wins, no ties and 241 losses, with mean raw margin +0.000412; A4 has 599/0/1 and +0.012758. A5 versus its same-block N_ROLE alternative has 270/2/328 and -0.001764. Their complete matched-condition records are available in the supplement.

Gain/loss contributions explain the averages. For A2 versus the simpler cubic rule, +0.002580 gain contribution minus 0.000945 loss contribution gives +0.001635. Against the same-block N_ROLE winner, A1's +0.003617 minus 0.000664 leaves +0.002953; against the smaller cross-block rule, +0.00000355 minus 0.00001530 gives -0.00001176. Contributions divide all positive and absolute negative differences by 600, including differences within the tie tolerance; the supplement also gives conditional averages over only the corresponding signed cases.

Equal rewards can come from different actions. Comparing complete formulas also leaves the separate effects of min and cubic terms unresolved. The observed losses inform our judgments in Section 2, but we specified no acceptable-loss or minimum-useful-gain threshold.

### 3.3 Interesting Structures Are Not Exclusive to Cross-Domain Roles

We also audit two explicitly defined motifs throughout the complete saved catalogue. After removing whitespace, we search for the exact substrings `min(drift,burst)` in Network and `stress*stress*stress` in Thermal. This is a narrow, reproducible string census, not semantic clustering or an exhaustive search for algebraically equivalent rules. Counts are retrospective and were chosen because of A1/A2.

The minimum motif appears in four X_ROLE submissions from one session, one N_ROLE submission from one session and one X_FLAT submission from one session. It is absent under this literal rule in N_FLAT and DOMAIN_V2. The cubic motif appears in seven X_FLAT submissions from five sessions, three N_FLAT submissions from one session and two X_ROLE submissions from one session; it is absent under the rule in N_ROLE and DOMAIN_V2. Each task/condition has six sessions and 72 submissions. Repeated submissions from a session are not independent discoveries.

A structure can be absent from H and perform well in a selected comparison while also occurring under neutral instructions. The minimum and cubic motifs therefore do not establish that biological, HCI or design knowledge caused these terms.

### 3.4 Complete Collection and Retrospective Selection

All 1,080 submissions pass the recorded validity gate, with 822 distinct within-domain exact strings (spacing/algebraic variants remain separate), 916 component representative instances and 90 original winners. The catalogue retains every occurrence with complete prompt/response provenance, syntax, selection status, component and scores. Tests exist for 944 submissions; 136 remain untested, not failed.

Readers can search the offline catalogue by expression, provenance and score. Its syntactic tags identify forms; they do not measure semantic novelty or cognitive processes. Each case card shows the exact H alongside the output.

We fix three core cases: the original X_ROLE session winner with highest selection utility in each domain. Ties use nodes, depth, session ID and slot ID in ascending order. One X_FLAT complement is selected from original winners with a tag combination absent from the core cases, using Network-Thermal-Cloud domain order and the same ranking within the first eligible domain. One low-selection X_ROLE example uses that domain order, minimum selection utility, and the same tie rules after excluding already used domain/expression pairs. A missing eligible complement would be omitted.

The selection function uses only selection/provenance/syntax fields. It writes case IDs and a rule hash before attaching test values, without replacing cases afterward. We nevertheless devised the rule after inspecting pilot results. These are post-hoc descriptions, not five prevalidated successes or the global best five outputs. Matched rows contain the original winners of all five conditions in the same domain/block. Full inclusion/exclusion logs are public.

## 4. Inputs, Generation, and Evaluation

### 4.1 Source Perspectives and Target Tasks

X/N mean cross-domain/neutral wording; ROLE/FLAT distinguish separate/combined guidance. H marks supplied hints. A block pairs conditions within a task; winners are chosen before test. U is reward relative to the reference (U=1); nodes measure formula size, not runtime. A trace has 320 simulated steps, not an independent generation.

Biological/HCI and design instructions guide rule generation for Network, Thermal and Cloud. Network ranks four synthetic queues, Thermal ranks four synthetic modules for derating, and Cloud ranks six synthetic slots for reclamation. The expression scores each option and selects the highest-scoring one. We normalize features to [0,1] by clipping negative raw values at zero and applying x/(1+x). Ties retain the first option.

Expressions use four task variables, constants, arithmetic, min, max, and abs. All conditions share a hard gate of 25 AST nodes and implemented depth 5, with soft targets of 14 nodes and depth 3. Recorded depth flattens additive/subtractive and multiplication chains; it is not ordinary binary-tree height. Each environment trace has 320 steps, with handcrafted transitions and rewards; task names do not imply validated physical or production systems.

The four factorial conditions share the hints in Table 7. The cross-domain instruction asks the model to interpret them through biological immune-adaptation and HCI reframing analogies, using minimalist industrial-design inspiration for concise expressions. ROLE assigns exploration and simplicity distinct functions within the same response; FLAT presents both together. These are prompt instructions, not observed internal stages. DOMAIN_V2 omits H and changes the guidance procedure, so it is descriptive rather than a single-module ablation.

| Condition | Framing | Organization | H |
| --- | --- | --- | --- |
| N_FLAT | Neutral | Combined | Yes |
| N_ROLE | Neutral | Roles | Yes |
| X_FLAT | Cross-domain | Combined | Yes |
| X_ROLE | Cross-domain | Roles | Yes |
| DOMAIN_V2 | Domain | Base | No |

*Table 6. Conditions. Every factorial arm includes exploration and simplicity guidance. Roles are textual within one response.*

| Task | Shared mathematical hints H |
| --- | --- |
| Network | `queue*(0.45+drift)`; `max(burst-idle,0)`; negative idle term |
| Thermal | `soc*imped`; `max(stress-0.5,0)`; temperature term |
| Cloud | `cost*freq`; `min(freq-0.5,0.25)`; positive jitter with idle |

*Table 7. H is supplied to all four factorial conditions within a task. The Cloud min term is an upper cap, not a lower clamp. Exact complete prompts and their verbatim differences are public.*

### 4.2 Recorded Generation and Evaluation

The pilot ran on 24 October 2026 (KST), requesting gpt-6.1-sol with low reasoning effort through Codex CLI 0.162.1. Three domains, six paired blocks per domain, and five conditions give 90 separately initialized sessions. Randomized condition order within domain/block and four rounds of three expressions yield 360 responses and 1,080 slots. Each session receives only its own prior answers and feedback. The required response is an expression array without explanatory commentary, so the record does not reveal the model's internal rationale.

Experimental message roles were serialized into one CLI input, rather than native API roles. Prompt length, semantics and token use were not exactly matched, and the requested 2,048-token output cap was not enforced. The contrasts therefore compare recorded instruction packages, not perfectly resource-matched interventions or verified server snapshots.

Feedback, selection and test use disjoint base seeds: 48 (1000001-1000048), 96 (1100001-1100096), and 600 (1200001-1200600), with fixed Thermal/Cloud offsets. Selection starts after generation, and selected policies and representatives are frozen before test access. Independent generation comparisons use sessions; each session's 12 submissions are dependent.

The reference expressions are queue+0.45*drift+0.15*burst-0.15*idle for Network, temp+0.4*soc+0.35*imped+0.25*stress for Thermal, and idle for Cloud. Historical labels Adaptive-PI, PID-lite, and Fixed-TTL denote simplified synthetic formulas, not full implementations of those methods. Utility U is the policy's mean trace reward divided by the reference's mean reward on the same domain/split; the reference has U=1. This ratio is not an average of per-trace ratios. References are comparison points, not optima or tuned published competitors.

We group behavior using the saved graph on a fixed four-value-per-coordinate grid and 500 diagnostic option panels. An edge requires Spearman score correlation above 0.98 and top-action agreement of at least 95 percent. Connected components may include transitive chains, so they describe groups within a session on finite probes, not globally unique ideas. We select each component's representative and the session winner by selection mean reward, breaking ties by expression hash and slot, then evaluate them on test data.

The original primary outcome counts representatives with U at least 0.99. This near-reference criterion includes below-reference policies and sets no threshold for practical improvement. Strict exceedance uses U greater than 1+1e-9. We froze the analysis locally before test access, without public preregistration.

## 5. Aggregate Evidence and Boundaries

Across the original experiment, equal-domain averaging of six within-block contrasts gives -0.1111 near-reference components per session for X_ROLE minus N_ROLE. The Network, Thermal and Cloud means are -0.6667, +0.1667 and +0.1667, with paired SDs 2.9439, 2.2286 and 4.4907. Figure 3 shows all 18 differences. Generation comparisons use six paired blocks per domain; the test traces do not enlarge that sample. The selected cases must be read alongside these aggregate results.

![Original paired near-reference differences](paired_differences.png)

*Figure 3. Original X_ROLE minus N_ROLE near-reference counts by block and domain. Selected artifact examples must be read alongside this mixed aggregate result.*

| Outcome | X_ROLE−N_ROLE | X_ROLE−X_FLAT | Interaction |
| --- | ---: | ---: | ---: |
| Primary count | −0.1111 | −0.5556 | −1.2222 |
| Strict-exceedance count | +0.3333 | +0.6667 | +0.3889 |
| All-pairs count | −0.0556 | −0.4444 | −1.1111 |
| Selected-policy utility | +0.000998 | −0.000144 | +0.000062 |

*Table 8. Preserved aggregate comparisons. Interaction is (X_ROLE−X_FLAT)−(N_ROLE−N_FLAT). Counts and utility answer different questions. The utility contrast is not a relative percentage gain.*

The retrospective profiles describe complexity and diversity across conditions. Relative to N_ROLE, X_ROLE has 0.5370 more mean nodes and 0.3889 fewer pre-threshold components per session; relative to X_FLAT, the differences are +0.8148 and -0.4444. The node difference is mainly Thermal (+1.5556), with Network -0.1667 and Cloud +0.2222. Session means include all 12 submissions, including repeats. These profiles do not show an aggregate simplicity-diversity advantage or identify a compression process. Full tables and figures are in the supplement.

The Cloud results show why meeting the near-reference threshold differs from improving on the reference. Of 304 representative instances, 178 are below 0.99, 118 lie from 0.99 through 1, and eight strictly exceed 1+1e-9, between 1.000012 and 1.000541. Thus 126 meet the near-reference threshold, but only eight exceed the reference; 25 of 30 originally selected Cloud policies are below it. No representatives cross either threshold between the saved selection and test splits. Selection bias and the source of the generated rules remain unresolved.

All cases share the study's limits: one requested model/effort, one wording per condition, six paired blocks per task, shared H overlapping reward features, handcrafted transitions/rewards and simple references. Actual token budgets were not matched. Every factorial arm includes both guidance functions, leaving no exploration-only, design-only or bare-length controls. The retrospective case rule does not provide a representative sample. Test ranks and observed losses are descriptive; we provide no confidence intervals, equivalence decisions, user ratings or deployment evidence.

The catalogue and replay expose the outputs and their tradeoffs, but cannot establish which source-domain knowledge produced a term or whether cross-domain wording caused it. Neutral-condition motifs and mixed aggregate results limit that interpretation. The supplied soc*imped hint overlaps the raw-variable product in the handcrafted reward, which also uses temperature and a stress threshold. Replay explains choices within this design; separating domain-guidance effects and establishing practical benefit require further evidence.

## 6. Conclusion and Reproduction

We examined task rules generated under combined cross-domain guidance and the reasons to retain them. A2 has the highest original observed Thermal mean, but gains come with larger penalties. Its lead over N/C can reverse within the joint +/-25% grid. It merits further study under a specified objective, without deployment evidence. A1's appeal weakens under broader comparison.

We trace supplied inputs, generated changes and judgments about the rules. The five retrospective cases, neutral-condition structures and mixed aggregate results leave biological/HCI knowledge transfer, algorithmic novelty and practical utility unestablished.

The paper (v1.10.3), source and supplementary evidence are public: [https://github.com/7065616b/symbolic-policy-framing-pilot](https://github.com/7065616b/symbolic-policy-framing-pilot). The supplement includes original prompts, outputs and replay records. Reusing policies and test seeds provides no independent observations. Model regeneration is not guaranteed without server snapshots and sampling seeds.

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

We examine task skills generated when an AI is asked to combine perspectives from different fields. A skill here is a small executable rule that selects an option. Biological/HCI exploration and minimalist-design guidance share one prompt with task facts, mathematical hints, a grammar and feedback. We ask what rules were produced and which merit further study; a causal benefit from combining domains remains unestablished.

### Novelty

We show which elements were supplied, what changed in the generated rules and how the alternatives affect each judgment. A2's evaluation changes with reward weights; A1's changes with the comparison set. These retrospective cases do not establish a new algorithm, mathematical invention, module synergy or causal domain transfer.

### Algorithms

The original 90 sessions yield 1,080 submissions with separate feedback, selection and test data. The five case IDs and original winners stay fixed regardless of presentation order. A1/A2 comparisons cover all 30 original winners in their task and 62 common-seed comparisons. Ranks across all 360 task submissions disclose missing test values. Replaying four saved policies on the original 600 seeds exactly reproduces all 2,400 saved rewards.

We analyze reward components and the first differing action for all 1,800 comparator-seed pairs; six sign-conditioned pairs illustrate full trajectories. These analyses add no independent observations. Thirty-six fixed weight configurations rescore the same paths with the floor applied at each step; all 86,400 scores match direct reward-modified simulation.

### Experiments

A2 ranks first among 30 Thermal winners on both saved splits. Against the seven-node cubic alternative, its 13-node expression has mean raw margin +0.001635, 390 wins and 210 losses, with largest observed loss 0.010608. Against the strongest selection-ranked neutral winner, A2 has 308 wins and 292 losses, with mean margin +0.000198 and 13 versus 15 nodes. Against N, 272/600 traces finish positive after an initially negative margin, while 36 do the reverse; the mean hazard-credit gain is largely offset by penalties. 

A1 ranks fifth among 30 Network winners; two instances of a smaller neutral rule have slightly higher means, and the paired results against that rule are 9 wins, 569 ties and 22 losses. A2 ranks first of 360 submissions on selection and first of 306 tested occurrences; A1 ranks seventh of 360 and seventh of 327. 

The original X_ROLE minus N_ROLE primary contrast remains -0.1111 near-reference components per session, with strict exceedance +0.3333. Neutral-condition motifs, shared hints, one requested model, six blocks per task, synthetic environments and retrospective emphasis limit interpretation. A2 ranks first among four fixed policies in 22/27 joint +/-25% weight configurations, but loses to N in four and C in three; halving hazard-credit weight makes it last. Grid counts are not probabilities. A2 remains a conditional follow-up candidate; causal cross-domain effects and practical utility remain unresolved.

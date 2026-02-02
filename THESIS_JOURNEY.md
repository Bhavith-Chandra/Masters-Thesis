# Research Narrative: From Sensor Noise to Behavioral Causal Discovery

This document serves as the "Master Narrative" for the 1-hour thesis dissertation meeting. It chronicles the methodological journey from raw data auditing to high-granularity structural modeling and ML-driven reasoning extraction.

---

## 📍 Phase 1: The Complexity Floor (The "Why")
**Objective**: To justify the transition from high-dimensional sensor data to structured causal reasoning.

- **The Discovery**: We began with an audit of the GLOBEM dataset, identifying **11,040 features** across 8 modalities (Sleep, Steps, Location, Screen, Social, etc.).
- **Scientific Decision**: We rejected "toy models" and "naive ML". We identified that a DAG over raw features is impossible.
- **The Protocol**: We established a strict **5-line-per-cell discipline** combined with **🧠 Interpretation** blocks to ensure every methodological step was scientifically documented, not just executed.

## 📍 Phase 2: Outcome Scrutiny & Stability
**Objective**: Selecting a robust ground-truth for depression.

- **The Audit**: We compared `dep`, `BDI2`, and weekly subscales.
- **Scientific Decision**: We selected **`dep` (Global Depression)**. While it correlated highly with `BDI2` (>0.8), it provided the most stable longitudinal signal across the 4-week window, serving as our "Sink Node" for all causal flows.

## 📍 Phase 3: High-Granularity Mechanical Discovery
**Objective**: Avoiding premature abstraction (Pre-latent recovery).

- **The Problem**: Traditional researchers use single variables like "Sleep Quality" or "Activity Level".
- **The Innovation**: We performed a **Decomposition Audit**. We broke modalities into independent mechanisms:
    - **Sleep**: Duration vs. Efficiency vs. Latency.
    - **Mobility**: Home Time vs. Entropy vs. Distance.
    - **Social**: Incoming vs. Outgoing vs. Unlock Freq.
- **Scientific Decision**: By retaining 16 granular variables, we prevented the information loss of over-aggregation.

## 📍 Phase 4: Constructing the "Human" Atlas
**Objective**: Assembling the generalized behavioral DAG.

- **The Association Floor**: We generated a **16x16 Grand Association Matrix**, documenting the empirical correlation between every behavioral node.
- **The Logic**: We used **Temporal Precedence** and **Behavioral Science** to argue for 20+ edges. For example:
    - *Unlock Frequency* → *Sleep Latency* (Digital stimulation delaying sleep).
    - *Distance Travelled* → *Social Outreach* (Mobility facilitating social calls).
- **The Result**: A 16-node, peer-review-grade directed acyclic graph.

## 📍 Phase 5: ML Reasoning Extraction (The Contrast)
**Objective**: Treating ML Models as "Reasoning Agents".

- **The Question**: Does a machine "see" behavior the same way a human theorist does?
- **The Method**: We extracted 4 structurally distinct DAGs:
    - **Linear Regression (Accumulative Logic)**: Identified the "Mutable Core" via Lasso Stability Selection.
    - **Random Forest (Shortcut Logic)**: Used **SHAP (Shapley Additive Explanations)** to uncover non-linear "shortcuts" where machines skip human-assumed mediators.
    - **SVM (Relational Logic)**: Mined interactions where behaviors jointly determine the outcome.
    - **KNN (Contextual Logic)**: Modeled patterns as local similarity neighborhoods.

## 📍 Phase 6: Quantitative Structural Synthesis
**Objective**: Proving the "Global Behavioral Anchors".

- **Structural Metrics**: We used **Graph Edit Distance (GED)** to quantify exactly how much machine reasoning deviates from human logic.
- **Hub Analysis**: Using **PageRank Centrality**, we proved that despite the differing "logic" of these models, they all converge on **Home Time** and **Sleep Duration** as the "Invariance Core" of behavioral health.

---

## 🎓 Key Dissertation Defense Points
1. **Methodological Rigor**: 11,000 features reduced to 16 through principled mechanical decomposition, not arbitrary selection.
2. **Structural Discovery**: The DAG is not just a demo; it is an eco-systemic model of behavioral health.
3. **Machine vs. Human**: The project proves that while ML models are excellent predictors, their internal "logic" (DAG) often highlights different structural paths than human theory, suggesting new areas for research.

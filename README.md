# MiroFish × Volt: Simulated-Reality Multi-Agent Research Laboratory

[![Status](https://img.shields.io/badge/Status-Completed-success.svg)](#)
[![Simulation Engine](https://img.shields.io/badge/Engine-MiroFish%20OASIS-blue.svg)](https://github.com/666ghj/MiroFish)
[![Product Under Study](https://img.shields.io/badge/Product-Volt-ff69b4.svg)](https://volt.qmatus.com/)
[![Reports](https://img.shields.io/badge/Reports-13%20Generated-purple.svg)](#research-reports-index)
[![Audit](https://img.shields.io/badge/Audit-Passed%20(Scientific%20Heuristic)-green.svg)](volt-mirofish-research/research/reports/FINAL_RESEARCH_QUALITY_AUDIT.md)

An autonomous multi-agent simulation research laboratory investigating developer, enterprise, and market reactions to **Volt** (`https://volt.qmatus.com/`), powered by the **MiroFish** OASIS multi-agent social engine.

---

## 1. Architectural Independence Principle

**Volt** is an independently deployed product. **MiroFish** was used strictly as an external, simulated-reality research environment:
- Zero integration between MiroFish and Volt.
- No modifications to Volt source code, production database, or deployment.
- No MiroFish dependencies installed inside Volt.

```
┌─────────────────────────────────┐         ┌─────────────────────────────────┐
│              VOLT               │         │        MIROFISH ENGINE          │
│   https://volt.qmatus.com/      │         │   Autonomous OASIS Simulation   │
│   • CLI & Local SQLite buffer   │         │   • 30 Heterogeneous Personas   │
│   • PostgreSQL Ledger           │ <---x-- │   • Reddit Social Dynamic Sim   │
│   • Mathematical Weighting      │ (No     │   • Upvotes, Posts, Comments    │
│   • Production Cloud (Fly.io)   │ Connect)│   • Qualitative Red-Teaming     │
└─────────────────────────────────┘         └─────────────────────────────────┘
```

---

## 2. Repository Layout

```
mirofish-volt/
├── README.md                                  # Master project overview and index
├── .gitignore                                 # Clean exclusion rules (no venv, node_modules, .env)
└── volt-mirofish-research/
    ├── documentation/
    │   └── RESEARCH_RUNBOOK.md                # Environment, verification, and execution runbook
    ├── mirofish/                              # Official MiroFish engine (commit 7657031ac0)
    │   ├── backend/                           # Flask, OASIS engine, CAMEL integration
    │   └── frontend/                          # Vite + Vue3 UI
    ├── research/
    │   ├── product-intelligence/
    │   │   └── VOLT_PRODUCT_DOSSIER.md        # Technical breakdown of Volt
    │   ├── reality-seeds/                     # 8 neutral reality context seeds
    │   │   ├── SEED_1_PRODUCT_CONTEXT.md
    │   │   ├── SEED_2_MARKET_CONTEXT.md
    │   │   ├── SEED_3_USER_PSYCHOLOGY.md
    │   │   ├── SEED_4_COMPETITIVE_LANDSCAPE.md
    │   │   ├── SEED_5_ADOPTION_AND_RESISTANCE.md
    │   │   ├── SEED_6_ORGANIZATIONAL_DYNAMICS.md
    │   │   ├── SEED_7_CRITICAL_PERSPECTIVES.md
    │   │   └── SEED_8_HYPOTHETICAL_DISCOVERY.md
    │   ├── personas/
    │   │   ├── personas.json                  # 30 rich, diverse agent archetypes
    │   │   ├── reddit_profiles.json           # OASIS-formatted Reddit agent profiles
    │   │   └── PERSONAS_OVERVIEW.md           # Segmentation matrix
    │   ├── simulation-results/                # Raw SQLite databases, JSON, and CSV traces
    │   │   ├── exp_a_organic_discovery/       # 30 agents, 2 posts, 18 comments, 164 traces
    │   │   ├── exp_b_critical_evaluation/     # 30 agents, 7 posts, 11 comments, 25 likes, 157 traces
    │   │   └── exp_c_organizational_adoption/ # 30 agents, 3 posts, 27 comments, 109 traces
    │   └── reports/                           # 13 research reports & final audit
    └── scripts/
        ├── generate_personas.py               # Persona generator
        └── run_research_experiment.py         # Autonomous simulation executor
```

---

## 3. The 3 Controlled Experiments

| Scenario | Objective | Agents | Posts | Comments | Likes | Total Traces |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **Exp A: Organic Discovery** | Initial organic perception of CLI speed and timesheet replacement | 30 | 2 | 18 | 3 | 164 |
| **Exp B: Critical Red-Teaming** | Adversarial stress-testing of Goodhart's law and surveillance dread | 30 | 7 | 11 | 25 | 157 |
| **Exp C: Org Adoption Trial** | Evaluation of company-wide rollout and custom manager rubrics | 30 | 3 | 27 | 7 | 109 |

---

## 4. Research Reports Index

All 13 research reports generated from the simulation are available in `volt-mirofish-research/research/reports/`:

1. **[FINAL_RESEARCH_QUALITY_AUDIT.md](volt-mirofish-research/research/reports/FINAL_RESEARCH_QUALITY_AUDIT.md)**: Forensic audit of raw SQLite databases, trace counts, hyperbolic claims, and honest product guidance.
2. **[EXECUTIVE_SUMMARY.md](volt-mirofish-research/research/reports/EXECUTIVE_SUMMARY.md)**: High-level findings, strategic matrix, and empirical insights.
3. **[VOLT_PRODUCT_PERCEPTION.md](volt-mirofish-research/research/reports/VOLT_PRODUCT_PERCEPTION.md)**: Speed vs. surveillance dichotomy and junior developer panic.
4. **[USER_PERSONA_ANALYSIS.md](volt-mirofish-research/research/reports/USER_PERSONA_ANALYSIS.md)**: Archetype behavior across individual users, founders, skeptics, and opinion formers.
5. **[ADOPTION_AND_REJECTION_ANALYSIS.md](volt-mirofish-research/research/reports/ADOPTION_AND_REJECTION_ANALYSIS.md)**: Primary signals driving adoption ("Yes") vs. rejection ("No").
6. **[COMPETITIVE_POSITIONING.md](volt-mirofish-research/research/reports/COMPETITIVE_POSITIONING.md)**: Volt vs. Harvest/Clockify, Hubstaff, LinearB, and Jira Story Points.
7. **[PRODUCT_WEAKNESSES.md](volt-mirofish-research/research/reports/PRODUCT_WEAKNESSES.md)**: Vulnerability analysis (Goodhart's law, invisible work discount, zero-sum competition).
8. **[PRODUCT_RECOMMENDATIONS.md](volt-mirofish-research/research/reports/PRODUCT_RECOMMENDATIONS.md)**: Strategic marketing pivot and rubric engine enhancements.
9. **[SOCIAL_DYNAMICS.md](volt-mirofish-research/research/reports/SOCIAL_DYNAMICS.md)**: Emergent upvote clustering and peer influence in Exp B.
10. **[EXPERIMENT_COMPARISON.md](volt-mirofish-research/research/reports/EXPERIMENT_COMPARISON.md)**: Cross-scenario synthesis from curiosity to operational debate.
11. **[REAL_WORLD_VALIDATION_PLAN.md](volt-mirofish-research/research/reports/REAL_WORLD_VALIDATION_PLAN.md)**: 4 empirical experiments to validate simulation findings in the real world.
12. **[METHODOLOGY.md](volt-mirofish-research/research/reports/METHODOLOGY.md)**: Complete simulation pipeline, mathematical formulas, and OASIS architecture.
13. **[LIMITATIONS_AND_BIAS_AUDIT.md](volt-mirofish-research/research/reports/LIMITATIONS_AND_BIAS_AUDIT.md)**: LLM prior biases, articulation bias, and simulated echo chambers.

---

## 5. Executive Takeaway for Volt's Founders

```
                       WHAT TO TRUST VS. WHAT TO DISREGARD
┌──────────────────────────────────────────────┬──────────────────────────────────────────────┐
│  TRUST & ACT UPON (High Qualitative Signal)   │   DISREGARD (Zero Quantitative Validity)     │
├──────────────────────────────────────────────┼──────────────────────────────────────────────┤
│ 1. Goodhart's Law commit-gaming vulnerability│ 1. "Unanimous approval" or percentage shares │
│ 2. Designer/marketer alienation from CLI/Git │ 2. Pricing elasticity ($29 vs $99 pricing)   │
│ 3. Contractor fear of unexplainable invoices │ 3. Enterprise IT procurement compliance claims│
│ 4. "Invisible work" penalty (refactoring/QA) │ 4. Conversion rates and sales cycle duration │
│ 5. Managerial burden of rubric calibration   │ 5. Simulated agent "willingness to buy"      │
└──────────────────────────────────────────────┴──────────────────────────────────────────────┘
```

### Actionable Product Directives:
1. **Never Brand as an "AI Payroll Judge":** Automated compensation grading triggers acute cultural antibodies (*"Digital Taylorism"*). Position Volt as an **Effort Proof & High-Fidelity Developer Log** that empowers contributors, leaving compensation decisions to humans.
2. **Log "Invisible Engineering":** Introduce native primitives for uncommitted work: `volt log --meeting`, `volt log --mentoring`, `volt log --review`.
3. **Build a Visual Quick-Entry Overlay:** Non-technical teammates (designers, growth marketers) will not adopt terminal CLIs.
4. **Contractor Invoice Exporter:** Translate complexity weightings into predictable hourly breakdowns for external client billing.

---

## 6. Reproducibility & Quick Start

### Prerequisites
- Python 3.12+ with `uv`
- Node.js 18+ and `npm`
- An OpenAI-compatible LLM endpoint (Gemini Flash, OpenAI, or Ollama)

### Reproduce Simulation
```bash
cd volt-mirofish-research/mirofish/backend
uv run python scripts/run_reddit_simulation.py \
    --config ../../research/simulation-results/exp_a_organic_discovery/simulation_config.json \
    --profiles ../../research/personas/reddit_profiles.json \
    --output-dir ../../research/simulation-results/reproduced_exp
```

Full details are documented in [RESEARCH_RUNBOOK.md](volt-mirofish-research/documentation/RESEARCH_RUNBOOK.md).

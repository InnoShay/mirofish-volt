# MIROFISH x VOLT RESEARCH LABORATORY: REUSABILITY RUNBOOK
**Document ID:** VOLT-DOC-RUNBOOK-01  
**Target Audience:** Research Engineers, Product Managers & DevOps Team  
**Workspace:** `/Users/demo/mirofish/volt-mirofish-research/`  

---

## 1. ENVIRONMENT OVERVIEW & ARCHITECTURE
This research lab operates an independent installation of **MiroFish** (upstream commit `7657031ac01184afe2cb220f5ee3545573b5e843`) powered by the **OASIS** social simulation engine and Google Gemini Flash models via an OpenAI-compatible endpoint.

```
volt-mirofish-research/
├── mirofish/                      # Upstream MiroFish Engine
│   ├── backend/                  # Flask REST API (Port 5001) & OASIS Engine
│   ├── frontend/                 # Vite + Vue 3 Web UI (Port 3000)
│   └── .env                      # LLM API configuration (Gemini endpoint)
├── research/
│   ├── product-intelligence/     # VOLT_PRODUCT_DOSSIER.md
│   ├── reality-seeds/            # 8 Reality Seed Documents
│   ├── personas/                 # 30 Generated Agent Personas (JSON & Markdown)
│   ├── experiments/              # Experiment configurations & DBs
│   ├── simulation-results/       # Exported JSON and CSV trace data
│   └── reports/                  # 12 Formal Research Deliverables
├── documentation/                # Research Runbook & System Guides
└── scripts/                      # Orchestration & Generation Scripts
```

---

## 2. SYSTEM CONTROL: START & STOP

### Starting MiroFish
To run the full native MiroFish web interface:
```bash
# Terminal 1: Start Backend (Port 5001)
cd /Users/demo/mirofish/volt-mirofish-research/mirofish/backend
uv run python run.py

# Terminal 2: Start Frontend (Port 3000)
cd /Users/demo/mirofish/volt-mirofish-research/mirofish/frontend
npm run dev -- --port 3000
```
- **Web UI:** `http://localhost:3000`
- **Backend API:** `http://localhost:5001`
- **Health Check:** `curl http://127.0.0.1:5001/health` (Returns `{"service":"MiroFish Backend","status":"ok"}`)

### Stopping MiroFish
```bash
# Identify and kill running processes
lsof -i :3000 -i :5001
# Or kill by name:
pkill -f "run.py"
pkill -f "vite"
```

---

## 3. UPDATING PRODUCT INFORMATION & REALITY SEEDS

### Adding New Product Information
When Volt releases new features or updates documentation:
1. Update `research/product-intelligence/VOLT_PRODUCT_DOSSIER.md` with verified facts.
2. Ensure you never modify files inside the Volt production repository.

### Preparing Updated Reality Seeds
1. Reality seeds live in `research/reality-seeds/`.
2. Follow the 8-seed modular structure:
   - `SEED_1_VOLT_PRODUCT_CONTEXT.md`: Product features, formulas, workflows.
   - `SEED_2_MARKET_CONTEXT.md`: Industry benchmarks and compensation norms.
   - `SEED_3_USER_PSYCHOLOGY.md`: Developer, manager, and founder incentives.
   - `SEED_4_COMPETITIVE_LANDSCAPE.md`: Competitors and alternative workflows.
   - `SEED_5_ADOPTION_AND_RESISTANCE.md`: Drivers and objections.
   - `SEED_6_ORGANIZATIONAL_DYNAMICS.md`: Power dynamics across roles.
   - `SEED_7_CRITICAL_PERSPECTIVES.md`: Edge cases, Goodhart vulnerabilities.
   - `SEED_8_HYPOTHETICAL_PRODUCT_DISCOVERY.md`: Discovery trigger scenarios.

---

## 4. GENERATING NEW PERSONAS
To regenerate or expand the simulated population:
```bash
cd /Users/demo/mirofish/volt-mirofish-research
python3 scripts/generate_personas.py
```
This script validates all required OASIS profile keys (`username`, `bio`, `persona`, `mbti`, `gender`, `age`, `country`) and outputs:
- `research/personas/personas.json` (Full rich attributes)
- `research/personas/reddit_profiles.json` (OASIS engine format)
- `research/personas/PERSONAS_OVERVIEW.md` (Human-readable roster)

---

## 5. RUNNING CONTROLLED SIMULATIONS

Use the automated experiment orchestrator:
```bash
cd /Users/demo/mirofish/volt-mirofish-research/mirofish/backend

# Run Experiment A (Organic Discovery, 10 rounds)
uv run python ../../scripts/run_research_experiment.py --experiment experiment_a --rounds 10

# Run Experiment B (Critical & Skeptical Evaluation, 8 rounds)
uv run python ../../scripts/run_research_experiment.py --experiment experiment_b --rounds 8

# Run Experiment C (Customer & Organizational Adoption, 6 rounds)
uv run python ../../scripts/run_research_experiment.py --experiment experiment_c --rounds 6

# Or execute all three in sequence:
uv run python ../../scripts/run_research_experiment.py --experiment all
```

---

## 6. EXPORTING AND COMPARING EXPERIMENTAL DATA

### Automated Data Exports
Every completed experiment automatically exports its SQLite tables into `research/simulation-results/<experiment_id>/`:
- `posts.json` & `posts.csv`: All discussion threads created.
- `comments.json` & `comments.csv`: All community replies and debates.
- `traces.json` & `traces.csv`: Chronological event log of all agent actions.
- `users.json` & `users.csv`: Active participant profiles.
- `metadata.json`: Runtime configuration and timestamp.

### Comparing Experiments
Run SQLite queries directly on the simulation databases:
```bash
# Compare comment counts across all three experiments
sqlite3 /Users/demo/mirofish/volt-mirofish-research/mirofish/backend/uploads/simulations/exp_a_organic_discovery/reddit_simulation.db "SELECT 'Exp A', count(*) FROM comment;"
sqlite3 /Users/demo/mirofish/volt-mirofish-research/mirofish/backend/uploads/simulations/exp_b_critical_evaluation/reddit_simulation.db "SELECT 'Exp B', count(*) FROM comment;"
sqlite3 /Users/demo/mirofish/volt-mirofish-research/mirofish/backend/uploads/simulations/exp_c_organizational_adoption/reddit_simulation.db "SELECT 'Exp C', count(*) FROM comment;"
```

---

## 7. MONITORING LLM USAGE & API COSTS

- **Model Configured:** Google Gemini Flash (`gemini-3.1-flash-lite` / `gemini-2.5-flash-lite`).
- **Endpoint:** `https://generativelanguage.googleapis.com/v1beta/openai/`
- **Cost Efficiency:**
  - Google Gemini Flash models cost $\sim \$0.075$ per 1,000,000 input tokens.
  - An entire 10-round experiment with 30 agents consumes $\approx 40,000$ tokens, costing less than **\$0.01 per full simulation run**.
- **Rate Limit Caution:** Free-tier keys have rate limits (15 RPM). To prevent bursting, `semaphore` in `backend/scripts/run_reddit_simulation.py` is configured to `5`.


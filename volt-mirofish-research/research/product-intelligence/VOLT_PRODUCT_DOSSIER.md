# VOLT PRODUCT INTELLIGENCE DOSSIER
**Document ID:** VOLT-DOSSIER-2026-Q4  
**Date:** November 18, 2026  
**Status:** Validated Technical & Market Analysis  
**Repository Source:** `https://github.com/hi-ashwinsharma/volt` (Checked-out branch: `feat/l30-goal-templates`)  
**Live Deployment:** `https://volt.qmatus.com/` (HTTP 200 OK, Vercel Edge / Cloud Run)  

---

## A. PRODUCT OVERVIEW

Volt is an output-based contribution tracking, impact verification, and mathematical weightage platform engineered for high-agency knowledge work teams. It is positioned as an antidote to traditional clock-based timesheets, replacing passive desk hours with a Git-inspired staging and commit workflow:

$$\text{Micro-tasks (Logs)} \xrightarrow{\texttt{volt add}} \text{Local / Staging Buffer} \xrightarrow{\texttt{volt commit}} \text{Verified Proof \& AI Evaluation}$$

### Core Architecture & Delivery Surfaces
1. **Developer Tooling First:** Designed around a `<3\text{s}` human thought and `<50\text{ms}` terminal interaction budget.
2. **Clients:**
   - **CLI Binary (`volt`):** Written in TypeScript/Bun, utilizing a local write-ahead SQLite queue (`~/.volt/queue.sqlite`) for sub-5ms local writes and offline resilience.
   - **Model Context Protocol (`volt-mcp`):** Native MCP server exposing staging, committing, and status tools directly to AI coding environments (Antigravity, Claude Desktop, Cursor).
   - **Desktop Quick-Entry Overlay:** Tauri v2 application providing a global keyboard shortcut (`Cmd+Shift+L` / `Ctrl+Shift+L`).
   - **Telegram Bot:** Voice note transcription via multimodal STT and text commands for mobile logging.
   - **Web Command Center:** Next.js 16 (React 19) Linear-dark command interface with keyboard shortcuts (`Cmd+K`).
3. **Backend & Data Infrastructure:**
   - **Fastify 5 REST API:** Multi-tenant service running on Google Cloud Run, organizing firm workspaces under `/v1/firms/:slug`.
   - **PostgreSQL on Neon:** Drizzle ORM with immutable audit ledgers (`score_audits`) guarded by PostgreSQL triggers disallowing `UPDATE` and `DELETE`.
   - **Upstash Redis:** Staging buffer, deduplication, and cache layer.
   - **Google Cloud Tasks & Cloud Scheduler:** Asynchronous ingestion workers, daily sweepers (19:30 IST), and AI evaluations.
   - **AI Judge Pipeline:** Multimodal LLM judge (`gemini-2.5-flash` / Gemini Flash on Vertex AI / developer keys) evaluating complexity and alignment against written domain rubrics.
   - **GitHub App:** Cryptographic verification of pull requests, commits, and CI checks.

---

## B. VERIFIED FUNCTIONALITY

Based on direct source code inspection of the monorepo (`packages/math`, `packages/db`, `packages/policy`, `apps/api`, `apps/cli`, `apps/web`):

1. **Two-Stage Logging Pipeline:**
   - `volt add "<log message>"` stores micro-tasks in a local SQLite database or Redis staging queue.
   - `volt commit` bundles staged logs into a single commit with metadata: domain, complexity, summary, PR link, and co-authors.
2. **Mathematical Weightage Formula ($W_c$):**
   - Implemented in `@volt/math/weightage.ts`:
     $$W_{\text{initial}} = C^{1.4} \times I \times E$$
     $$W_c = \text{round}\left( W_{\text{initial}} \times V \times D, \, 2 \right)$$
   - **Cognitive Complexity ($C \in \{1, 2, 3, 5, 8, 13\}$):** Non-linear power table:
     - $C=1 \rightarrow 1.00$
     - $C=2 \rightarrow 2.64$
     - $C=3 \rightarrow 4.66$
     - $C=5 \rightarrow 9.52$
     - $C=8 \rightarrow 18.38$
     - $C=13 \rightarrow 36.26$
   - **Business Impact ($I \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$):** Organizational leverage multiplier.
   - **Evidence Multiplier ($E \in \{0.5, 1.0, 1.2\}$):** Unverified (0.5), verified PR/artifact (1.0), exceptional benchmarks/docs (1.2).
   - **Consensus Modifier ($V \in [0.70, 1.30]$):** Peer review modifier.
   - **Decay Factor ($D \in [0.50, 1.00]$):** Rewards prompt logging.
3. **Co-Author Handshake & Collaboration Split:**
   - $N \in [1, 3]$ contributors: Full credit replication to incentivize co-authoring without penalty.
   - $N \ge 4$: Split formula $\text{Share} = \frac{3}{N} \times W_c$ to prevent credit dilution and social loafing.
4. **Security & Access Control:**
   - Dual-Authentication: Firebase ID tokens for browser sessions; SHA-256 hashed API keys (`volt_sk_*`) for CLI/MCP/bot.
   - Policy-Based Access Control (PBAC): Scoped permission evaluations (`commit:create`, `cycle:manage`, `commit:review_peer`) with strict conflict-of-interest checks (no self-review).
5. **Latest Strategic Evolution (Docs 14-16 & Branch `feat/l30-goal-templates`):**
   - Shift from automatic payroll/bonus payout engine toward manager-facing goal and proof tracking for teams of 8-20.
   - Dual scoring modes: Time-based (default) and VoltAI (optional).
   - Commits categorized into Auto-verified (connected tools like GitHub) and Self-reported (manual notes/files).
   - Plain-language custom manager rubrics instead of a rigid black-box rubric.

---

## C. TARGET CUSTOMER SEGMENTS

1. **High-Agency Software Engineering Teams (8–30 engineers):**
   - Startups, boutique consultancies, and remote development houses where standard timesheets (Harvest, Clockify, Toggl) create friction and resentment.
2. **Cross-Functional Product & Research Labs:**
   - Teams blending AI research, product design, and deep technical infrastructure where hours logged do not correlate with business breakthrough.
3. **Agencies & Freelancer Collectives:**
   - Knowledge collectives distributing pooled project revenue based on verified contribution complexity and deliverables rather than billable hours.
4. **Technical Founders & Engineering Managers:**
   - Leaders seeking objective visibility into team progress, bottleneck unblocking, and authentic individual leverage without micromanagement.

---

## D. USER PROBLEMS ADDRESSED

1. **The "Ass-in-Chair" Distortion:** Hourly tracking incentivizes slow execution, junior inefficiency, and prolonged desk time while penalizing senior engineers who solve deep architectural problems in 30 minutes.
2. **Friday Afternoon Timesheet Dread:** Retrospective, end-of-week timesheet filling results in fabricated, low-fidelity time logs that provide zero real insight into productivity.
3. **The Invisible R&D Problem:** In research and exploratory engineering, disproving a dead-end hypothesis saves millions in capital but generates zero billable lines of code. Volt’s "Epistemic Parity" treats rigorous refutation equally to feature shipment.
4. **Context Switching Overhead:** Traditional project management tools (Jira, Asana, Linear) require leaving the terminal or IDE; Volt integrates into `git`, CLI, Tauri overlay, and MCP.

---

## E. VALUE PROPOSITION

- **For Individual Contributors:** "Get recognized and rewarded for how hard and impactful your work is, not how many hours you sat at a desk. Log in 1 second from your terminal or AI IDE."
- **For Engineering Managers & Founders:** "Eliminate timesheet chasing. Gain tamper-proof visibility into goals, verifiable proofs, and AI-assisted complexity scoring calibrated to your own written rules."
- **For Finance & Leadership:** "Fair, explainable bonus allocation driven by immutable mathematical ledger entries rather than subjective end-of-quarter politics."

---

## F. COMPETITIVE ALTERNATIVES

| Alternative Category | Representative Tools | Key Limitations Volt Exploits |
| :--- | :--- | :--- |
| **Traditional Timesheets** | Harvest, Toggl, Clockify, Replicon | Pure hour counting; zero complexity awareness; high friction logging. |
| **Activity Surveillance** | Hubstaff, Time Doctor, Teramind | Invasive keylogging and screenshot monitoring; destroys psychological safety and high-agency culture. |
| **Engineering Metrics / DORA** | Jellyfish, LinearB, DX, Waydev | Aggregate PR cycle time / commit velocity; easily gamed by PR splitting; disconnected from financial compensation or bonus pools. |
| **Project Tracking** | Linear, Jira, GitHub Projects | Focuses on status transitions (Todo $\rightarrow$ Done); does not compute individual cognitive complexity, business leverage, or compensation shares. |

---

## G. POTENTIAL ADOPTION BARRIERS

1. **Employee Anxiety Over "AI Judging Work":** Fear that an algorithmic judge (`gemini-2.5-flash`) will misunderstand nuanced engineering trade-offs or penalize non-code contributions.
2. **Gaming the Formula ($C^{1.4} \times I \times E$):** Risk that engineers optimize for high-complexity claims ($C=8$ or $13$), claim inflated impact multipliers, or co-author collude to duplicate points.
3. **Manager Configuration Burden:** Defining custom rubrics and plain-language goal templates requires deliberate operational effort from managers who are already time-constrained.
4. **Organizational Resistance from Traditional HR:** Established HR and payroll systems are legally and contractually tethered to hourly/salaried models; moving to variable weightage payout requires executive mandate.
5. **Tool Fatigue:** Introducing another tool alongside Slack, Jira/Linear, and GitHub can cause developer resistance unless CLI and MCP integration feels genuinely frictionless.

---

## H. TRUST AND PRIVACY CONSIDERATIONS

1. **Data Scope & Tenancy:** Strict firm-level tenant isolation (`/v1/firms/:slug`) and PBAC prevent cross-firm leakage.
2. **Immutable Auditability:** Triggers prevent administrative tampering with historical score audits.
3. **AI Transparency:** Full reasoning text must be captured and inspectable by managers to prevent "black box" resentment.
4. **Artifact Privacy:** GitHub integrations require repo metadata access; organizations may hesitate to grant cloud third-party services access to private repositories.

---

## I. UNVERIFIED ASSUMPTIONS

1. *Assumption:* High-performing engineers will gladly log in the terminal if it takes $<3$ seconds. *(Needs verification: Do engineers actually remember `volt add` during deep work?)*
2. *Assumption:* Teams want output-based compensation rather than the predictability of fixed salaries. *(Needs verification: Risk tolerance of mid-level and junior employees.)*
3. *Assumption:* AI rubrics can objectively grade complex tasks across engineering, growth, and operations with minimal human escalation. *(Needs verification: Rate of false positives and contested scores.)*
4. *Assumption:* Non-engineering roles (Sales, Ops, Finance) will embrace a tool with Git-like mental models (`add`, `commit`, `staging`).

---

## J. RESEARCH QUESTIONS FOR SIMULATION

1. **RQ1 (Discovery & First Impressions):** How do diverse professional personas react to the initial concept of "Git for your work" and "AI-judged impact scoring"? Where does skepticism concentrate?
2. **RQ2 (Objections & Failure Modes):** What are the sharpest criticisms raised by skeptical engineers, conservative managers, and security-minded professionals? What triggers tool rejection?
3. **RQ3 (Organizational Viability):** In a team setting (founder vs. senior engineer vs. junior engineer vs. operations), how do internal power dynamics and incentives shape willingness to adopt Volt?


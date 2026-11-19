# REALITY SEED 1: VOLT PRODUCT CONTEXT
**Domain:** Product Architecture, Features & Workflows  
**Integrity Level:** Verified against production codebase and live deployment (`volt.qmatus.com`)  

---

### 1. What is Volt?
Volt is an output-based contribution tracking and mathematical weightage platform engineered for knowledge work teams. It replaces traditional timesheet hour tracking with a Git-inspired staging and commit workflow:
- **`volt add "<task>"`**: Micro-tasks are captured instantaneously into an embedded SQLite write-ahead queue (`~/.volt/queue.sqlite`) or cloud staging buffer in under 50ms without interrupting focus.
- **`volt commit`**: Bundles staged micro-logs into an immutable commit, attaching metadata: cognitive complexity ($C$), business impact ($I$), artifact proof ($E$), summary, and co-authors.

### 2. The Weightage Mathematical Engine ($W_c$)
Volt calculates commit value using a deterministic mathematical formula:
$$W_c = \text{round}\left( C^{1.4} \times I \times E \times V \times D, \, 2 \right)$$
- **Cognitive Complexity ($C \in \{1, 2, 3, 5, 8, 13\}$)**: Employs a non-linear power scale ($C^{1.4}$) so that breakthrough engineering ($C=13 \rightarrow 36.26\times$) compounds exponentially over routine chores ($C=1 \rightarrow 1.0\times$).
- **Business Impact Multiplier ($I \in \{0.5, 1.0, 1.5, 2.0, 3.0\}$)**: Measures leverage on critical path goals, customer delivery, or cost efficiency.
- **Evidence Multiplier ($E \in \{0.5, 1.0, 1.2\}$)**: Differentiates unverified self-reported logs ($0.5\times$), verified GitHub PRs/commits via GitHub App ($1.0\times$), and exceptional reproducible benchmarks/documentation ($1.2\times$).
- **Consensus Modifier ($V \in [0.70, 1.30]$)**: Peer calibration factor.
- **Timeliness Decay ($D \in [0.50, 1.00]$)**: Penalizes stale batch logging and rewards real-time capture.

### 3. Collaboration & Payout Rules
- **Co-Author Distribution**: Full credit duplication for 1 to 3 collaborators ($100\%$ each); distributed as $\text{Share} = \frac{3}{N} \times W_c$ for $N \ge 4$ contributors.
- **Bonus Pool Distribution**: Transparent team bonus fund allocation where each contributor's payout equals $\text{BonusPool} \times \left( \frac{\sum W_{c,u}}{\sum_{\text{all}} W_c} \right)$.
- **Dual Scoring Flexibility**: Project managers can operate in standard Time-Based mode or activate VoltAI scoring, with full plain-language rubric customization and human manager override.

### 4. Client Surfaces
- Fast CLI binary (`volt`) with offline SQLite queue.
- Model Context Protocol (`volt-mcp`) daemon for AI IDEs (Antigravity, Cursor, Claude Desktop).
- Desktop Quick-Entry Overlay (Tauri v2, global shortcut `Cmd+Shift+L`).
- Telegram bot with voice STT audio transcription.
- Modern Web Command Center (Next.js 16, Linear-dark aesthetic, `Cmd+K` palette).


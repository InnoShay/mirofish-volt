# STRATEGIC PRODUCT RECOMMENDATIONS FOR VOLT
**Document ID:** VOLT-REP-09-RECOMMENDATIONS  
**Date:** November 18, 2026  
**Actionability Rating:** High / Immediate Roadmap Relevance  
**Author:** AI Product Intelligence & DevOps Team  

---

## 1. STRATEGIC POSITIONING & MARKETING PIVOT

### Recommendation 1: Never Brand as an "AI Payroll Judge"
- **Finding Source:** Experiment B (Comments 1-3, 8) & Experiment C (Comments 7, 18, 21).
- **Rationale:** The term "AI Judge" or "AI-computed compensation" triggers immediate resistance, evoking dystopian imagery of "digital Taylorism" and algorithmic firing. It mobilizes labor advocates, alarms HR/legal decision-makers, and intimidates junior developers.
- **Actionable Execution:**
  - Reframe the headline at `volt.qmatus.com` from *"Get paid for what you ship, not the hours you sit"* to:  
    **"The Zero-Friction Delivery Engine for High-Agency Teams. Turn shipped work into verified proof, clear progress, and fair recognition."**
  - Position VoltAI strictly as **"Studio Assist"**—an intelligent assistant that drafts goals, summarizes weekly wins, and suggests complexity estimates that managers always confirm.

### Recommendation 2: Lead with the Developer Experience Invariant (<3s Rule)
- **Finding Source:** Experiment A (Comments 1, 8, 11) & Experiment C (Comment 11).
- **Rationale:** The sub-50ms CLI queue and MCP IDE integration are universally loved differentiators that no legacy timesheet tool possesses.
- **Actionable Execution:** Make the local CLI installation (`curl -fsSL https://volt.build/install.sh | sh`) the hero CTA on the website. Let developers use Volt as their personal free scratchpad logbook before their company ever adopts it.

---

## 2. CORE ENGINE & RUBRIC ENHANCEMENTS

### Recommendation 3: Explicit "Refactoring & Stewardship" Rubric Templates
- **Finding Source:** Experiment A (Comment 17), Experiment B (Comment 9), Experiment C (Comment 9, 13).
- **Rationale:** Developers fear that deleting code, refactoring architectures, or mentoring will be down-weighted against flashy feature PRs.
- **Actionable Execution:**
  - Ship standard, pre-calibrated rubric starter templates in `@volt/math`:
    - *Template A (Infrastructure & Technical Debt):* Grants automatic $C=5$ or $C=8$ weightage for PRs that delete $\ge 500$ lines of code, improve test coverage by $\ge 5\%$, or fix high-concurrency race conditions.
    - *Template B (Mentorship & Pair Programming):* Leverages the existing Co-Author handshake to award full credit for senior-junior pairing sessions.

### Recommendation 4: Anti-Gaming Verification via Code Metrics (Not Just Prompt Text)
- **Finding Source:** Experiment B (Post 2; Comments 5, 8).
- **Rationale:** Prevent prompt-engineered commit summaries from inflating the complexity multiplier.
- **Actionable Execution:**
  - Extend the GitHub App integration (`docs/06-github-app-and-artifacts.md`) to extract objective AST complexity metrics (cyclomatic complexity change, AST depth, diff size) alongside the commit summary.
  - If a commit claims $C=8$ or $13$ but the AST diff shows only comment changes or minor copy edits, flag it automatically for mandatory human manager review.

---

## 3. INCLUSIVITY & NON-DEVELOPER ERGONOMICS

### Recommendation 5: First-Class Artifact Support for Non-Technical Deliverables
- **Finding Source:** Experiment A (Comment 13) & Experiment C (Comments 12, 16, 20).
- **Rationale:** Cross-functional teams cannot adopt Volt if designers, marketers, and PMs are treated as second-class citizens.
- **Actionable Execution:**
  - In `packages/types`, expand verified artifact sources beyond `github_pr` to include `figma_file`, `google_doc`, and `custom_url`.
  - Equip the Tauri desktop overlay (`Cmd+Shift+L`) and Telegram bot with direct attachment upload capabilities.

---

## 4. ENTERPRISE & LEGAL READINESS

### Recommendation 6: Structuring Payouts as Discretionary Bonus Pools Only
- **Finding Source:** Experiment C (Comments 16, 17, 24).
- **Rationale:** Compliance with labor law and preventing wage-and-hour lawsuits.
- **Actionable Execution:** Maintain base salaries as fixed and separate. In all product documentation, explicitly state that Volt point allocations apply solely to discretionary performance bonus funds, never to base salary calculations.


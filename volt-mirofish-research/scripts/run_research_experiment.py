"""
Volt Research Experiment Orchestrator
Executes controlled multi-agent simulations using MiroFish's OASIS engine.
Supports Experiment A, B, and C.
Extracts results into SQLite, JSON, and CSV for deep product intelligence analysis.
"""

import argparse
import asyncio
import csv
import json
import os
import shutil
import sqlite3
import sys
import time

# Paths
ROOT_DIR = "/Users/demo/mirofish/volt-mirofish-research"
MIROFISH_DIR = os.path.join(ROOT_DIR, "mirofish")
BACKEND_DIR = os.path.join(MIROFISH_DIR, "backend")
PERSONAS_PATH = os.path.join(ROOT_DIR, "research/personas/reddit_profiles.json")
EXPERIMENTS_DIR = os.path.join(ROOT_DIR, "research/experiments")
SIM_RESULTS_DIR = os.path.join(ROOT_DIR, "research/simulation-results")

# Ensure backend path is in sys.path
sys.path.insert(0, BACKEND_DIR)
sys.path.insert(0, os.path.join(BACKEND_DIR, "scripts"))

# Import OASIS simulation runner
from scripts.run_reddit_simulation import RedditSimulationRunner

EXPERIMENT_SPECS = {
    "experiment_a": {
        "id": "exp_a_organic_discovery",
        "name": "Experiment A: Organic Product Discovery",
        "research_question": "How might people naturally perceive Volt when they encounter it for the first time?",
        "total_hours": 6,          # 12 rounds (30 min per round)
        "minutes_per_round": 30,
        "agents_per_hour_min": 6,
        "agents_per_hour_max": 10,
        "initial_posts": [
            {
                "poster_agent_id": 25,  # Simon Kestler (Tech Creator)
                "content": (
                    "Just came across Volt (volt.qmatus.com) – they're pitching 'Git for your work' "
                    "and replacing hourly timesheets with non-linear mathematical weightage (C^1.4 * I * E). "
                    "<5ms CLI with local SQLite queue, MCP server, and team bonus pools. "
                    "Is hourly tracking finally dead, or is this too radical for normal teams?"
                )
            },
            {
                "poster_agent_id": 0,   # Alex Rivera (Early Dev)
                "content": (
                    "Tested the volt CLI binary locally. Sub-50ms capture from the terminal is remarkably slick. "
                    "No Electron bloat. But how does an AI judge or rubric handle refactoring vs feature shipping? "
                    "Anyone else trying this out on real repos?"
                )
            }
        ]
    },
    "experiment_b": {
        "id": "exp_b_critical_evaluation",
        "name": "Experiment B: Skeptical and Critical Evaluation",
        "research_question": "What are the strongest reasons a potential customer might refuse to use Volt?",
        "total_hours": 6,          # 12 rounds
        "minutes_per_round": 30,
        "agents_per_hour_min": 6,
        "agents_per_hour_max": 10,
        "initial_posts": [
            {
                "poster_agent_id": 4,   # Martin Lindqvist (Principal SRE)
                "content": (
                    "Critical evaluation of Volt (volt.qmatus.com): Any compensation system tied to mathematical "
                    "scoring (C^1.4 * I * E) will fall victim to Goodhart's Law within 60 days. Engineers will "
                    "prompt-engineer their commit summaries into 'architectural paradigms' to game the AI judge. "
                    "Why shouldn't engineering teams just stick to standard peer reviews and qualitative 1-on-1s?"
                )
            },
            {
                "poster_agent_id": 20,  # Nadia Petrov (AI Safety Researcher)
                "content": (
                    "Using LLMs (Gemini Flash) to grade human cognitive complexity is deeply fraught. "
                    "LLM evaluators are notoriously sensitive to length bias, vocabulary sophistication, and formatting. "
                    "What stops someone from using an LLM to generate the highest-scoring commit descriptions "
                    "while junior engineers doing unglamorous bug fixing get penalized?"
                )
            },
            {
                "poster_agent_id": 19,  # Gordon Vance (Privacy Advocate)
                "content": (
                    "Volt claims to be zero-friction, but having an automated system log, score, and ledger "
                    "every micro-task into an immutable PostgreSQL database looks like digital Taylorism disguised "
                    "as developer tooling. How is this not surveillance creep?"
                )
            }
        ]
    },
    "experiment_c": {
        "id": "exp_c_organizational_adoption",
        "name": "Experiment C: Customer and Organizational Adoption",
        "research_question": "What would need to be true for individuals or organizations to adopt Volt?",
        "total_hours": 6,          # 12 rounds
        "minutes_per_round": 30,
        "agents_per_hour_min": 6,
        "agents_per_hour_max": 10,
        "initial_posts": [
            {
                "poster_agent_id": 6,   # Marcus Vance (Startup Founder)
                "content": (
                    "We are evaluating Volt across our 14-person startup to replace timesheets and distribute "
                    "our quarterly team bonus pool based on verified output. I need honest feedback from our "
                    "engineering leads, junior devs, and ops: what would need to be true for you to trust this with your compensation?"
                )
            },
            {
                "poster_agent_id": 8,   # Tariq Mansoor (Head of People/Ops)
                "content": (
                    "From an operations and HR perspective, how do we handle the shift from fixed predictable pay "
                    "to variable weightage points? What about legal employment contracts, junior career growth, and "
                    "non-technical teammates who don't touch Git or CLI? What are the actual implementation barriers?"
                )
            },
            {
                "poster_agent_id": 9,   # Wei Chen (VP Engineering)
                "content": (
                    "Examining the latest Volt architecture (Docs 14-16): they introduced dual scoring modes "
                    "(time-based default vs VoltAI optional) and plain-language custom manager rubrics. "
                    "Does this shift make it viable for teams of 8-20, or is the configuration burden still too high?"
                )
            }
        ]
    }
}

def export_simulation_data(db_path: str, output_dir: str):
    """Exports SQLite simulation tables to structured JSON and CSV files."""
    os.makedirs(output_dir, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    tables = ["post", "comment", "like", "dislike", "trace", "user"]
    export_summary = {}

    for table in tables:
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = [dict(row) for row in cursor.fetchall()]
            export_summary[table] = len(rows)

            # Export JSON
            json_file = os.path.join(output_dir, f"{table}s.json")
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(rows, f, indent=2, ensure_ascii=False)

            # Export CSV
            if rows:
                csv_file = os.path.join(output_dir, f"{table}s.csv")
                with open(csv_file, "w", newline="", encoding="utf-8") as f:
                    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                    writer.writeheader()
                    writer.writerows(rows)
        except Exception as e:
            export_summary[table] = f"Error: {str(e)}"

    conn.close()
    return export_summary

async def run_experiment(exp_key: str, max_rounds: int = 12):
    spec = EXPERIMENT_SPECS[exp_key]
    exp_dir = os.path.join(EXPERIMENTS_DIR, spec["id"])
    sim_dir = os.path.join(BACKEND_DIR, "uploads/simulations", spec["id"])
    os.makedirs(exp_dir, exist_ok=True)
    os.makedirs(sim_dir, exist_ok=True)

    # 1. Copy profiles
    shutil.copy(PERSONAS_PATH, os.path.join(exp_dir, "reddit_profiles.json"))
    shutil.copy(PERSONAS_PATH, os.path.join(sim_dir, "reddit_profiles.json"))

    # 2. Build simulation config
    agent_configs = []
    for i in range(30):
        agent_configs.append({
            "agent_id": i,
            "active_hours": list(range(24)),
            "activity_level": 0.8
        })

    config_data = {
        "simulation_id": spec["id"],
        "simulation_name": spec["name"],
        "research_question": spec["research_question"],
        "llm_model": "gemini-3.1-flash-lite",
        "time_config": {
            "total_simulation_hours": spec["total_hours"],
            "minutes_per_round": spec["minutes_per_round"],
            "agents_per_hour_min": spec["agents_per_hour_min"],
            "agents_per_hour_max": spec["agents_per_hour_max"],
            "peak_hours": list(range(24)),
            "off_peak_hours": []
        },
        "agent_configs": agent_configs,
        "event_config": {
            "initial_posts": spec["initial_posts"]
        }
    }

    config_path = os.path.join(sim_dir, "simulation_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=2)
    shutil.copy(config_path, os.path.join(exp_dir, "simulation_config.json"))

    print("\n" + "=" * 60)
    print(f"STARTING {spec['name']}")
    print(f"Research Question: {spec['research_question']}")
    print(f"Config path: {config_path}")
    print(f"Max rounds: {max_rounds}")
    print("=" * 60 + "\n")

    start_time = time.time()
    runner = RedditSimulationRunner(config_path=config_path, wait_for_commands=False)
    await runner.run(max_rounds=max_rounds)
    elapsed = time.time() - start_time

    print(f"\nSimulation finished in {elapsed:.1f}s")

    # 3. Export data
    db_path = os.path.join(sim_dir, "reddit_simulation.db")
    results_output = os.path.join(SIM_RESULTS_DIR, spec["id"])
    summary = export_simulation_data(db_path, results_output)
    print("Export Summary:", summary)

    # Copy DB to experiment dir
    shutil.copy(db_path, os.path.join(exp_dir, "reddit_simulation.db"))

    # Save execution metadata
    meta = {
        "experiment_id": spec["id"],
        "name": spec["name"],
        "research_question": spec["research_question"],
        "llm_model": "gemini-3.1-flash-lite",
        "rounds_executed": max_rounds,
        "elapsed_seconds": elapsed,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "export_summary": summary
    }
    with open(os.path.join(results_output, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    return meta

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", choices=["experiment_a", "experiment_b", "experiment_c", "all"], default="experiment_a")
    parser.add_argument("--rounds", type=int, default=10)
    args = parser.parse_args()

    if args.experiment == "all":
        for key in ["experiment_a", "experiment_b", "experiment_c"]:
            asyncio.run(run_experiment(key, max_rounds=args.rounds))
    else:
        asyncio.run(run_experiment(args.experiment, max_rounds=args.rounds))

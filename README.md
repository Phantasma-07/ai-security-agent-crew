# AI Security Agent Crew 🛡

**By KyberPhantasma — Kybernos Labs**
**Status: Work in Progress**

---

## Overview

A multi-agent AI system designed for Web2 and Web3 offensive security research. Built around an MCP (Model Context Protocol) orchestration architecture where all agent communication is routed through a central hub — **HERMES**.

This project demonstrates object-oriented Python design, modular agent architecture, and applied cybersecurity concepts.

---

## Agents

| Agent | Role | Tag |
|---|---|---|
| HERMES | Orchestrator & Memory Hub | CORE |
| XALGORIX | Recon Specialist | RECON |
| PENTEST SUITE | Web2 & Web3 Hunter | OFFENSIVE |
| SHANNON LITE | Exploit Validator | VALIDATION |
| OPENHACK | Source Code Triage | ANALYSIS |
| CAI | Raw Hacking Engine | ENGINE |

---

## Architecture

```
XALGORIX ──┐
PENTEST ───┤
SHANNON ───┼──► HERMES (MCP Hub) ──► Output / Report
OPENHACK ──┤
CAI ───────┘
```

No agent communicates directly with another.
All tasks route through HERMES.

---

## How to Run

**Requirements:** Python 3.6+ (no external libraries needed)

```bash
python main.py
```

**Example commands in the terminal:**
```
HERMES › status
HERMES › dispatch recon target.com
HERMES › dispatch fuzz api endpoint
HERMES › broadcast full security sweep
HERMES › profile XALGORIX
HERMES › memory
HERMES › help
```

---

## Project Structure

```
ai-security-agent-crew/
│
├── main.py        # Entry point — Hermes interactive terminal
├── hermes.py      # Orchestrator class — routing, memory, dispatch
├── agents.py      # All agent classes (inheriting from base Agent)
└── README.md      # This file
```

---

## Concepts Demonstrated

- Object-Oriented Programming (classes, inheritance, method overriding)
- Multi-agent system design
- Task routing via keyword mapping
- Persistent in-session memory logging
- Clean CLI interface design
- Modular, readable Python structure

---

## Roadmap

- [ ] Connect agents to real LLM backends (Ollama / Nemotron / Kimi K2)
- [ ] Add real recon tool integration (subfinder, httpx, nuclei)
- [ ] Implement actual Slither static analysis in OPENHACK
- [ ] Build web interface for HERMES dashboard
- [ ] Persistent memory across sessions (JSON / SQLite)

---

*Kybernos Labs — "We train the people who guard the world."*

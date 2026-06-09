# hermes.py
# HERMES — Central Orchestrator and Memory Hub.
# All agent communication flows through Hermes via the
# Model Context Protocol (MCP) architecture.
# Author: KyberPhantasma — Kybernos Labs

from agents import Xalgorix, PentestSuite, ShannonLite, OpenHack, CAI


class Hermes:
    """
    HERMES is the central intelligence of the AI Security Crew.

    Responsibilities:
    - Register and manage all agents
    - Route tasks to appropriate agents based on task type
    - Maintain a persistent memory log of all operations
    - Synthesize agent outputs into a unified report

    All communication between agents passes through Hermes.
    No agent communicates directly with another.
    This is the MCP (Model Context Protocol) architecture.
    """

    # Task keywords that map to specific agents
    ROUTING_MAP = {
        "recon": "XALGORIX",
        "osint": "XALGORIX",
        "subdomain": "XALGORIX",
        "fingerprint": "XALGORIX",
        "hunt": "PENTEST SUITE",
        "payload": "PENTEST SUITE",
        "exploit": "PENTEST SUITE",
        "attack": "PENTEST SUITE",
        "defi": "PENTEST SUITE",
        "smart contract": "PENTEST SUITE",
        "validate": "SHANNON LITE",
        "verify": "SHANNON LITE",
        "false positive": "SHANNON LITE",
        "severity": "SHANNON LITE",
        "signal": "SHANNON LITE",
        "code": "OPENHACK",
        "source": "OPENHACK",
        "static": "OPENHACK",
        "solidity": "OPENHACK",
        "dependency": "OPENHACK",
        "fuzz": "CAI",
        "brute": "CAI",
        "probe": "CAI",
        "stress": "CAI",
        "engine": "CAI",
    }

    def __init__(self):
        self.name = "HERMES"
        self.role = "Orchestrator & Memory Hub"
        self.status = "active"
        self.memory = []       # Persistent log of all operations
        self.crew = {}         # Registered agents
        self._register_crew()

    def _register_crew(self):
        """Instantiate and register all agents into the crew."""
        agents = [
            Xalgorix(),
            PentestSuite(),
            ShannonLite(),
            OpenHack(),
            CAI(),
        ]
        for agent in agents:
            self.crew[agent.name] = agent

        self._log("SYSTEM", "All agents registered. Crew online.")

    def _log(self, source, message):
        """Write an entry to Hermes memory."""
        entry = f"[{source}] {message}"
        self.memory.append(entry)

    def _route(self, task):
        """
        Determine which agent should handle a given task.
        Scans the task string for known keywords.
        Falls back to PENTEST SUITE as the default offensive agent.
        """
        task_lower = task.lower()
        for keyword, agent_name in self.ROUTING_MAP.items():
            if keyword in task_lower:
                return agent_name
        return "PENTEST SUITE"  # default

    def dispatch(self, task):
        """
        Receive a task, route it to the correct agent,
        log the interaction, and return the agent's response.
        """
        self._log("HERMES", f"Task received: '{task}'")
        agent_name = self._route(task)
        agent = self.crew.get(agent_name)

        if not agent:
            return f"[HERMES] Error: Agent '{agent_name}' not found in crew."

        self._log("HERMES", f"Routing to {agent_name}...")
        response = agent.receive_task(task)
        self._log(agent_name, "Task complete.")

        return response

    def dispatch_all(self, task):
        """
        Broadcast a task to every agent in the crew simultaneously.
        Returns a combined report from all agents.
        """
        self._log("HERMES", f"Broadcasting task to full crew: '{task}'")
        report_lines = [
            "╔══════════════════════════════════════════════════╗",
            "  HERMES — FULL CREW BROADCAST REPORT",
            "╚══════════════════════════════════════════════════╝",
            "",
        ]
        for agent in self.crew.values():
            report_lines.append(agent.receive_task(task))
            report_lines.append("")

        self._log("HERMES", "Full crew broadcast complete.")
        return "\n".join(report_lines)

    def crew_status(self):
        """Display the current status of all registered agents."""
        border = "═" * 50
        lines = [
            border,
            "  HERMES — CREW STATUS REPORT",
            border,
            f"  Orchestrator : {self.name}",
            f"  Status       : {self.status.upper()}",
            f"  Agents Online: {len(self.crew)}",
            f"  Memory Entries: {len(self.memory)}",
            border,
            "",
        ]
        for agent in self.crew.values():
            lines.append(f"  [{agent.tag:<12}] {agent.name:<16} — {agent.status.upper()}")

        lines.append(border)
        return "\n".join(lines)

    def show_memory(self):
        """Print the full operation memory log."""
        border = "─" * 50
        lines = [border, "  HERMES — MEMORY LOG", border]
        if not self.memory:
            lines.append("  No entries yet.")
        else:
            for i, entry in enumerate(self.memory, 1):
                lines.append(f"  {str(i).zfill(3)}  {entry}")
        lines.append(border)
        return "\n".join(lines)

    def agent_profile(self, name):
        """Return the full profile of a named agent."""
        agent = self.crew.get(name.upper())
        if not agent:
            return f"[HERMES] Agent '{name}' not found."
        return agent.profile()

    def __repr__(self):
        return f"<Hermes | Agents: {len(self.crew)} | Memory: {len(self.memory)} entries>"

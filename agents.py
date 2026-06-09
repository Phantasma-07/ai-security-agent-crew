# agents.py
# Defines all agent classes in the AI Security Crew.
# Each agent inherits from the base Agent class.
# Author: KyberPhantasma — Kybernos Labs


class Agent:
    """
    Base class for all agents in the AI Security Crew.
    Every agent has a name, role, set of capabilities,
    and the ability to receive and process tasks.
    """

    def __init__(self, name, role, tag, description, capabilities):
        self.name = name
        self.role = role
        self.tag = tag
        self.description = description
        self.capabilities = capabilities
        self.status = "standby"
        self.task_log = []

    def activate(self):
        """Set agent status to active."""
        self.status = "active"
        return f"[{self.name}] Activated."

    def deactivate(self):
        """Set agent status to standby."""
        self.status = "standby"
        return f"[{self.name}] Returning to standby."

    def receive_task(self, task):
        """
        Receive a task string, log it, and process it.
        Returns the agent's response.
        """
        self.status = "active"
        self.task_log.append(task)
        response = self.process(task)
        self.status = "standby"
        return response

    def process(self, task):
        """
        Default task processor. Subclasses override this
        to implement agent-specific behaviour.
        """
        return (
            f"[{self.name} — {self.role}]\n"
            f"Task received: '{task}'\n"
            f"Capabilities available: {', '.join(self.capabilities)}\n"
            f"Processing with {self.tag} logic...\n"
        )

    def profile(self):
        """Return a formatted summary of the agent's identity."""
        border = "─" * 48
        lines = [
            border,
            f"  AGENT    : {self.name}",
            f"  ROLE     : {self.role}",
            f"  TAG      : {self.tag}",
            f"  STATUS   : {self.status.upper()}",
            f"  INFO     : {self.description}",
            f"  SKILLS   : {', '.join(self.capabilities)}",
            border,
        ]
        return "\n".join(lines)

    def __repr__(self):
        return f"<Agent: {self.name} | {self.role} | {self.status}>"


# ── Individual Agent Classes ──────────────────────────────────────


class Xalgorix(Agent):
    """
    Recon Specialist.
    Builds comprehensive target intelligence through OSINT,
    subdomain enumeration, and asset fingerprinting.
    """

    def __init__(self):
        super().__init__(
            name="XALGORIX",
            role="Recon Specialist",
            tag="RECON",
            description=(
                "Advanced reconnaissance agent. Builds target maps through "
                "OSINT, subdomain enumeration, certificate transparency "
                "analysis, and asset fingerprinting. Feeds the crew with "
                "structured intelligence before engagement begins."
            ),
            capabilities=[
                "OSINT Collection",
                "Subdomain Enumeration",
                "Asset Fingerprinting",
                "Certificate Transparency",
                "Shodan Integration",
                "Recon Automation",
            ],
        )

    def process(self, task):
        return (
            f"[XALGORIX — RECON]\n"
            f"Initiating reconnaissance on: '{task}'\n"
            f"  › Running subdomain enumeration...\n"
            f"  › Querying certificate transparency logs...\n"
            f"   › Fingerprinting exposed assets...\n"
            f"  › Compiling OSINT profile...\n"
            f"  ✓ Recon package ready. Forwarding to HERMES.\n"
        )


class PentestSuite(Agent):
    """
    Web2 & Web3 Hunter.
    Dual-mode offensive agent covering bug bounty and smart
    contract attack surface analysis.
    """

    def __init__(self):
        super().__init__(
            name="PENTEST SUITE",
            role="Web2 & Web3 Hunter",
            tag="OFFENSIVE",
            description=(
                "Dual-mode offensive agent handling Web2 bug bounty hunting "
                "and Web3 smart contract attack surface analysis. Interfaces "
                "with HackerOne, Bugcrowd, and Immunefi workflows."
            ),
            capabilities=[
                "Bug Bounty Hunting",
                "Smart Contract Attacks",
                "Payload Generation",
                "Attack Chain Mapping",
                "DeFi Exploit Analysis",
                "Report Drafting",
            ],
        )

    def process(self, task):
        return (
            f"[PENTEST SUITE — OFFENSIVE]\n"
            f"Engaging target: '{task}'\n"
            f"  › Mapping attack surface (Web2 + Web3)...\n"
            f"  › Generating context-aware payloads...\n"
            f"  › Tracing attack chains...\n"
            f"  › Flagging potential findings for SHANNON validation...\n"
            f"  ✓ Offensive sweep complete. Passing findings upstream.\n"
        )


class ShannonLite(Agent):
    """
    Exploit Validator.
    Applies information-theoretic reasoning to validate findings
    and filter false positives before escalation.
    """

    def __init__(self):
        super().__init__(
            name="SHANNON LITE",
            role="Exploit Validator",
            tag="VALIDATION",
            description=(
                "Named after Claude Shannon. Validates and stress-tests "
                "exploit hypotheses from the crew. Applies information-theoretic "
                "reasoning to assess signal vs noise in vulnerability findings "
                "before escalation."
            ),
            capabilities=[
                "Exploit Validation",
                "False Positive Filtering",
                "Severity Scoring",
                "PoC Verification",
                "Signal Analysis",
            ],
        )

    def process(self, task):
        return (
            f"[SHANNON LITE — VALIDATION]\n"
            f"Validating finding: '{task}'\n"
            f"  › Stress-testing exploit hypothesis...\n"
            f"  › Applying false positive filters...\n"
            f"  › Scoring severity (CVSS + contextual weight)...\n"
            f"  › Verifying proof-of-concept logic...\n"
            f"  ✓ Validation complete. Signal confirmed. Ready for report.\n"
        )


class OpenHack(Agent):
    """
    Source Code Triage Agent.
    Specializes in static analysis of Web2 and Solidity codebases.
    """

    def __init__(self):
        super().__init__(
            name="OPENHACK",
            role="Source Code Triage",
            tag="ANALYSIS",
            description=(
                "Specializes in static analysis and triage of open-source "
                "codebases. Identifies vulnerable patterns, insecure "
                "dependencies, and logic flaws across Web2 and Solidity "
                "contracts. Prioritizes findings by exploitability."
            ),
            capabilities=[
                "Static Analysis",
                "Dependency Auditing",
                "Logic Flaw Detection",
                "Solidity Review",
                "Vulnerability Triage",
                "Code Pattern Matching",
            ],
        )

    def process(self, task):
        return (
            f"[OPENHACK — ANALYSIS]\n"
            f"Triaging codebase: '{task}'\n"
            f"  › Running static analysis pass...\n"
            f"  › Auditing dependency tree for known CVEs...\n"
            f"  › Reviewing Solidity logic for vulnerability classes...\n"
            f"  › Prioritizing findings by exploitability score...\n"
            f"  ✓ Triage complete. Findings ranked and packaged.\n"
        )


class CAI(Agent):
    """
    Raw Hacking Engine.
    Executes low-level attack simulations and fuzzing operations.
    """

    def __init__(self):
        super().__init__(
            name="CAI",
            role="Raw Hacking Engine",
            tag="ENGINE",
            description=(
                "The raw offensive core of the crew. Executes low-level "
                "attack simulations, fuzzes endpoints, and stress-tests "
                "targets. Operates with maximum offensive capability under "
                "Hermes orchestration."
            ),
            capabilities=[
                "Endpoint Fuzzing",
                "Attack Simulation",
                "Brute Force Logic",
                "Vulnerability Probing",
                "Offensive Execution",
                "Stress Testing",
            ],
        )

    def process(self, task):
        return (
            f"[CAI — ENGINE]\n"
            f"Executing against: '{task}'\n"
            f"  › Initiating endpoint fuzzing...\n"
            f"  › Running attack simulations...\n"
            f"  › Probing for vulnerability entry points...\n"
            f"   › Stress-testing edge cases...\n"
            f"  ✓ Engine run complete. Raw output forwarded to HERMES.\n"
        )

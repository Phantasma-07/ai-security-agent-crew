# main.py
# Entry point for the AI Security Agent Crew.
# Run this file to launch the interactive Hermes terminal.
# Author: KyberPhantasma — Kybernos Labs
#
# Usage:
#   python main.py
#
# Requirements:
#   Python 3.6+
#   No external libraries needed — runs on Pydroid3

from hermes import Hermes


BANNER = """
██╗  ██╗██╗   ██╗██████╗ ███████╗██████╗ ███╗   ██╗ ██████╗ ███████╗
██║ ██╔╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗████╗  ██║██╔═══██╗██╔════╝
█████╔╝  ╚████╔╝ ██████╔╝█████╗  ██████╔╝██╔██╗ ██║██║   ██║███████╗
██╔═██╗   ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║╚██╗██║██║   ██║╚════██║
██║  ██╗   ██║   ██████╔╝███████╗██║  ██║██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

  AI SECURITY AGENT CREW — KYBERNOS LABS
  Orchestrated by HERMES via MCP Architecture
  KyberPhantasma · Work in Progress · 2025
"""

HELP_TEXT = """
┌─────────────────────────────────────────────────┐
│  HERMES COMMAND REFERENCE                       │
├─────────────────────────────────────────────────┤
│  status          — Show crew status             │
│  dispatch <task> — Route task to best agent     │
│  broadcast <task>— Send task to all agents      │
│  profile <name>  — View agent profile           │
│  memory          — Show operation memory log    │
│  agents          — List all agents              │
│  help            — Show this menu               │
│  exit            — Shut down Hermes             │
├─────────────────────────────────────────────────┤
│  DISPATCH EXAMPLES:                             │
│  dispatch recon target.com                      │
│  dispatch fuzz api endpoint                     │
│  dispatch validate SQL injection finding        │
│  dispatch solidity ERC-20 code review           │
│  broadcast full security sweep                  │
└─────────────────────────────────────────────────┘
"""


def list_agents(hermes):
    """Print a simple numbered list of all crew agents."""
    border = "─" * 48
    print(border)
    print("  REGISTERED AGENTS")
    print(border)
    for i, (name, agent) in enumerate(hermes.crew.items(), 1):
        print(f"  {i}. {name:<18} [{agent.tag}]")
    print(border)


def run():
    """Main loop — launches the Hermes interactive terminal."""
    print(BANNER)

    # Boot Hermes and register crew
    print("  Booting HERMES...")
    hermes = Hermes()
    print("  ✓ Crew online. All agents registered.\n")
    print("  Type 'help' for commands or 'exit' to quit.\n")

    while True:
        try:
            raw = input("HERMES › ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n[HERMES] Shutdown signal received. Crew standing down.")
            break

        if not raw:
            continue

        # Normalise input
        parts = raw.split(maxsplit=1)
        command = parts[0].lower()
        argument = parts[1] if len(parts) > 1 else ""

        # ── Command Handling ──────────────────────────────

        if command == "exit":
            print("\n[HERMES] All agents standing down. Session terminated.")
            break

        elif command == "help":
            print(HELP_TEXT)

        elif command == "status":
            print(hermes.crew_status())

        elif command == "agents":
            list_agents(hermes)

        elif command == "memory":
            print(hermes.show_memory())

        elif command == "dispatch":
            if not argument:
                print("[HERMES] Error: No task provided. Usage: dispatch <task>")
            else:
                print()
                print(hermes.dispatch(argument))

        elif command == "broadcast":
            if not argument:
                print("[HERMES] Error: No task provided. Usage: broadcast <task>")
            else:
                print()
                print(hermes.dispatch_all(argument))

        elif command == "profile":
            if not argument:
                print("[HERMES] Error: Provide an agent name. Usage: profile <name>")
            else:
                print()
                print(hermes.agent_profile(argument))

        else:
            print(f"[HERMES] Unknown command: '{command}'. Type 'help' for options.")


if __name__ == "__main__":
    run()

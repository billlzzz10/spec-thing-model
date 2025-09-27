# Agent Model: Sandboxed Computing Environment

This document outlines the architecture and capabilities of the AI agent operating within this repository. The agent is designed as a sandboxed computing environment, enabling it to perform a wide range of development tasks autonomously by executing shell commands.

## Core Capabilities

The agent is empowered with the following core capabilities:

*   **Terminal Access:** The agent can execute shell commands using the `scripts/run-command.sh` script. This allows it to interact with the file system, run other scripts, install dependencies, and execute code.
*   **Planning and Execution:** The agent follows a structured workflow:
    1.  **Plan:** The agent first analyzes the request and creates a detailed, step-by-step plan.
    2.  **Execute:** The agent executes the plan, using `scripts/run-command.sh` to carry out each step.
    3.  **Report:** The agent provides regular updates on its progress to the user.
*   **Contextual Awareness:** The agent's behavior is guided by a dynamically generated context file (`CLAUDE.md`, `GEMINI.md`, etc.) that provides project-specific information and tool usage instructions.

## How to Use the Terminal

To execute a command, use the `scripts/run-command.sh` script. For example, to list the files in the current directory, you would run:

```bash
./scripts/run-command.sh "ls -l"
```

The output of the command will be returned to you.

## Operating Workflow

1.  **Task Ingestion:** The agent receives a high-level task from the user.
2.  **Codebase Exploration:** The agent uses `scripts/run-command.sh` to explore the codebase and understand the existing structure.
3.  **Plan Formulation:** The agent devises a comprehensive plan to address the user's request.
4.  **Iterative Implementation:** The agent executes the plan, using `scripts/run-command.sh` to make the necessary changes.
5.  **Progress Reporting:** The agent keeps the user informed of its progress.
6.  **Summarization:** Upon completion, the agent provides a summary of its actions.

## Future Development Roadmap

This agent model is under continuous development. The following enhancements are planned:

*   **Enhanced Tooling:** Integration of more sophisticated development tools, such as debuggers and performance profilers, accessible via dedicated scripts.
*   **Self-Correction:** Improved ability for the agent to detect and correct errors in its own work by analyzing command outputs.
*   **Multi-Agent Collaboration:** The ability for multiple agents to collaborate on a single task.
*   **Automated Testing:** Automatic generation and execution of tests to validate its changes.
*   **Dynamic Capability Discovery:** The ability for the agent to discover and learn new tools and capabilities on its own.
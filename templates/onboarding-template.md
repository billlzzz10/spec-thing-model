# Onboarding Analysis for Existing Project

This document outlines the steps to analyze an existing ("brownfield") project to prepare it for spec-driven development. The goal is to understand the project's structure, dependencies, and conventions before creating new features.

## Step 1: Understand the Project Structure

First, let's get a high-level overview of the project's layout.

**Action:**
*   List the files and directories in the root of the project to understand the overall structure. Pay close attention to directories like `src`, `source`, `app`, `lib`, `tests`, `docs`, etc.

**Recommended Command:**
```bash
./scripts/run-command.sh "ls -lF"
```

**Analysis:**
*   *Document the key directories and their apparent purpose here.*
*   *Is this a standard project structure for its language/framework (e.g., a standard Maven, Gradle, or npm project)?*
*   *Where does the main application logic seem to reside?*
*   *Where are the tests located?*

## Step 2: Identify Dependencies and Build Tools

Next, identify how the project is built and what its dependencies are.

**Action:**
*   Look for dependency management files (e.g., `package.json`, `requirements.txt`, `pom.xml`, `build.gradle`, `Cargo.toml`).
*   Read the contents of these files to understand the project's dependencies.

**Recommended Commands:**
```bash
# For Node.js projects
./scripts/run-command.sh "cat package.json"

# For Python projects
./scripts/run-command.sh "cat requirements.txt"

# For Maven projects
./scripts/run-command.sh "cat pom.xml"

# For Gradle projects
./scripts/run-command.sh "cat build.gradle"
```

**Analysis:**
*   *What is the primary programming language and framework?*
*   *What are the key libraries or dependencies?*
*   *Are there any custom build scripts or configurations?*
*   *What is the command to build the project?*

## Step 3: Understand and Run Tests

A project's tests are a great source of information about its behavior.

**Action:**
*   Identify the testing framework and how to run the tests. This information is often in the `README.md` or a dependency file (e.g., `pytest` in `requirements.txt`, `jest` in `package.json`).
*   Run the test suite to ensure the project is in a working state.

**Recommended Command:**
*   *This will vary by project. Based on your findings from Step 2, determine the correct command.*
*   Example for a Node.js project: `./scripts/run-command.sh "npm install && npm test"`
*   Example for a Python project with pytest: `./scripts/run-command.sh "pip install -r requirements.txt && pytest"`

**Analysis:**
*   *What testing framework is used?*
*   *What is the command to run the tests?*
*   *Do all the tests pass? If not, what are the errors?*
*   *What is the overall test coverage like (if you can tell)?*

## Step 4: Initial Onboarding Summary

Based on your analysis, provide a summary of the project.

**Summary:**
*   **Project Purpose:** *Briefly describe what the project does.*
*   **Tech Stack:** *List the primary language, framework, and key dependencies.*
*   **Build Process:** *How is the project built and run?*
*   **Testing Strategy:** *How are tests run, and what is their status?*
*   **Next Steps:** *What are the immediate next steps to begin working on a new feature? (e.g., create a new spec, write a failing test, etc.)*
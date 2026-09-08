# Jan-SahayakAI

Jan-SahayakAI is an AI-powered Good Neighbour Agent designed to help residents with civic problems and government benefits. It acts as an operations assistant for citizens by identifying problems, reasoning about required actions, selecting appropriate tools, and explaining next steps.

## Features
- **Civic Issue Identification:** Helps identify issues like potholes, garbage accumulation, and broken streetlights.
- **Complaint Preparation:** Collects missing information and automatically prepares structured civic complaints.
- **Department Routing:** Intelligently routes issues to the correct mock government department.
- **Complaint Tracking:** Allows users to track the status of their complaints.
- **Follow-ups:** Provides guidance on the next action to take for an existing complaint.
- **Government Scheme Discovery:** Searches a small JSON-backed set of schemes from official government sources.
- **Preliminary Eligibility Checking:** Performs initial eligibility checks for schemes (Prototype).

## Prerequisites
- Python 3.10+
- AWS Account with Amazon Bedrock enabled
- Access to **Anthropic Claude 3.5 Sonnet** (or Claude Sonnet 4.6) requested in the AWS Bedrock Console.

## Setup Instructions

1. **Activate the virtual environment:**
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. **Ensure dependencies are installed:**
   ```powershell
   pip install strands-agents boto3 botocore[crt]
   ```

3. **Configure AWS:**
   Ensure your AWS CLI is authenticated (`aws configure` or SSO) and points to a region where you have Claude access (e.g., `ap-south-1`).

4. **Run the agent:**
   ```powershell
   python app.py
   ```

## Architecture
This project uses [Strands Agents](https://github.com/strands-agents/harness-sdk) to connect Claude (via Amazon Bedrock) with Python-based tools. 
For scheme discovery in Part 9, the flow is:

```text
Agent -> search_schemes() -> data/schemes/schemes.json
```

This is an intermediate knowledge-source architecture. Part 10 will replace or augment it with official-document RAG; RAG is not included yet. For more details, see `documentation.md`.

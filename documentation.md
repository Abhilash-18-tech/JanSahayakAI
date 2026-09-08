# Jan-SahayakAI Technical Documentation

## Overview
Jan-SahayakAI uses the **Strands Agents** framework to create an AI assistant that can reason and use tools. The LLM acts as the brain, while Python functions act as deterministic tools the LLM can call to interact with the outside world (or in our case, mock databases).

## System Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │  Jan-SahayakAI  │ (app.py -> agents/jan_sahayak.py)
                  │  Strands Agent  │
                  └────────┬────────┘
                           │
                       Claude/LLM
                           │
       ┌───────────────────┼────────────────────┐
       │                   │                    │
       ▼                   ▼                    ▼
 Civic Tools         Scheme Tools        Follow-up Tools
       │                   │                    │
       │                   ▼                    │
       │          ┌─────────────────┐            │
                           │          │ Scheme Knowledge│            │
                           │          │ JSON Prototype  │            │
       │          └─────────────────┘            │
       │                   │                    │
       ▼                   ▼                    ▼
 Complaint System   Scheme Information    Complaint Status
```

## Directory Structure

- `app.py`: The main entry point. Initializes the agent and handles the CLI loop.
- `agents/jan_sahayak.py`: Defines the agent, its system prompt, and connects its tools.
- `tools/`: Contains all the deterministic tools the agent can call.
  - `civic.py`: Tools for creating complaints and identifying departments.
  - `complaint.py`: Tool for tracking complaints.
  - `followup.py`: Tool for advising on complaint follow-ups.
  - `schemes.py`: JSON-backed tools for searching schemes, checking preliminary eligibility, and reading details.
- `data/`: Mock data storage layer.
  - `store.py`: A mock in-memory database to store civic complaints.
  - `schemes/schemes.json`: Official-source scheme records used by the Part 9 prototype.

## Civic Tool Definitions

### `create_civic_complaint(issue, location, description)`
Takes user input, uses `identify_department` to find the correct authority, generates a mock ID, and saves the structured JSON to the local store.

### `identify_department(issue, location)`
Uses simple keyword matching to determine the likely responsible government department.

### `track_complaint(complaint_id)`
Looks up a complaint ID in the mock database and returns its current status and details.

### `follow_up_complaint(complaint_id)`
Checks the status of an existing complaint and returns a recommended next action for the user.

## Government Scheme Tool Definitions

*Note: Part 9 scheme tools operate on an intermediate JSON-backed knowledge source (`data/schemes/schemes.json`). Every result includes an official source and requires current eligibility verification.*

### `search_schemes(category=None, location=None)`
Loads `data/schemes/schemes.json`, then filters by category and location case-insensitively. Nationwide schemes are returned for a supplied state or location because they apply across India.

### `check_scheme_eligibility(scheme_id, user_data)`
Performs a PRELIMINARY eligibility check by comparing provided user data against the scheme's requirements. It identifies missing information and returns a status like `POTENTIALLY_ELIGIBLE` or `MORE_INFORMATION_NEEDED`.

### `get_scheme_details(scheme_id)`
Retrieves full details about a specific JSON-backed scheme, including its eligibility notes, benefits, documents, authority, and official source.

## Future Milestones
- **Part 10 RAG Integration:** Upgrade or augment the JSON prototype with official government documents processed via document ingestion, chunking, embeddings, and vector retrieval (RAG). This has not been implemented.
- Connecting the mock complaint database to a real persistent database (e.g., SQLite, PostgreSQL).
- Frontend UI (e.g., Streamlit or React).

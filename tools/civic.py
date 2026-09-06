import json
from strands import tool
from data.store import save_complaint

def _identify_department(issue: str, location: str) -> str:
    """Internal function to identify the department."""
    issue_lower = issue.lower()
    if "pothole" in issue_lower or "road" in issue_lower:
        return "Municipal Corporation (Roads Department)"
    elif "garbage" in issue_lower or "sanitation" in issue_lower:
        return "Municipal Corporation (Solid Waste Management)"
    elif "water" in issue_lower or "drainage" in issue_lower:
        return "Water Supply and Sewerage Board"
    elif "streetlight" in issue_lower or "electricity" in issue_lower:
        return "Electricity Board"
    else:
        return "General Civic Administration"

@tool
def identify_department(issue: str, location: str) -> str:
    """
    Identify the likely responsible civic authority or department for a given issue.

    Args:
        issue: Type of civic issue (e.g., pothole, garbage, water).
        location: Location where the issue occurred.
    """
    return _identify_department(issue, location)

@tool
def create_civic_complaint(
    issue: str,
    location: str,
    description: str
) -> str:
    """
    Create a civic complaint and return structured complaint details.

    Args:
        issue: Type of civic issue.
        location: Location where the issue occurred.
        description: Detailed description of the issue.
    """
    
    # Use our internal logic to get the department
    department = _identify_department(issue, location)
    
    complaint_data = {
        "issue": issue,
        "location": location,
        "description": description,
        "department": department,
        "priority": "High" if "dangerous" in description.lower() or "urgent" in description.lower() else "Normal",
        "status": "READY_FOR_SUBMISSION"
    }
    
    # Save to mock database
    complaint_id = save_complaint(complaint_data)
    
    # Return formatted JSON string
    return json.dumps(complaint_data, indent=2)
import json
from strands import tool
from data.store import get_complaint

@tool
def track_complaint(complaint_id: str) -> str:
    """
    Track the status of a civic complaint.

    Args:
        complaint_id: The unique identifier of the complaint (e.g., JSA-2026-0001).
    """
    complaint = get_complaint(complaint_id)
    
    if not complaint:
        return json.dumps({
            "error": f"Complaint ID '{complaint_id}' not found.",
            "status": "NOT_FOUND"
        }, indent=2)
        
    return json.dumps({
        "complaint_id": complaint_id,
        "issue": complaint.get("issue"),
        "status": complaint.get("status"),
        "department": complaint.get("department"),
        "created_at": complaint.get("created_at")
    }, indent=2)

import json
from strands import tool
from data.store import get_complaint, update_complaint_status

@tool
def follow_up_complaint(complaint_id: str) -> str:
    """
    Follow up on an existing civic complaint.

    Args:
        complaint_id: The unique identifier of the complaint (e.g., JSA-2026-0001).
    """
    complaint = get_complaint(complaint_id)
    
    if not complaint:
        return json.dumps({
            "error": f"Complaint ID '{complaint_id}' not found.",
            "status": "NOT_FOUND"
        }, indent=2)
        
    current_status = complaint.get("status")
    
    # Mock follow-up logic based on status
    if current_status == "READY_FOR_SUBMISSION":
        next_action = "Please submit the complaint to the appropriate department."
    elif current_status == "SUBMITTED":
        next_action = "Complaint is awaiting assignment. Please check back in 24 hours."
    elif current_status == "ASSIGNED":
        next_action = "Workers have been assigned. Resolution is pending."
    elif current_status == "IN_PROGRESS":
        next_action = "Work is currently ongoing."
    elif current_status == "RESOLVED":
        next_action = "This issue has already been resolved."
    else:
        next_action = "Contact the department for more information."
        
    return json.dumps({
        "complaint_id": complaint_id,
        "current_status": current_status,
        "recommended_next_action": next_action,
        "note": "This is a demo follow-up. No real government action was taken."
    }, indent=2)

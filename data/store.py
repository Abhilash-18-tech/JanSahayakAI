import datetime

# Mock database to store complaints
# Format: { complaint_id: { details... } }
MOCK_COMPLAINTS_DB = {}

def generate_complaint_id() -> str:
    """Generate a mock complaint ID."""
    current_year = datetime.datetime.now().year
    count = len(MOCK_COMPLAINTS_DB) + 1
    return f"JSA-{current_year}-{count:04d}"

def save_complaint(complaint_data: dict) -> str:
    """Save a complaint and return its generated ID."""
    complaint_id = generate_complaint_id()
    
    # Add metadata
    complaint_data["complaint_id"] = complaint_id
    complaint_data["created_at"] = datetime.datetime.now().isoformat()
    if "status" not in complaint_data:
        complaint_data["status"] = "CREATED"
        
    MOCK_COMPLAINTS_DB[complaint_id] = complaint_data
    return complaint_id

def get_complaint(complaint_id: str) -> dict | None:
    """Retrieve a complaint by ID."""
    return MOCK_COMPLAINTS_DB.get(complaint_id)

def update_complaint_status(complaint_id: str, new_status: str) -> bool:
    """Update the status of an existing complaint."""
    if complaint_id in MOCK_COMPLAINTS_DB:
        MOCK_COMPLAINTS_DB[complaint_id]["status"] = new_status
        return True
    return False

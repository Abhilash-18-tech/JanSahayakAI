from strands import tool


@tool
def create_civic_complaint(
    issue: str,
    location: str,
    description: str
) -> str:
    """
    Create a civic complaint.

    Args:
        issue: Type of civic issue.
        location: Location where the issue occurred.
        description: Detailed description of the issue.
    """

    return (
        f"Complaint prepared successfully.\n"
        f"Issue: {issue}\n"
        f"Location: {location}\n"
        f"Description: {description}\n"
        f"Status: Ready for submission"
    )
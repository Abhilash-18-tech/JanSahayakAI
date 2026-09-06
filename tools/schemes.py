import json
from strands import tool
from data.schemes_data import SCHEMES

@tool
def search_government_schemes(
    state: str = None,
    age: int = None,
    income_range: str = None,
    occupation: str = None,
    is_student: bool = None,
    rural_urban: str = None,
    keywords: list[str] = None
) -> str:
    """
    Search the Jan-SahayakAI prototype government scheme dataset based on user characteristics.
    The agent should call this when a user asks about available schemes.

    Args:
        state: State of residence (e.g., "Telangana", "All").
        age: Age of the user.
        income_range: Approximate income or class (e.g., "low_income", "middle_income").
        occupation: Current occupation (e.g., "farmer", "student").
        is_student: Whether the user or their children are students.
        rural_urban: Whether the user lives in a "rural" or "urban" area.
        keywords: General keywords representing the user's situation (e.g., ["children", "pregnant"]).
    """
    results = []
    
    for scheme in SCHEMES:
        score = 0
        reasons = []
        
        # State match
        if state and scheme["state"].lower() != "all":
            if state.lower() == scheme["state"].lower():
                score += 2
                reasons.append(f"Matches state: {state}")
            else:
                continue # Strict exclusion if state doesn't match
                
        # Age match
        if age and scheme["age_requirements"]:
            min_age = scheme["age_requirements"].get("min")
            max_age = scheme["age_requirements"].get("max")
            if min_age and age < min_age: continue
            if max_age and age > max_age: continue
            score += 1
            
        # Target groups / keywords
        target_groups = scheme.get("target_groups", [])
        if income_range and "low_income" in income_range.lower() and "low_income" in target_groups:
            score += 1
            reasons.append("Targets low-income families")
            
        if occupation and scheme.get("occupation_requirements"):
            if occupation.lower() in [req.lower() for req in scheme["occupation_requirements"]]:
                score += 2
                reasons.append(f"Matches occupation: {occupation}")
                
        if is_student and "students" in target_groups:
            score += 2
            reasons.append("Provides student benefits")
            
        if rural_urban and rural_urban.lower() in target_groups:
            score += 1
            reasons.append(f"Matches area type: {rural_urban}")
            
        if keywords:
            for kw in keywords:
                if kw.lower() in target_groups or kw.lower() in scheme["description"].lower():
                    score += 1
                    reasons.append(f"Related to: {kw}")
                    
        # Include scheme if it scored any points or if no filters were applied (broad search)
        if score > 0 or not any([state, age, income_range, occupation, is_student, rural_urban, keywords]):
            results.append({
                "scheme_id": scheme["scheme_id"],
                "scheme_name": scheme["scheme_name"],
                "category": scheme["category"],
                "why_relevant": ", ".join(list(set(reasons))) if reasons else "General potential fit.",
                "benefits": scheme["benefits"],
                "verification_required": True
            })
            
    # Sort by relevance score if we had a complex scoring mechanism, for now just return
    if not results:
        return json.dumps({"message": "No schemes found matching the criteria in the prototype dataset."})
        
    return json.dumps(results, indent=2)


@tool
def check_scheme_eligibility(scheme_id: str, user_data: dict) -> str:
    """
    Perform a PRELIMINARY eligibility check for a specific scheme using available user information.

    Args:
        scheme_id: The ID of the scheme (e.g., 'SCH-001').
        user_data: A dictionary containing known facts about the user (e.g., {"age": 20, "income": 50000, "occupation": "student"}).
    """
    scheme = next((s for s in SCHEMES if s["scheme_id"] == scheme_id), None)
    if not scheme:
        return json.dumps({"error": f"Scheme {scheme_id} not found."})
        
    matched = []
    missing = []
    unverified = []
    
    # Check age
    if scheme["age_requirements"]:
        if "age" in user_data:
            age = user_data["age"]
            min_age = scheme["age_requirements"].get("min")
            max_age = scheme["age_requirements"].get("max")
            if min_age and age < min_age:
                return json.dumps({"preliminary_status": "LIKELY_NOT_ELIGIBLE", "reason": f"Age {age} is below minimum {min_age}."})
            if max_age and age > max_age:
                return json.dumps({"preliminary_status": "LIKELY_NOT_ELIGIBLE", "reason": f"Age {age} is above maximum {max_age}."})
            matched.append(f"Age {age} fits requirements.")
        else:
            missing.append("age")
            
    # Check income
    if scheme["income_limit"]:
        if "income" in user_data:
            if user_data["income"] > scheme["income_limit"]:
                return json.dumps({"preliminary_status": "LIKELY_NOT_ELIGIBLE", "reason": f"Income exceeds limit of {scheme['income_limit']}."})
            matched.append("Income within limit.")
        else:
            missing.append("annual_income")
            
    # Check state
    if scheme["state"] != "All":
        if "state" in user_data:
            if user_data["state"].lower() != scheme["state"].lower():
                return json.dumps({"preliminary_status": "LIKELY_NOT_ELIGIBLE", "reason": f"Scheme is specific to {scheme['state']}."})
            matched.append(f"Resident of {scheme['state']}.")
        else:
            missing.append("state_of_residence")
            
    # Check occupation
    if scheme["occupation_requirements"]:
        if "occupation" in user_data:
            if user_data["occupation"].lower() not in [req.lower() for req in scheme["occupation_requirements"]]:
                unverified.append(f"Occupation does not explicitly match: {scheme['occupation_requirements']}")
            else:
                matched.append(f"Occupation matches {user_data['occupation']}.")
        else:
            missing.append("occupation")

    status = "POTENTIALLY_ELIGIBLE"
    if missing:
        status = "MORE_INFORMATION_NEEDED"

    return json.dumps({
        "scheme_name": scheme["scheme_name"],
        "preliminary_status": status,
        "matched_conditions": matched,
        "missing_information": missing,
        "unverified_conditions": unverified,
        "verification_required": True,
        "note": "This is a prototype eligibility rule — verify against the official government source."
    }, indent=2)


@tool
def get_scheme_details(scheme_id: str) -> str:
    """
    Get full detailed information about a specific scheme.

    Args:
        scheme_id: The ID of the scheme (e.g., 'SCH-001').
    """
    scheme = next((s for s in SCHEMES if s["scheme_id"] == scheme_id), None)
    if not scheme:
        return json.dumps({"error": f"Scheme {scheme_id} not found."})
        
    return json.dumps({
        "scheme_name": scheme["scheme_name"],
        "purpose": scheme["description"],
        "benefits": scheme["benefits"],
        "target_beneficiaries": scheme["target_groups"],
        "documents_required": scheme["documents_required"],
        "application_process": scheme["application_method"],
        "official_source": scheme.get("official_source", "Official source not yet configured in prototype."),
        "important_note": "This data is PROTOTYPE only. Official verification is required."
    }, indent=2)

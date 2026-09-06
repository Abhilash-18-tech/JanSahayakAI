"""
MOCK DATA: Government Schemes Prototype Dataset

IMPORTANT:
This is a prototype dataset. Do NOT treat these rules as official or legally binding.
Any eligibility indicated here is PRELIMINARY and requires verification against official government sources.
"""

SCHEMES = [
    {
        "scheme_id": "SCH-001",
        "scheme_name": "PM Vidyalakshmi Education Scheme (Prototype)",
        "description": "Financial assistance for students from low-income families pursuing higher education.",
        "category": "Education",
        "target_groups": ["students", "low_income"],
        "state_or_central": "Central",
        "state": "All",
        "age_requirements": {"min": 16, "max": 25},
        "income_limit": 800000,
        "occupation_requirements": ["student"],
        "gender_requirements": None,
        "disability_requirements": None,
        "education_requirements": ["high_school_graduate"],
        "family_requirements": None,
        "benefits": "Scholarship up to Rs. 50,000 per year for higher education.",
        "documents_required": ["Income Certificate", "Aadhar Card", "10th/12th Marksheet", "Admission Letter"],
        "official_source": "https://www.myscheme.gov.in (Prototype Link)",
        "application_method": "Online portal"
    },
    {
        "scheme_id": "SCH-002",
        "scheme_name": "Rural Housing Assistance (Prototype)",
        "description": "Subsidies for building pucca houses in rural areas for families below poverty line.",
        "category": "Housing",
        "target_groups": ["rural", "low_income", "bpl"],
        "state_or_central": "Central",
        "state": "All",
        "age_requirements": {"min": 18, "max": None},
        "income_limit": 200000,
        "occupation_requirements": None,
        "gender_requirements": None,
        "disability_requirements": None,
        "education_requirements": None,
        "family_requirements": ["no_pucca_house"],
        "benefits": "Financial assistance of Rs. 1,20,000 in plains and Rs. 1,30,000 in hilly areas.",
        "documents_required": ["BPL Card", "Aadhar Card", "Bank Passbook", "Land Ownership Document"],
        "official_source": "https://rhreporting.nic.in (Prototype Link)",
        "application_method": "Gram Panchayat"
    },
    {
        "scheme_id": "SCH-003",
        "scheme_name": "Telangana Rythu Bandhu (Prototype)",
        "description": "Investment support scheme for farmers in Telangana.",
        "category": "Agriculture",
        "target_groups": ["farmers", "land_owners"],
        "state_or_central": "State",
        "state": "Telangana",
        "age_requirements": {"min": 18, "max": None},
        "income_limit": None,
        "occupation_requirements": ["farmer"],
        "gender_requirements": None,
        "disability_requirements": None,
        "education_requirements": None,
        "family_requirements": None,
        "benefits": "Rs. 5,000 per acre per season to support farm investment.",
        "documents_required": ["Pattadar Passbook", "Aadhar Card", "Bank Account details"],
        "official_source": "https://rythubandhu.telangana.gov.in (Prototype Link)",
        "application_method": "Agricultural Extension Officer"
    },
    {
        "scheme_id": "SCH-004",
        "scheme_name": "National Child Nutrition Program (Prototype)",
        "description": "Nutritional support for pregnant women and children under 6 years.",
        "category": "Health",
        "target_groups": ["pregnant_women", "children", "mothers"],
        "state_or_central": "Central",
        "state": "All",
        "age_requirements": None,
        "income_limit": None,
        "occupation_requirements": None,
        "gender_requirements": ["female"], # Also applies to children, but simplifying for prototype
        "disability_requirements": None,
        "education_requirements": None,
        "family_requirements": ["pregnant_or_infant"],
        "benefits": "Supplementary nutrition, health checkups, and immunization.",
        "documents_required": ["Aadhar Card", "Mother and Child Protection (MCP) Card"],
        "official_source": "Local Anganwadi Centre",
        "application_method": "In-person at Anganwadi"
    }
]

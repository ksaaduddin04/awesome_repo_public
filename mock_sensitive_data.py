# -----------------------------
# Mock Personally Identifiable Information (PII)
# -----------------------------

user_profile = {
    "full_name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+1-555-123-4567",
    "address": "1234 Elm Street, Springfield, IL 62701"
}

# -----------------------------
# Mock Social Security Number (FAKE)
# -----------------------------
social_security_number = "123-45-6789"  # Fake sample format

# -----------------------------
# Mock Credit Card Information (FAKE)
# -----------------------------
credit_card_info = {
    "cardholder_name": "John Doe",
    "card_number": "4111 1111 1111 1111",  # Test Visa number (commonly used for testing)
    "expiry_date": "12/30",
    "cvv": "123"
}

# -----------------------------
# Mock Protected Health Information (PHI) - FAKE
# -----------------------------
phi_data = {
    "patient_id": "PAT-00001",
    "diagnosis": "Hypertension",
    "prescription": "Lisinopril 10mg",
    "doctor": "Dr. Smith",
    "visit_date": "2026-01-15"
}

if __name__ == "__main__":
    print("Mock user profile:", user_profile)
    print("Mock SSN:", social_security_number)
    print("Mock credit card info:", credit_card_info)
    print("Mock PHI data:", phi_data)

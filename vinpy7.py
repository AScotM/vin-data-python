import re

def is_valid_vin(vin):
    """Simple VIN validation: check length and forbidden characters."""
    vin = vin.upper()
    return len(vin) == 17 and not any(c in "IOQ" for c in vin)

def extract_vins(text):
    """
    Extracts any 17-character alphanumeric sequence (loose filtering).
    We allow all characters in A-Z and 0-9 to ensure we catch potential invalid VINs too.
    """
    pattern = r'\b[\w\d]{17}\b'  # More relaxed, allows any 17-char alphanumeric string
    return re.findall(pattern, text)

# Example input text (similar to PHP version)
input_text = """
Here are some sample VINs:
1HGCM82633A123456, WDBBA48D7KA093694, and incorrect ones like ABC1234INVALID5678, 5YJSA1E26FF10130O (with an O).
"""

# Extract VINs from text
vin_list = extract_vins(input_text)

# Validate each extracted VIN
valid_vins = [vin for vin in vin_list if is_valid_vin(vin)]
invalid_vins = [vin for vin in vin_list if not is_valid_vin(vin)]

# Print results
print("\n Valid VINs:")
for vin in valid_vins:
    print(f"  - {vin}")
if not valid_vins:
    print("  (None found)")

print("\n Invalid VINs:")
for vin in invalid_vins:
    print(f"  - {vin}")
if not invalid_vins:
    print("  (None found)")

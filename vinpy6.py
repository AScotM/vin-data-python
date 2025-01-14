import re

def is_valid_vin(vin):
    """
    Validate a VIN.
    
    :param vin: str - The VIN to validate
    :return: bool - True if valid, False otherwise
    """
    print(f"Validating VIN: {vin}")  # Debugging

    # Check the length
    if len(vin) != 17:
        print(f"  Invalid length for VIN: {vin}")
        return False

    # Ensure it does not contain invalid characters
    if re.search(r"[IOQ]", vin):
        print(f"  VIN contains invalid characters: {vin}")
        return False

    return True

def extract_vins(text):
    """
    Extract potential VINs from a given string.
    
    :param text: str - The text to search for VINs
    :return: list - A list of potential VIN-like strings
    """
    # More permissive regex to capture any sequence of 17 or more characters
    pattern = r"\b([A-Za-z0-9]{17,})\b"
    matches = re.findall(pattern, text)
    print(f"Extracted potential VINs: {matches}")  # Debugging
    return matches

# Example usage
input_text = """
Here are some sample VINs:
1HGCM82633A123456, WDBBA48D7KA093694, and incorrect ones like ABC1234INVALID5678.
"""

# Extract potential VINs
vin_list = extract_vins(input_text)

# Categorize VINs
valid_vins = []
invalid_vins = []
for vin in vin_list:
    if is_valid_vin(vin):
        valid_vins.append(vin)
    else:
        invalid_vins.append(vin)

# Display results
print("\nValid VINs:")
if valid_vins:
    for vin in valid_vins:
        print(f"  {vin}")
else:
    print("  None")

print("\nInvalid VINs:")
if invalid_vins:
    for vin in invalid_vins:
        print(f"  {vin}")
else:
    print("  None")


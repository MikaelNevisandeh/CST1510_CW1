"""
Cyber Security Mini-Project: Parsing Messy Log Entries (Pass Criteria).
"""

def parse_line(raw_line):
    """Cleans a messy raw string line and returns a structured dictionary."""
    # Strip whitespace and make everything lowercase
    cleaned = raw_line.strip().lower()
    
    # Split the main source part from the rest of the attributes
    src_part, rest = cleaned.split(",", 1)
    
    # Isolate the IP address string value
    _, ip_address = src_part.split("=")
    
    # Initialize dictionary with the clean label key and string IP
    result = {"src": ip_address.strip()}
    
    # Loop over the remaining segments to extract keys and values
    for piece in rest.split(","):
        key, val = piece.split("=")
        clean_key = key.strip()
        clean_val = val.strip()
        
        # Check if the value is purely a number before converting
        if clean_val.isdigit():
            result[clean_key] = int(clean_val)
        else:
            result[clean_key] = clean_val  # Keep it as a string if it is text like "failed"
            
    return result


def main():
    """Main program execution flow."""
    # Threshold Pass Standard: 5 genuinely messy raw lines directly inside the code
    raw_lines = [
        "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
        "  src=192.168.1.50 , attempts=450 , result=failed  ",
        "Src=172.16.0.22,attempts=5,result=failed",
        "src=10.0.0.15,  ATTEMPTS=150,  result=failed",
        "  SRC=192.168.1.90,attempts=95,result=failed  "
    ]

    print("--- Cleaned Cyber Security Logs ---")
    
    # Clean and print each record array dictionary to the screen
    for line in raw_lines:
        cleaned_dict = parse_line(line)
        print(cleaned_dict)


if __name__ == "__main__":
    main()

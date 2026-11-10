"""
Cyber Security Mini-Project: Monitoring Failed Login Attempts.
"""

def check_record(record):
    """Determines if a security record has exceeded its allowed limit."""
    if record["value"] > record["limit"]:
        return "OVER LIMIT"
    else:
        return "OK"


def print_report(record, status):
    """Prints a clear report for a single IP address record."""
    print(f"IP: {record['label']:<15} | Failed: {record['value']:<4} / Total: {record['limit']:<4} -> Status: {status}")


def main():
    """Main program execution flow."""
    # Threshold Pass Standard: Hardcoded list of at least 3 dictionaries directly in the code
    records = [
        {"label": "10.0.0.5", "value": 12, "limit": 400},
        {"label": "192.168.1.50", "value": 450, "limit": 400},
        {"label": "172.16.0.22", "value": 5, "limit": 10},
        {"label": "10.0.0.15", "value": 150, "limit": 100}
    ]

    print("--- Cyber Security Status Report ---")
    
    # Loop over your records and print a report for each
    for record in records:
        status = check_record(record)
        print_report(record, status)


if __name__ == "__main__":
    main()





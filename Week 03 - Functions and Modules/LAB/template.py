"""
Cyber Security Mini-Project: Functional Threat Record Check (Week 3 Pass Criteria).
"""

def status_of(percent):
    """Returns the security warning status based on failed attempt percentages."""
    if percent >= 100:
        return "OVER LIMIT"
    else:
        return "OK"


def main():
    """Main program execution flow."""
    # 1. Ask user for the three lane-specific inputs
    source_ip = input("Enter Source IP: ")
    failed_logins = int(input("Enter Failed Logins: "))
    total_attempts = int(input("Enter Total Attempts: "))
    
    # 2. Work out difference and percentage inline
    difference = total_attempts - failed_logins
    percent = (failed_logins / total_attempts) * 100
    
    # 3. Call status_of for the threat status
    status = status_of(percent)
    
    # 4. Print the bordered report matching the standard requirements
    print("========================================")
    print(f"RECORD CHECK  -  {source_ip}")
    print("========================================")
    print(f"Failed      : {failed_logins}")
    print(f"Total       : {total_attempts}")
    print(f"Status      : {status}")
    print("========================================")


if __name__ == "__main__":
    main()

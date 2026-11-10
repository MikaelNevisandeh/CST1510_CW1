"""
Cyber Security Mini-Project: Initial Threat Record Check (Week 1 Pass Criteria).
"""

# 1. Ask the user for the three lane-specific values
source_ip = input("Enter Source IP: ")
failed_logins = int(input("Enter Failed Logins: "))
total_attempts = int(input("Enter Total Attempts: "))

# 2. Print them back in a clean, lined bordered report matching the standard layout
print("========================================")
print(f"RECORD CHECK  -  {source_ip}")
print("========================================")
print(f"Failed      : {failed_logins}")
print(f"Total       : {total_attempts}")
print("========================================")

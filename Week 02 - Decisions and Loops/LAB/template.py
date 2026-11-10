"""
Cyber Security Mini-Project: Conditional Threat Record Check (Week 2 Pass Criteria).
"""

# 1. Ask the user for the three lane-specific values
source_ip = input("Enter Source IP: ")
failed_logins = int(input("Enter Failed Logins: "))
total_attempts = int(input("Enter Total Attempts: "))

# 2. Decide the threat status using if / else logic
if failed_logins > total_attempts:
    status = "OVER LIMIT"
else:
    status = "OK"

# 3. Print the values back in a lined bordered report matching the standard layout
print("========================================")
print(f" RECORD CHECK  -  {source_ip}")
print("========================================")
print(f" Failed      : {failed_logins}")
print(f" Total       : {total_attempts}")
print(f" Status      : {status}")
print("========================================")



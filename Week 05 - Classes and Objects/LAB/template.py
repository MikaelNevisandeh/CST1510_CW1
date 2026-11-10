class Record:
    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = failed_logins
        self.total_attempts = total_attempts

    def status(self):
        """Returns the security threat status based on failed login percentage."""
        percentage = (self.failed_logins / self.total_attempts) * 100
        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

# Create two independent record instances
r1 = Record("10.0.0.5", 12, 400)
r2 = Record("192.168.1.50", 450, 400)

# Rule check: Change one to prove independence before printing
r1.failed_logins = 395  # This changes r1 to a WARNING state

# Call status() once per record and store the result in a variable
r1_status = r1.status()
r2_status = r2.status()

# Print bordered report for r1
print("+" + "-" * 50 + "+")
print(f"| IP Address:    {r1.source_ip:<35} |")
print(f"| Logins/Total:  {r1.failed_logins}/{r1.total_attempts:<33} |")
print(f"| Alert Status:  {r1_status:<35} |")
print("+" + "-" * 50 + "+")

print() # Empty line between reports

# Print bordered report for r2
print("+" + "-" * 50 + "+")
print(f"| IP Address:    {r2.source_ip:<35} |")
print(f"| Logins/Total:  {r2.failed_logins}/{r2.total_attempts:<33} |")
print(f"| Alert Status:  {r2_status:<35} |")
print("+" + "-" * 50 + "+")

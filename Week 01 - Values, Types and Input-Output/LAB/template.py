source_ip = input("Enter the source IP address: ")
failed_logins = float(input("Enter the number of failed logins: "))
total_attempts = float(input("Enter the number of total attempts: "))

difference = total_attempts - failed_logins
percent = (failed_logins / total_attempts) * 100

print()
print("==================================")
print(f" RECORD CHECK  -  {source_ip}")
print("==================================")

print(f"Failed Logins:  {failed_logins:>18.2f}")
print(f"Total Attempts: {total_attempts:>18.2f}")
print(f"Difference:     {difference:>+18.2f}")
print(f"Percentage:     {percent:>18.2f}%")

print(f"Analysis:       Review Required")

print("==================================")

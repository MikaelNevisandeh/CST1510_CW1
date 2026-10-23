"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  Cyber
Date  :

Run it:   python template.py
"""


label = input("Enter record label (e.g., Hostname/IP): ")
value = float(input("Enter current value: "))
limit = float(input("Enter safety limit: "))



difference = value - limit
percent = (value / limit) * 100


if percent >= 100.0:
    status = "OVER LIMIT"
elif percent >= 90.0:
    status = "WARNING"
else:
    status = "OK"



print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Current Value: {value:>19.2f}")
print(f"Safety Limit:  {limit:>19.2f}")
print(f"Difference:    {difference:>19.2f}")
print(f"Percentage:    {percent:>18.2f}%")
print(f"Status:        {status:>19}")

print("=" * 34)


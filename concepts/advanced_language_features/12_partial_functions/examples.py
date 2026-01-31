# Partial Functions Examples

from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(4))  # 16
print(cube(4))    # 64

# With multiple args
def send_email(to, subject, body):
    print(f"Sending to {to}: {subject} - {body}")

send_to_boss = partial(send_email, "boss@example.com", "Report")
send_to_boss("Weekly update")  # Sending to boss@example.com: Report - Weekly update

# Sorting with partial
data = ["apple", "Banana", "cherry"]
sorted_data = sorted(data, key=partial(str.lower))
print(sorted_data)  # ['apple', 'Banana', 'cherry']
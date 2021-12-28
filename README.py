# Function_Writing
# Income Calculation Function Description: Pay is the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.
def computepay(h, r):
    if h <= 40:
        a = r*h
    else:
        a = r*40 + r*1.5*(h-40)
    return a

hrs = input("Enter Hours:")
rph = input("Enter Rate Per Hour:")
h = float(hrs)
r = float(rph)

p = computepay(h, r)
print("Pay", p)

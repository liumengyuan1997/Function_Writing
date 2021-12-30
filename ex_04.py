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

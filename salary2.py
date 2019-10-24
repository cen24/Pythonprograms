
#Compute Pay h*r. if Hours worked(h) greater than 40 then include OvertimePay
# the Hours worked over 40 and hourly pay is at rate 1.5% of regular hours pay.

def computepay(h, r):
    if h >= 40:
        pay = (40 * r) + (h - 40) * (r * 1.5)
    else:
        pay = (h * r)
    return pay

try:
    hrs = input("Enter Hours:")
    rte = input('Enter Rate:')
    h = float(hrs)
    r = float(rte)

except:
    print("Please enter number digit")
    exit()

pay = computepay(h, r)
print(pay)

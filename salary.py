
#Compute Pay H*R. if Hours worked(H) greater than 40 then include OvertimePay (Otp)
# Otp is the Hours worked over 40 and hourly pay is at rate 1.5% of regular hours pay.

hrs = input('Enter Hours:')
rte = input('Enter Rate:')
H = float(hrs)
R = float(rte)
Reg = H*R
Otp = (H-40)*(R*.5)

if H > 40:
    print(Reg + Otp)
else:
    print(Reg)
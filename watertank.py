h=10
r=5
F=10
t=int(input("enter the time "))

Vtank = 3.14*r**2*h

Vwater = F*t

if Vwater > Vtank:
    print("Over flow condition ")
    print("volume of ", Vwater-Vtank)
elif Vwater == Vtank:
    print("Tank full ")
else:
    print("Underflow condition ")
    ht = Vwater/(3.14*r**2)
    hr = h - ht
    print(f"filled height {ht}\nRemaining height {hr}")
        

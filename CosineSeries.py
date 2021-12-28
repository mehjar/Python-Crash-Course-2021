import math

angle = 60;
rad = math.pi/180*60;

actval = math.cos(rad)

# print(actval)

cosval = 0;

numterms = 3;

for ii in range(numterms):
    numerator = ((-1)**ii)*rad**(ii*2);
    denominator = SriFactorial((ii)*2);
    cosval += numerator/denominator;
    print(ii)

print(cosval)

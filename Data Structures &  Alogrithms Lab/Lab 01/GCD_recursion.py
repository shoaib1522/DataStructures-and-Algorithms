def calculateGCD(A, B):
    if B==0:
        return A 
    return calculateGCD(B, A%B)
examples = [[18, 12], [25, 15], [40, 60]]
for e in examples:
    A, B = e
    gcd = calculateGCD(A, B)
    print("GCD of", A, "and", B, "is:", gcd)
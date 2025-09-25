def przestaw(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if (n > 0):
        w = a + 10 * b + 100 * przestaw(n)
        print("invoke!")
    else:
        if (a > 0):
            w = a+10*b
        else:
            w = b
    return w


# ---- Test cases: ----
print(przestaw(316498))  # Expected output: 134689, number or invokes: 3
print(przestaw(43657688))  # Expedted output: 34566788, number or invokes: 4
print(przestaw(154005710))  # Expected output: 145007501, number of invokes: 5
# Expected output: 989786756453412, number of invokes: 8
print(przestaw(998877665544321))

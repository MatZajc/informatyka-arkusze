def przestaw2(n):
    multiplier = 1
    result = 0
    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100
        if (n > 0):
            result += (a + 10 * b) * multiplier
            multiplier *= 100
        else:
            if (a > 0):
                result += (a + 10 * b) * multiplier
            else:
                result += b * multiplier
    return result


# ---- Test cases: ----
print(przestaw2(316498))  # Expected output: 134689, number or invokes: 3
print(przestaw2(43657688))  # Expedted output: 34566788, number or invokes: 4
print(przestaw2(154005710))  # Expected output: 145007501, number of invokes: 5
# Expected output: 989786756453412, number of invokes: 8
print(przestaw2(998877665544321))

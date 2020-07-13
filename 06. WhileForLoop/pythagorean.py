
# for a in range(200, 300):
#     for b in range(200, 500):
#         for c in range(200, 500):
#             if (a**2) + (b**2) == c**2 and a + b +c == 1000:
#                 print(a * b * c)
#                 print(f"{a} {b} {c}")

for a in range(100, 1000):
    for b in range(100, 1000):
        c = 1000 - a - b
        if a * a +  b * b == c * c and a < b < c:
            print(a * b * c)
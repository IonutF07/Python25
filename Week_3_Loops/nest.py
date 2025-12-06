#program to explain nested loop
#outer loop
for i in range(1, 6):
    print(f"multiplication table {i}")
    #inner loop
    for j in range(1, 6):
        product = i * j
        print(f"{i} x {j} = {product}")

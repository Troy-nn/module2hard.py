def get_password(n):
    pairs = []
    # print (f"pairs = {pairs} n = {n}")
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                # print (f" {n} % ({i} + {j}) == 0")
                pairs.append(f"{i}{j}")
                # print (f"Добавляет пару чисел {i}{j} в список pairs.")
                # print (f"Список с добавленной парой чисел: \npairs = {pairs}")
    # print (f".join({pairs})")
    result = ''.join(pairs)
    # print (f"result = {result}")
    return result

n1 = 9

n2 = 11


result1 = get_password(n1)

result2 = get_password(n2)

print(f"{n1} - {result1}")
print(f"{n2} - {result2}")

for n in range(3, 21):
    print(f"{n} - {get_password(n)}")

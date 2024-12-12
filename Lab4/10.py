def hanoi(n, source, tar, aux):
    if n == 1:
        print(f"Przenos dysk 1 z {source} do {tar}")
        return
    else:
        hanoi(n - 1, source, aux, tar)
        print(f"Przenos dysk {n} z {source} do {tar}")
        hanoi(n - 1, aux, tar, source)

hanoi(3, "A", "B", "C")
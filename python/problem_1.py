def multiples(lst: list[int], *multipliers: int) -> list[int]:
    conditions = [lambda x, m=m: x % m == 0 for m in multipliers]
    return [x for x in lst if any(cond(x) for cond in conditions)]

print(sum(multiples(range(1000), 3, 5)))


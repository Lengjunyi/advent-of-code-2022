input = """Monkey 0:
  Starting items: 54, 61, 97, 63, 74
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 1:
  Starting items: 61, 70, 97, 64, 99, 83, 52, 87
  Operation: new = old + 8
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 6

Monkey 2:
  Starting items: 60, 67, 80, 65
  Operation: new = old * 13
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 3:
  Starting items: 61, 70, 76, 69, 82, 56
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 5
    If false: throw to monkey 2

Monkey 4:
  Starting items: 79, 98
  Operation: new = old + 2
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 3

Monkey 5:
  Starting items: 72, 79, 55
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 6:
  Starting items: 63
  Operation: new = old + 4
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 72, 51, 93, 63, 80, 86, 81
  Operation: new = old * old
  Test: divisible by 11
    If true: throw to monkey 0
    If false: throw to monkey 4"""

for isPart1 in [True, False]:
    monkeys = []
    ops = []
    params = []

    for index, m in enumerate(input.split("\n\n")):
        lines = m.split("\n")
        monkeys.append(list(map(int, lines[1].split(":")[1].split(","))))
        ops.append(lines[2].split("=")[1])
        params.append(list(map(int, [line.split()[-1] for line in lines[3:]])))

    # mod that handles overflow for part2
    mod = 1
    for (i,_,_) in params:
        mod *= i

    counts = [0] * len(monkeys)
    for iter in range(20 if isPart1 else 10000):
        for i, items in enumerate(monkeys):
            counts[i] += len(items)
            for old in items:
                new = eval(ops[i])
                if isPart1:
                    new //= 3
                else:
                    new %= mod
                (n, t, f) = params[i]
                if new % n == 0:
                    monkeys[t].append(new)
                else:
                    monkeys[f].append(new)
            monkeys[i] = []
    counts.sort()
    print(counts[-1] * counts[-2])
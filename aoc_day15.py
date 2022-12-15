input = """Sensor at x=155404, y=2736782: closest beacon is at x=2062250, y=2735130
Sensor at x=2209843, y=541855: closest beacon is at x=2159715, y=2000000
Sensor at x=3437506, y=3046523: closest beacon is at x=3174767, y=2783059
Sensor at x=925392, y=1508378: closest beacon is at x=941123, y=1223290
Sensor at x=2349988, y=3272812: closest beacon is at x=1912017, y=3034331
Sensor at x=292610, y=374034: closest beacon is at x=941123, y=1223290
Sensor at x=2801735, y=1324309: closest beacon is at x=2159715, y=2000000
Sensor at x=3469799, y=2027984: closest beacon is at x=3174767, y=2783059
Sensor at x=3292782, y=2910639: closest beacon is at x=3174767, y=2783059
Sensor at x=3925315, y=2646100: closest beacon is at x=3174767, y=2783059
Sensor at x=1883646, y=2054943: closest beacon is at x=2159715, y=2000000
Sensor at x=2920303, y=3059306: closest beacon is at x=3073257, y=3410773
Sensor at x=2401153, y=2470599: closest beacon is at x=2062250, y=2735130
Sensor at x=2840982, y=3631975: closest beacon is at x=3073257, y=3410773
Sensor at x=1147584, y=3725625: closest beacon is at x=1912017, y=3034331
Sensor at x=2094987, y=2782172: closest beacon is at x=2062250, y=2735130
Sensor at x=3973421, y=982794: closest beacon is at x=3751293, y=-171037
Sensor at x=2855728, y=2514334: closest beacon is at x=3174767, y=2783059
Sensor at x=1950500, y=2862580: closest beacon is at x=1912017, y=3034331
Sensor at x=3233071, y=2843812: closest beacon is at x=3174767, y=2783059
Sensor at x=2572577, y=3883463: closest beacon is at x=3073257, y=3410773
Sensor at x=3791570, y=3910685: closest beacon is at x=3073257, y=3410773
Sensor at x=3509554, y=311635: closest beacon is at x=3751293, y=-171037
Sensor at x=1692070, y=2260914: closest beacon is at x=2159715, y=2000000
Sensor at x=1265756, y=1739058: closest beacon is at x=941123, y=1223290"""

import re
input_t = [list(map(int, re.findall(r"-?\d+", sensor))) for sensor in input.split("\n")]

s = set()
b = set()
N = 2000000

for (xs, ys, xb, yb) in input_t:
    dis = abs(xs - xb) + abs(ys - yb)
    dis -= abs(ys - N)
    if yb == N:
        b.add(xb)
    s.update(range(xs - dis, xs + dis + 1))

print(len(s.difference(b)))

# this solution only works for the given dataset.

intervals_x_plus_y = []
intervals_x_minus_y = []

for (xs, ys, xb, yb) in input_t:
    dis = abs(xs - xb) + abs(ys - yb)
    intervals_x_plus_y.append((xs + ys - dis, xs + ys + dis))
    intervals_x_minus_y.append((xs - ys - dis, xs - ys + dis))

for _, a in intervals_x_plus_y:
    for b, _ in intervals_x_plus_y:
        if a + 1 == b - 1:
            x_plus_y = a + 1

for _, a in intervals_x_minus_y:
    for b, _ in intervals_x_minus_y:
        if a + 1 == b - 1:
            x_minus_y = a + 1

x = (x_plus_y + x_minus_y) // 2
y = (x_plus_y - x_minus_y) // 2
print(2 * N * x + y)
color = ("red", "green", "blue", "yellow", "orange")

(a, b, c, d, e) = color

print(f"a: {a} b: {b} c: {c} d: {d} e: {e}")

(f, g, *h) = color
print(f"f: {f} g: {g} h: {h}")

(i, *j, k) = color
print(f"i: {i} j: {j} k: {k}")

(*l, m, n) = color
print(f"l: {l} m: {m} n: {n}")
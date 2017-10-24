courses = {
    'BGN': 1,
    'USD': 1.79549,
    'EUR': 1.95583,
    'GBP': 2.53405
}

amount = float(input())
initial = input().upper()
to = input().upper()

rate_in = 1 / courses.get(initial)
in_to_bgn = amount / rate_in
rate_out = 1 / courses.get(to)
out = in_to_bgn * rate_out

print("{:.2f} {}".format(out, to))

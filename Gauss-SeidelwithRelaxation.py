x1 = lambda x2: (8 + (2 * x2)) / 10
x2 = lambda x1: (9 + (3 * x1)) / 12
error = lambda n, o: abs((n - o) / n) * 100

ax1, ax2 = 0, 0

itemax = 5
relaxation_factor = 1.2

table = '{0:1} | {1:7} | {2:7} | {3:7} | {4:7}'
print(table.format("i", "x1", "x2", "E1", "E2"))
for i in range(itemax):
    if i == 0:
        print(table.format(i, ax1, ax2, "-", "-"))
        cx1 = ax1
        cx2 = ax2
    else:
        cx1 = ax1 + relaxation_factor * (x1(cx2) - ax1)
        cx2 = ax2 + relaxation_factor * (x2(cx1) - ax2)
        print(
            table.format(
                i,
                cx1,
                cx2,
                "{0:.2f}".format(error(cx1, ax1)),
                "{0:.2f}".format(error(cx2, ax2)),
            )
        )

    ax1 = cx1
    ax2 = cx2

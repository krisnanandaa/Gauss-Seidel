x1 = lambda x2, x3: (7.85 + (0.1 * x2) + (0.2 * x3)) / 3
x2 = lambda x1, x3: (-19.3 - (0.1 * x1) + (0.3 * x3)) / 7
x3 = lambda x1, x2: (71.4 - (0.3 * x1) + (0.2 * x2)) / 10
error = lambda n, o: abs((n - o) / n) * 100

ax1, ax2, ax3 = 0, 0, 0

itemax = 5

table = '{0:1} | {1:7} | {2:7} | {3:7} | {4:7} | {5:7} | {6:7}'
print(table.format("i", "x1", "x2", "x3", "E1", "E2", "E3"))
for i in range(itemax):
    if i == 0:
        print(table.format(i, ax1, ax2, ax3, "-", "-", "-"))
        cx1 = ax1
        cx2 = ax2
        cx3 = ax3
    else:
        cx1 = round(x1(ax2, ax3), 3)
        cx2 = round(x2(cx1, ax3), 3)
        cx3 = round(x3(cx1, cx2), 3)
        print(
            table.format(
                i,
                cx1,
                cx2,
                cx3,
                "{0:.2f}".format(error(cx1, ax1)),
                "{0:.2f}".format(error(cx2, ax2)),
                "{0:.2f}".format(error(cx3, ax3)),
            )
        )

    ax1 = cx1
    ax2 = cx2
    ax3 = cx3

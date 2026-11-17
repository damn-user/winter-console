import math, os, sys, time

if os.name == "nt":
    os.system("")

sys.stdout.write("\033[2J\033[?25l")

c_w = 20
c_h = 10

step = 360
radius = 7

ring_angle = 0

buff = "@#%*+."
buff_cr = [
    (2.5, buff[0]),
    (1.5, buff[1]),
    (0.5, buff[2]),
    (-0.5, buff[3]),
    (-1.5, buff[4]),
    (-10, buff[5]),
]


def draw(ring_angle):
    z_buf = [[-999 for x in range(40)] for y in range(20)]
    canvas = [[" " for x in range(40)] for y in range(20)]

    for st in range(step):
        angle = math.radians(st)

        for t in range(3):
            x = int(
                round(c_w + radius * math.cos(angle) * 2 * math.cos(ring_angle)) + t - 1
            )
            y = int(round(c_h + radius * math.sin(angle)))

            z = radius * math.cos(angle) * math.sin(ring_angle)

            for cr, gr in buff_cr:
                if z > cr and z >= z_buf[y][x]:
                    canvas[y][x] = "\033[38;5;214m" + gr + "\033[0m"
                    z_buf[y][x] = z
                    break

    frame = "\n".join("".join(row) for row in canvas)
    sys.stdout.write("\033[H" + frame)
    sys.stdout.flush()


try:
    while True:
        draw(ring_angle)
        ring_angle += 0.05
        time.sleep(0.05)

except KeyboardInterrupt:
    sys.stdout.write("\033[?25h\n")

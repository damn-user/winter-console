import os, sys, math, time, random

if os.name == "nt":
    os.system("")

sys.stdout.write("\033[2J\033[?25l")

cen_w = 30
cen_h = 10

buff_cr = [
    (7.2, "M", 154),
    (6.2, "B", 118),
    (5.2, "@", 82),
    (4.2, "#", 46),
    (3.3, "$", 40),
    (2.4, "&", 34),
    (1.6, "%", 34),
    (0.9, "*", 28),
    (0.2, "+", 28),
    (-0.5, "=", 22),
    (-1.3, ":", 22),
    (-2.3, "-", 235),
    (-3.8, ".", 234),
    (-99, "·", 233),
]


step = 360


def draw_tree(stp):
    canvas = [[" " for x in range(60)] for y in range(31)]
    z_buf = [[-999 for x in range(60)] for y in range(31)]

    height = 15

    height_base = 3
    radius = 3

    for i_st in range(height_base * 2):
        i = i_st * 0.5
        for st in range(step):
            angle = math.radians(st)

            x = int(round(cen_w + radius * math.cos(angle)))
            y = int(math.floor(cen_h + height + radius * 0.25 * math.sin(angle) + i))

            z = radius * math.sin(angle)

            for cr, gr, color in buff_cr:
                if z > cr and z > z_buf[y][x]:
                    canvas[y][x] = f"\033[38;5;130m" + gr + "\033[0m"
                    z_buf[y][x] = z
                    break

    for i_st in range(height * 2):
        i = i_st * 0.5
        for st in range(step):
            angle = math.radians(st)
            radius = (i * 0.7) * (1 + 0.2 * math.sin(angle * 5))
            rot_angle = angle + stp

            x = int(round(cen_w + radius * math.cos(rot_angle)))
            y = int(math.floor(cen_h + radius * 0.25 * math.sin(rot_angle) + i))

            z = radius * math.sin(rot_angle)

            if (st + (i * 45)) % 180 < 35 and z > z_buf[y][x]:
                clr_l = [196, 214, 27]
                clr = random.choice(clr_l)
                canvas[y][x] = f"\033[38;5;{clr}m●\033[0m"
                z_buf[y][x] = z
                continue

            for cr, gr, color in buff_cr:
                if z > cr and z > z_buf[y][x]:
                    canvas[y][x] = f"\033[38;5;{color}m" + gr + "\033[0m"
                    z_buf[y][x] = z
                    break

    star_rad = 2
    for st in range(int(step / 72)):
        angle = math.radians(st * 72 - 90)

        for r in range(star_rad):
            x = int(round(cen_w + r * math.cos(angle) * 2 * math.cos(stp)))
            y = int(round(cen_h - 2 + r * math.sin(angle)))

            z = star_rad * math.sin(rot_angle) * math.cos(angle)

            if z > -0.5:
                canvas[y][x] = f"\033[38;5;226m*\033[0m"
            else:
                if canvas[y][x] == " ":
                    canvas[y][x] = f"\033[38;5;226m.\033[0m"

    return canvas


snow_canvas = [[" " for x in range(60)] for y in range(31)]


def snow_generate():
    r_pos = random.randint(0, 59)
    snow_canvas[0][r_pos] = "*"


def snow_fall():
    for y in range(31 - 1, -1, -1):
        for x in range(len(snow_canvas[y])):
            if snow_canvas[y][x] == "*" and y + 1 < 31:
                snow_canvas[y + 1][x] = "*"
                snow_canvas[y][x] = " "

            elif snow_canvas[y][x] == "*" and y + 1 >= 31:
                snow_canvas[y][x] = " "


def clip(s_c, c):
    snow_fall()
    snow_generate()

    canvas = [[" " for x in range(60)] for y in range(31)]
    for y in range(31):
        for x in range(60):
            canvas[y][x] = s_c[y][x]
            if c[y][x] != " ":
                canvas[y][x] = c[y][x]

    frame = "\n".join("".join(row) for row in canvas)
    sys.stdout.write("\033[H" + frame)
    sys.stdout.flush()


stp = 0

try:
    while True:
        clip(snow_canvas, draw_tree(stp))
        stp += 0.05
        time.sleep(0.05)

except KeyboardInterrupt:
    sys.stdout.write("\033[?25h\n")

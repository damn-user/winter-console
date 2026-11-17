import math, random, os, sys, time

if os.name == "nt":
    os.system("")

sys.stdout.write("\033[2J\033[?25l")

width = 60
height = 40

canvas = [[" " for x in range(width)] for y in range(height)]


def snow_generate():
    r_pos = random.randint(0, width - 1)
    canvas[0][r_pos] = "*"


def snow_fall():
    for y in range(height - 1, -1, -1):
        for x in range(len(canvas[y])):
            if canvas[y][x] == "*" and y + 1 < height:
                canvas[y + 1][x] = "*"
                canvas[y][x] = " "

            elif canvas[y][x] == "*" and y + 1 >= height:
                canvas[y][x] = " "


try:
    while True:
        for _ in range(random.randint(1, 3)):
            snow_generate()
        time.sleep(0.1)
        snow_fall()

        frame = "\n".join("".join(row) for row in canvas)
        sys.stdout.write("\033[H" + frame)
        sys.stdout.flush()

except KeyboardInterrupt:
    sys.stdout.write("\033[?25h\n")

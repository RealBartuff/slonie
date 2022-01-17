# ASCII by Barłomiej Dębowski

lines = ([
    "  Create a frame!      ",
    "           __     __   ",
    "          /  \~~~/  \  ",
    "    ,----(     ..    ) ",
    "   /      \__     __/  ",
    "  /|         (\  |(    ",
    " ^  \  /___\  /\ |     ",
    "    |__|   |__|-..     ",
])


def strip_one_space(s):
    if s.endswith(" "):
        s = s[:-1]
    if s.startswith(" "):
        s = s[1:]
    return s


def print_dumbo(start, end):
    print(start.strip() * 25)
    for row in lines:
        print("*", strip_one_space(row), "*")
    print(end.strip() * 25)


print_dumbo("*", "*")

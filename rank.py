import sys


# given two sorted lists, return a new list of all sorted elements
def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if not compare(a[i], b[j]):
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1
    return c


def mergesort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    if len(arr) == 2:
        if compare(arr[0], arr[1]):
            return [arr[1], arr[0]]
        else:
            return arr
    mid = len(arr) // 2
    a = mergesort(arr[:mid])
    b = mergesort(arr[mid:])
    return merge(a, b)


# true if a >= b, false otherwise
def compare(a, b):
    answer = '0'
    while answer not in ['1', '2']:
        print(f"Which is 'greater'? \n (1) - '{a}' \t or \n (2) - '{b}'", file=sys.stderr)
        answer = read_char()

    return answer == '2'


# cross-platform reads a single character in raw mode
def read_char():
    # try the Windows method, fall back to Unix
    try:
        import msvcrt
        ch = msvcrt.getch()
    except ImportError:
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ord(ch) == 3:
        print("Ctrl+C detected, aborting")
        exit(0)
    return ch


# if this is being executed from the command line
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} INPUT_FILE", file=sys.stderr)
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    sorted_items = mergesort(lines)
    for item in sorted_items:
        print(item)

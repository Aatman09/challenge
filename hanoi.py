import time
import os

disks = 5
delay = 0.4

pegs = {
    'A': list(range(disks, 0, -1)),
    'B': [],
    'C': []
}

moves = 0


def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n  Tower of Hanoi   move: {moves}\n")

    for row in range(disks, 0, -1):
        line = ""
        for peg in ['A', 'B', 'C']:
            stack = pegs[peg]
            if len(stack) >= row:
                d = stack[row - 1]
                bar = "=" * d
                line += f"  {bar}|{bar}".center(20)
            else:
                line += "|".center(20)
        print(line)

    print("  " + "-"*18 + "  " + "-"*18 + "  " + "-"*18)
    print("  " + "A".center(18) + "  " + "B".center(18) + "  " + "C".center(18))


# basically move everything above the biggest disk out of the way first,
# then shift the big disk across, then stack everything back on top of it
# it just keeps calling itself with one less disk each time until theres nothing left to move
def move(n, src, dst, aux):
    global moves

    if n == 0:
        return

    move(n-1, src, aux, dst)

    pegs[dst].append(pegs[src].pop())
    moves += 1
    draw()
    time.sleep(delay)

    move(n-1, aux, dst, src)


draw()
time.sleep(0.8)
move(disks, 'A', 'C', 'B')
print(f"\n  done in {moves} moves\n")
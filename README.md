# Tower of Hanoi

small python script i wrote to visualise the tower of hanoi puzzle. it animates the disks moving between the three pegs step by step.

## how to run

```
python hanoi.py
```

you'll need python 3 installed, thats it.

## changing it

at the top of the file there's two variables you can tweak:

- `disks` — how many disks, 5 is default. dont go too high it gets slow fast
- `delay` — seconds between each move, set to 0 if you just want it to finish instantly

## how it works

it uses recursion — the move function just keeps calling itself with one less disk until theres nothing left to move. not much to it really, the whole logic is like 10 lines.
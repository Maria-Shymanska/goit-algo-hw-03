def move_disk(source, target, disks, intermediate, steps):
    if disks == 1:
        target.append(source.pop())
        steps.append(f"Перемістити диск з {source.name} на {target.name}: {target[-1]}")
    else:
        move_disk(source, intermediate, disks - 1, target, steps)
        move_disk(source, target, 1, intermediate, steps)
        move_disk(intermediate, target, disks - 1, source, steps)

class Peg(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

def hanoi(n, pegs):
    for disk in range(n, 0, -1):
        pegs[0].append(disk)
    
    steps = []
    move_disk(pegs[0], pegs[2], n, pegs[1], steps)

    return steps, pegs

def main():
    n = int(input("Введіть кількість дисків: "))
    pegs = [Peg('A'), Peg('B'), Peg('C')]
    steps, pegs = hanoi(n, pegs)
    print("Початковий стан:", {peg.name: list(peg) for peg in pegs})
    for i, step in enumerate(steps):
        print(f"Проміжний стан ({i+1}):", {peg.name: list(peg) for peg in pegs})
        print(step)
    print("Кінцевий стан:", {peg.name: list(peg) for peg in pegs})

if __name__ == "__main__":
    main()


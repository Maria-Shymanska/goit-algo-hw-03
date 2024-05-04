
def visualize(pegs):
    max_height = max(len(peg) for peg in pegs)
    for level in range(max_height - 1, -1, -1):
        for peg in pegs:
            if level < len(peg):
                disk_size = peg[level]
                print(f"{'=' * disk_size:<3}", end="")
            else:
                print(" | ", end="")
        print()

def move_disk(source, target, source_name, target_name, steps):
    disk = source[-1]
    source.pop()
    target.append(disk)
    steps.append(f"Перемістити диск з {source_name} на {target_name}: {disk}")

def hanoi(n, source, target, intermediate, source_name, target_name, intermediate_name, steps):
    if n == 1:
        move_disk(source, target, source_name, target_name, steps)
    else:
        hanoi(n - 1, source, intermediate, target, source_name, intermediate_name, target_name, steps)
        move_disk(source, target, source_name, target_name, steps)
        hanoi(n - 1, intermediate, target, source, intermediate_name, target_name, source_name, steps)

def main():
    n = int(input("Введіть кількість дисків: "))
    source = list(range(n, 0, -1))
    target = []
    intermediate = []
    steps = []
    hanoi(n, source, target, intermediate, 'A', 'C', 'B', steps)
    print("Початковий стан:")
    visualize([source, intermediate, target])
    for i, step in enumerate(steps):
        print(f"Проміжний стан ({i+1}):")
        visualize([source, intermediate, target])
        print(step)
        if i < len(steps) - 1:
            print()
    print("Кінцевий стан:")
    visualize([source, intermediate, target])

if __name__ == "__main__":
    main()




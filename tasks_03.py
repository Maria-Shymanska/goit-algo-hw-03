
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
    print("Початковий стан:", {'A': source, 'B': intermediate, 'C': target})
    for i, step in enumerate(steps):
        print(f"Проміжний стан ({i+1}):", {'A': source, 'B': intermediate, 'C': target})
        print(step)
    print("Кінцевий стан:", {'A': source, 'B': intermediate, 'C': target})

if __name__ == "__main__":
    main()

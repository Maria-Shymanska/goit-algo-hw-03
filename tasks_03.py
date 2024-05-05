def move_disk(start, end, disk):
    print(f"Перемістити диск з {start} на {end}: {disk}")

def hanoi(n, start, end, middle):
    if n == 1:
        move_disk(start, end, start[-1])
    else:
        hanoi(n - 1, start, middle, end)
        move_disk(start, end, start[-1])
        hanoi(n - 1, middle, end, start)

def main():
    n = int(input("Введіть кількість дисків: "))
    start = 'A'
    end = 'C'
    middle = 'B'
    
    initial_state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {initial_state}")

    hanoi(n, start, end, middle)

    final_state = {'A': [], 'B': [], 'C': list(range(n, 0, -1))}
    print(f"Кінцевий стан: {final_state}")

if __name__ == "__main__":
    main()









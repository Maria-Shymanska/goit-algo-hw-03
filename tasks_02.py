import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Запитуємо користувача про рівень рекурсії
    order = int(input("Введіть рівень рекурсії (ціле число): "))

    # Створюємо вікно та екземпляр черепашки
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Сніжинка Коха")

    tess = turtle.Turtle()
    tess.speed(0)
    tess.color("blue")

    # Переміщення черепашки до початкової позиції
    tess.penup()
    tess.goto(-150, 90)
    tess.pendown()

    # Викликаємо функцію для малювання сніжинки Коха
    for _ in range(3):
        koch_snowflake(tess, order, 300)
        tess.right(120)

    # Закриваємо вікно при натисканні клавіші "Enter"
    wn.mainloop()

if __name__ == "__main__":
    main()

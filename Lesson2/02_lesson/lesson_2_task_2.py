def is_year_leap(год):
    if (год % 4 == 0):
        print(f"год: {год} - True")
    else:
        print(f"год: {год} - False")


is_year_leap(int(input("Введите год: ")))

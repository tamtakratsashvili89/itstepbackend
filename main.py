def calculator():
    # 1) პირველი რიცხვის შეყვანა და ვალიდაცია
    try:
        num1 = float(input("გთხოვთ, შეიყვანოთ პირველი რიცხვი: "))
    except ValueError:
        print("გაითვალისწინეთ: შესაძლებელია მხოლოდ რიცხვის შეყვანა!")
        return  # პროგრამა ამთავრებს მუშაობას


   # 3) ოპერატორის შეყვანა
    operation = input("აირჩიე ოპერაცია (+, -, *, /): ")


    # 2) მეორე რიცხვის შეყვანა და ვალიდაცია
    try:
        num2 = float(input("გთხოვთ, შეიყვანოთ მეორე რიცხვი: "))
    except ValueError:
        print("გაითვალისწინეთ: შესაძლებელია მხოლოდ რიცხვის შეყვანა!")
        return


    # 4) ოპერაციის შესრულება
    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        # დამატებითი ვალიდაცია: ნულზე გაყოფა აკრძალულია
        if num2 == 0:
            print("შეცდომა: გაითვალისწინეთ, რომ ნულზე გაყოფა შეუძლებელია!")
            return
        result = num1 / num2

    else:
        print("შეცდომა: მიუთითე სწორი ოპერაცია!")
        return

    # 5) შედეგის ჩვენება
    print(f"შედეგი არის: {result}")


# ვიძახებთ ფუნქციას
calculator()

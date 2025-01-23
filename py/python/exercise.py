
connection = True

while connection:
    email = input("Enter your email address: ")
    
    if email.count('@') == 1 and email.count('.') >= 1:
        print("Your email has been successfully recorded!")
        break

    else:
        print("The entered address is invalid. Please try again..")



"""
метод count считает колл во вхождений символа в строку 
в первом случае count проверяет, что символ ( @ ) встречается ровно 1 раз
во втором случае count проверяет, что символ ( . ) встречается хотя бы один раз

break нужен для выхода из цикла после сообщения о том что мы умнички и мы справились

так же можно было сделать через условный оператор if , но как по мне используя метод count
мы значительно повысим надежность проверки входных данных :)

"""
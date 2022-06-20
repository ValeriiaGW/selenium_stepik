# assert abs(-42) == 42 #проверяет число по модулю, в случае true ничего не выводит
#
# assert abs(-42) == -42, "Should be absolute value of a number" # проверяет число по модудю, в случае false выведет ошибку с указанным описанием


# python умеет подставлять пользовательские значения в строки с помощью функции .format().

# Синтаксис выглядит примерно так:

# "Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")

print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

# наиболее современный способ форматирования строк, который появился в Python3.6, носит название f-strings.
# Он позволяет исполнять выражения на Python прямо внутри строк, обладает еще большей лаконичностью и удобством использования.
# Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: f"ваша строка {my_var}".
# В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат
# исполнения которого также требуется подставить в вашу строку.

# Example 1
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

# Example 2
actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

# Example 3
print(f"{2+3}")



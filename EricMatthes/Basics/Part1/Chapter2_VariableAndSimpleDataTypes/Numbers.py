"""INTEGERS"""

a = 2 + 3
b = 3 - 2
v = 2 * 3
f = 2 / 3
h = 2 % 3

p = 3 ** 2
P = 3 ** 3
PP = 10 ** 6

"""FLOATS"""

A = 0.1 + 0.1
B = 0.2 + 0.2
C = 2 * 0.1
D = 2 * 0.2

AA = 0.2 + 0.1  # 0.30000000000000004
DD = 3 * 0.1  # 0.30000000000000004

"""Avoliding ytpe errors with the str() Function"""

# age = 23
# message = "happy " + age + "rd Birthday!"
#
# print(message)  # Hato, chunki "son bilan matnni qoshib bolmaydi!

age = 23
message = "happy " + str(age) + "rd Birthday!"

print(message.title())

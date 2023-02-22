import re
from itertools import permutations


def solution(expression):
    answer = []
    # 1 정규표현식을 이용하여 입력을 연산자로 구분하여 나눈다.
    expression = re.split("([-+*])", expression)  # 연산자가 아닌것으로 구분함
    operators = list(permutations(["+", "-", "*"]))  # 6가지 경우 연산자 열을 반환함

    for operator in operators:  # 6가지의 경우 연산을 반복
        exp = expression[:]
        for op in operator:
            while op in exp:
                idx = exp.index(op)
                exp[idx - 1] = str(eval(exp[idx - 1] + op + exp[idx + 1]))
                del exp[idx : idx + 2]
        answer.append(abs(int(exp[0])))

    return max(answer)

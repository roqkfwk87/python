class Calculator:

    def input_expr(self):
        expr = input("수식을 입력하세요 >>> ")
        self.expr = expr

    def calculate(self):
        return eval(self.expr)

calc = Calculator()

calc.input_expr()
# print(calc.expr)
print(f'수식 결과는 {calc.calculate()}입니다.')
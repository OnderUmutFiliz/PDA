class PDAMathExpressionValidator:
    def __init__(self):
        self.stack = []

    def is_operator(self, char):
        return char in '+-*/'

    def is_digit(self, char):
        return char.isdigit()

    def is_balanced_parentheses(self, expression):
        for char in expression:
            if char == '(':
                self.stack.append(char)
            elif char == ')':
                if not self.stack or self.stack[-1] != '(':
                    return False
                self.stack.pop()
        return not self.stack

    def is_valid_expression(self, expression):
        # Parantezlerin dengeli olup olmadığını kontrol etme
        if not self.is_balanced_parentheses(expression):
            return False
        
        i = 0
        while i < len(expression):
            char = expression[i]

            if char == '(':
                # '(' den sonraki karakterin geçerli olup olmadığını kontrol et
                if i + 1 < len(expression) and (self.is_operator(expression[i + 1]) or expression[i + 1] == ')'):
                    return False
            elif char == ')':
                # ')' den önceki karakterin geçerli olup olmadığını kontrol et
                if i - 1 >= 0 and self.is_operator(expression[i - 1]):
                    return False
            elif self.is_operator(char):
                # Geçersiz operatör yerleşimini kontrol et
                if i == 0 or i == len(expression) - 1:  # Operator at the start or end
                    return False
                if i - 1 >= 0 and not (self.is_digit(expression[i - 1]) or expression[i - 1] == ')'):
                    return False
                if i + 1 < len(expression) and not (self.is_digit(expression[i + 1]) or expression[i + 1] == '('):
                    return False
                # Sıfıra bölmeyi kontrol et
                if char == '/' and i + 1 < len(expression) and expression[i + 1] == '0':
                    return False
            elif not self.is_digit(char):
                # Geçersiz karakter
                return False

            i += 1

        return True

def validate_expression(expression):
    pda = PDAMathExpressionValidator()
    return pda.is_valid_expression(expression)

# Kullanıcıdan ifade al
expression = input("Lütfen matematiksel ifadeyi girin: ")
if validate_expression(expression):
    print(f"İfade '{expression}' geçerlidir.")
else:
    print(f"İfade '{expression}' geçersizdir.")


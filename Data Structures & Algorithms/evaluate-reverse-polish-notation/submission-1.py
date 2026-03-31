class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b, a = stack.pop(), stack.pop()
                match t:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(t))
        
        while len(stack) > 1:
            t, b, a = stack.pop(), stack.pop(), stack.pop()
            match t:
                case "+":
                    stack.append(a + b)
                case "-":
                    stack.append(a - b)
                case "*":
                    stack.append(a * b)
                case "/":
                    stack.append(a // b)
        
        return stack.pop()
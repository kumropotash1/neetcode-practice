class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            for c in s:
                match c:
                    case '\\':
                        res += "\\\\"
                    case ",":
                        res += "\\,"
                    case _:
                        res += c
            res += ","
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        word, acc = "", ""
        for c in s:
            match c:
                case "\\":
                    if acc == "\\":
                        word += "\\"
                        acc = ""
                    else:
                        acc = "\\"
                case ",":
                    if acc == "\\":
                        word += ","
                        acc = ""
                    else:
                        res.append(word)
                        word = ""
                case _:
                    word += c
        if word:
            res.append(word)
        
        return res
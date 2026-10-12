class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        i = 0
        n = len(expression)

        def parse():
            nonlocal i

            union = set()
            current = {""}

            while i < n and expression[i] != "}":

                if expression[i] == ",":
                    union |= current
                    current = {""}
                    i += 1

                elif expression[i] == "{":
                    i += 1
                    choices = parse()
                    i += 1

                    current = {
                        a + b
                        for a in current
                        for b in choices
                    }

                else:
                    current = {
                        a + expression[i]
                        for a in current
                    }
                    i += 1

            return union | current

        return sorted(parse())

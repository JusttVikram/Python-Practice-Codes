#Leetcode 592.
class Solution:
    def fractionAddition(self,expression: str) -> str:
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        def add(a, b):
            lcm_ab = lcm(a[1], b[1])
            return [a[0] * (lcm_ab // a[1]) + b[0] * (lcm_ab // b[1]), lcm_ab]

        def simplify(frac):
            if frac[0] == 0:
                return [0, 1]
            gcd_ab = gcd(frac[0], frac[1])
            return [frac[0] // gcd_ab, frac[1] // gcd_ab]

        def parse(expression):
            res = []
            num = ""
            for i, c in enumerate(expression):
                if c in "+-":
                    if num:
                        res.append([int(num), 1])
                        num = ""
                    if c == "+":
                        res.append([1, 1])
                    else:
                        res.append([-1, 1])
                else:
                    num += c
            res.append([int(num), 1])
            return res

        frac_list = parse(expression)
        res = [0, 1]
        for frac in frac_list:
            res = add(res, frac)
        res = simplify(res)
        return str(res[0]) + "/" + str(res[1])
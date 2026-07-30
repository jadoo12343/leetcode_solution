class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int, b_int = int(a, 2), int(b, 2)
        while b_int != 0:
            carry = a_int & b_int
            a_int = a_int ^ b_int
            b_int = carry << 1
        return bin(a_int)[2:]


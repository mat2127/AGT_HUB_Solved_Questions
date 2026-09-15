class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
        for i in range(len(s)):
           if i + 1 < len(s) and (
                (s[i] == "I" and s[i + 1] in "VX") or
                (s[i] == "X" and s[i + 1] in "LC") or
                (s[i] == "C" and s[i + 1] in "DM")
):
                num -= roman_values[s[i]]
           else:
                num += roman_values[s[i]]
        return num      

        
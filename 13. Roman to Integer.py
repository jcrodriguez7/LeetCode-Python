class solution(object):
    def romanToInt(self, s: str) -> int:
            solution = 0


            if "IV" in s: 
                solution += 4
                s = s.replace("IV"," ")
            if "IX" in s: 
                solution += 9
                s = s.replace("IX","")
            if "XL" in s:
                solution += 40
                s = s.replace("XL","")
            if "XC" in s:
                solution += 90
                s = s.replace("XC","")
            if "CD" in s:
                solution += 400
                s = s.replace("CD","")
            if "CM" in s:
                solution += 900
                s = s.replace("CM","")
                

            for i in s:
                if i == "I": solution += 1
                elif i == "V": solution += 5
                elif i == "X": solution += 10
                elif i == "L": solution += 50
                elif i == "C": solution += 100
                elif i == "D": solution += 500
                elif i == "M": solution += 1000


            return solution
    
    def romanToInt2(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
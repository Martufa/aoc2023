from typing import List, Dict

def trebuchet():
    with open("blabla.txt", "r") as wrong_comb:
        total = 0
        translate_numbers: Dict[str:int] = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
        for line in wrong_comb:
            first: List[str] = []
            last: List[str] = []
            line_r = [] #line reconstruct
            for letter in line:
                if not letter.isdecimal():
                    line_r.append(letter)
                    
                    if len(line_r) > 2 and "".join(line_r[-3] + line_r[-2] + line_r[-1]) in translate_numbers:
                        letter = translate_numbers["".join(line_r[-3] + line_r[-2] + line_r[-1])]
                    
                    if len(line_r) > 3 and "".join(line_r[-4] + line_r[-3] + line_r[-2] + line_r[-1]) in translate_numbers:
                        letter = translate_numbers["".join(line_r[-4] + line_r[-3] + line_r[-2] + line_r[-1])]
                    
                    if len(line_r) > 4 and "".join(line_r[-5] + line_r[-4] + line_r[-3] + line_r[-2] + line_r[-1]) in translate_numbers:
                        letter = translate_numbers["".join(line_r[-5] + line_r[-4] + line_r[-3] + line_r[-2] + line_r[-1])]

                if not letter.isdecimal():
                    continue
                
                if len(first) == 0:
                    first = [letter]
                    continue
                
                last = [letter]
                
            if len(last) == 0:
                if len(first) == 0:
                    continue
                total += int("".join(first + first))
                continue
            
            total += int("".join(first + last))
        print(str(total))
        return

trebuchet()
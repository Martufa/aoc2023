from typing import List, Tuple, Dict

def schematics() -> None:
    rotations = [-1, 0, 1]
    sum_used = 0
    
    with open("blabla.txt", "r", encoding = "utf-8") as schematic:
        special_xy: List[Tuple[int, int]] = []
        num_all_coors: Dict[Tuple[int, int], str] = {} # (X, Y), číslo pod nima schované jako str
        
        for y, line in enumerate(schematic):
            line_wo_end = line[:-1]
            for x, character in enumerate(line_wo_end):
                if character.isdecimal():
                    num_all_coors[(x,y)] = character
                    continue
                
                if character != ".":
                    special_xy.append((x, y))

        
    for (spec_x, spec_y) in special_xy:
        for change_y in rotations:
            new_y = spec_y + change_y
            for change_x in rotations:
                new_x = spec_x + change_x
                
                # pokud nalezneš na okolních souřadnicích číslo
                # dostaň se na jeho začátek
                
                if num_all_coors.get((new_x, new_y)) is not None:
                    step = 0
                    temp_dict_num: List[str] = []
                    
                    while num_all_coors.get((new_x + step, new_y)) is not None:
                        step -= 1
                    step += 1 # přešlápli jsme to, tady už číslo není, fixin it
                    
                    # teď šlapej dopředu, zapisuj si, cos měl jako čísla a rovnou maž dict
                    while num_all_coors.get((new_x + step, new_y)) is not None:
                        temp_dict_num.append(num_all_coors.get((new_x + step, new_y), ""))
                        del num_all_coors[(new_x + step, new_y)]
                        step += 1
                    
                    if len(temp_dict_num) != 0:
                        sum_used += int("".join(temp_dict_num))
                        temp_dict_num = []
    
    print(sum_used)
    return

schematics()

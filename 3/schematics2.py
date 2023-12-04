from typing import List, Tuple, Dict

def schematics() -> None:
    rotations = [-1, 0, 1]
    sum_used = 0
    
    with open("blabla.txt", "r", encoding = "utf-8") as schematic:
        # special_xy: List[Tuple[int, int]] = []
        num_all_coors: Dict[Tuple[int, int], str] = {} # (X, Y), číslo pod nima schované jako str
        possible_gear_xy: List[Tuple[int, int]] = []
        
        for y, line in enumerate(schematic):
            line_wo_end = line[:-1]
            for x, character in enumerate(line_wo_end):
                if character.isdecimal():
                    num_all_coors[(x,y)] = character
                    continue
                
                if character == "*":
                    possible_gear_xy.append((x, y))

    #první zkontroluj, jestli je to gear... jestli ne, přejdi na další kolo
    for (spec_x, spec_y) in possible_gear_xy:
        gear_nums_to_mult: List[int] = []
        for change_y in rotations:
            new_y = spec_y + change_y
            for change_x in rotations:
                new_x = spec_x + change_x
                if num_all_coors.get((new_x, new_y)) is not None:
                    #adjacent += 1
                    step = 0
                    temp_dict_num: List[str] = []

                    #ok, našel jsi adjacent číslo, teď mi ho vytvoř celé... a zbytek odstraň z dictu
                    
                    while num_all_coors.get((new_x + step, new_y)) is not None:
                        step -= 1
                    step += 1
                    
                    while num_all_coors.get((new_x + step, new_y)) is not None:
                        temp_dict_num.append(num_all_coors.get((new_x + step, new_y), ""))
                        del num_all_coors[(new_x + step, new_y)]
                        step += 1
                    
                    if len(temp_dict_num) != 0:
                        gear_nums_to_mult.append(int("".join(temp_dict_num)))
                        temp_dict_num = []
                
        if len(gear_nums_to_mult) != 2:
            continue
        
        sum_used += gear_nums_to_mult[0] * gear_nums_to_mult[1]  

    print(sum_used)
    return

schematics()

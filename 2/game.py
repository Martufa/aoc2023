from typing import Dict

def game():
    total_possible = 0
    possible_ids = 0
    all_powers = 0
    max_values: Dict[str, int] = {"red":12, "green":13, "blue":14}
    with open("blabla.txt", "r") as all_games:
        for line in all_games:
            error = False
            
            game_id, game = line.split(":")
            real_id = int(game_id.split(" ")[1])
            game = game[:-1]
            game_rounds = game.split(";")
            
            max_red_found = 0
            max_green_found = 0
            max_blue_found = 0
            for current_round in game_rounds:
                number_and_type = current_round.split(",")
                for current_nat in number_and_type:
                    _, shown_number, shown_type = current_nat.split(" ")
                    
                    if shown_type == "red" and int(shown_number) > max_red_found:
                        max_red_found = int(shown_number)
                        
                    if shown_type == "green" and int(shown_number) > max_green_found:
                        max_green_found = int(shown_number)
                        
                    if shown_type == "blue" and int(shown_number) > max_blue_found:
                        max_blue_found = int(shown_number)
                    
                    
                    if int(shown_number) > max_values[shown_type]:
                        #máme chybu, neplatná hra
                        error = True

            if not error:
                total_possible += 1
                possible_ids += real_id
                all_powers += (max_red_found * max_green_found * max_blue_found)
    
    print(total_possible, possible_ids, all_powers)   
        
    return

game()

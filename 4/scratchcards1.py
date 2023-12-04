from typing import List

def scratchcards() -> None:
    
    with open("blabla.txt", "r", encoding = "utf-8") as scratchcards:
        total_won = 0
        total_scratches: List[int] = []
        for line in scratchcards:
            game_w_id, game = line.split(": ")
            game = game[:-1]
            win_list, my_list = game.split(" | ")
            my_win_nums = 0
            win_list = win_list.split(" ")
            my_list = my_list.split(" ")
            
            for win_num in win_list:
                if win_num in my_list and win_num != "" :
                    my_win_nums += 1
            
            if my_win_nums == 0:
                continue
            
            total_won += pow(2, my_win_nums - 1)
        
        print(total_won)    

scratchcards()

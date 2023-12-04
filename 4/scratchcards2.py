from typing import List

def scratchcards() -> None:
    
    with open("blabla.txt", "r", encoding = "utf-8") as scratchcards:
        total_won = 0
        total_scratches: List[int] = []
        for _ in range(197):
            total_scratches.append(1)
            
        for line_id, line in enumerate(scratchcards):
            for _ in range(total_scratches[line_id]):
                _, game = line.split(": ")
                game = game[:-1]
                
                win_list, my_list = game.split(" | ")
                my_win_nums = 0
                win_list = win_list.split(" ")
                my_list = my_list.split(" ")
                
                for win_num in win_list:
                    if win_num in my_list and win_num != "" :
                        my_win_nums += 1
                
                for i in range(my_win_nums):
                    if line_id + i >= len(total_scratches) - 1:
                        break
                    total_scratches[line_id + i + 1] += 1

        print(sum(total_scratches))

# correct answer is 5132675

scratchcards()

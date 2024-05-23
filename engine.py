# the solving engine for the word search puzzles

# RIGHT NOW IT IS SETUP TO BE EASY TO TEST MAKE SURE TO RUN THIS FILE ALONE

# read the table from the file
file_to_read = open("table.txt", "r")
corrected_ocr_result_table = file_to_read.read()
file_to_read.close()

#print(corrected_ocr_result_table)
corrected_ocr_result_table = corrected_ocr_result_table.replace(",", "")

# transform the table to a 2d matrix
word_matrix = []
for i in range(len(corrected_ocr_result_table.split("\n"))):
    word_matrix.append(list(corrected_ocr_result_table.split("\n")[i]))

#print(word_matrix)

#word = 'EMIC'
def check_all_ways(word_matrix, word, currenty, currentx, current_word_index, oldy, oldx):
    # im using try because if the index is out of range it will throw an error
    current_word_index += 1
    if current_word_index == len(word):
        print('found word')
        #print('y:', currenty+1)
        #print('x:', currentx+1)
        #print('coming from y:', oldy+1)
        #print('coming from x:', oldx+1)
        coming_from = ''
        if currenty > oldy:
            coming_from += 'up'
        elif currenty < oldy:
            coming_from += 'down'
        if currentx > oldx:
            coming_from += ' left'
        elif currentx < oldx:
            coming_from += ' right'
        print('coming from:', coming_from)
        return 
    try: # right
        if word_matrix[currenty][currentx+1] == word[current_word_index]:
            #print('found right')
            check_all_ways(word_matrix, word, currenty, currentx+1, current_word_index, currenty, currentx)
    except:
        pass
    try: # left
        if word_matrix[currenty][currentx-1] == word[current_word_index]:
            #print('found left')
            check_all_ways(word_matrix, word, currenty, currentx-1, current_word_index, currenty, currentx)
    except:
        pass
    try: # up
        if word_matrix[currenty-1][currentx] == word[current_word_index]:
            #print('found up')
            check_all_ways(word_matrix, word, currenty-1, currentx, current_word_index, currenty, currentx)
    except:
        pass
    try: # down
        if word_matrix[currenty+1][currentx] == word[current_word_index]:
            #print('found down')
            check_all_ways(word_matrix, word, currenty+1, currentx, current_word_index, currenty, currentx)
    except:
        pass
    try: # up right
        if word_matrix[currenty-1][currentx+1] == word[current_word_index]:
            #print('found up right')
            check_all_ways(word_matrix, word, currenty-1, currentx+1, current_word_index, currenty, currentx)
    except:
        pass
    try: # up left
        if word_matrix[currenty-1][currentx-1] == word[current_word_index]:
            #print('found up left')
            check_all_ways(word_matrix, word, currenty-1, currentx-1, current_word_index, currenty, currentx)
    except:
        pass
    try: # down right
        if word_matrix[currenty+1][currentx+1] == word[current_word_index]:
            #print('found down right')
            check_all_ways(word_matrix, word, currenty+1, currentx+1, current_word_index, currenty, currentx)
    except:
        pass
    try: # down left
        if word_matrix[currenty+1][currentx-1] == word[current_word_index]:
            #print('found down left')
            check_all_ways(word_matrix, word, currenty+1, currentx-1, current_word_index, currenty, currentx)
    except:
        pass
    return

def solve(word_matrix, word):
    for y in range(int(len(word_matrix) - 1)):
        for x in range(len(word_matrix[1])):
            if word_matrix[y][x] == word[0]:
                #print('found first letter')
                check_all_ways(word_matrix, word, y, x, 0, y, x)

        

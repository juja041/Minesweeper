import random

def bombicky():
    global list_squares
    list_squares=[i for i in range(100)]
    global list_bombs
    list_bombs = random.sample(list_squares, 20)
    for i in list_bombs:
        list_squares[i] = True

    print(list_squares)
    
    global number_of_adjacent_bombs
    number_of_adjacent_bombs = []


            

    for i in list_squares:
        
        if i is True:
            number_of_adjacent_bombs.append(True)
        
        else:
            
            if i%10 == 0:
                
                if i == 0:
                    
                    numb=0
                    for a in [i+1,i+10,i+11]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)    
                            
                elif i==90:
                    
                    numb=0
                    for a in [i+1,i-10,i-9]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)
                
                else:
                    
                    numb=0
                    for a in [i+1,i-10,i+10,i-9,i+11]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)
            
            elif i%10 == 9:
                
                if i == 9:
                    
                    numb=0
                    for a in [i-1,i+10,i+9]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)
                
                elif i == 99:
                    
                    numb=0
                    for a in [i-1,i-10,i-11]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)
                
                else:
                    
                    numb=0
                    for a in [i-1,i-10,i-11,i+9,i+10]:
                        
                        if list_squares[a] is True:
                            numb+=1
                    
                    number_of_adjacent_bombs.append(numb)
            
            elif i<9:
                
                numb=0
                for a in [i-1,i+1,i+10,i+9,i+11]:
                        
                    if list_squares[a] is True:
                        numb+=1
                    
                number_of_adjacent_bombs.append(numb)
                
            elif i > 90:
                
                numb=0
                for a in [i-1,i+1,i-10,i-9,i-11]:
                        
                    if list_squares[a] is True:
                        numb+=1
                    
                number_of_adjacent_bombs.append(numb)
                
            else:
                
                numb=0
                for a in [i-1,i+1,i-10,i-9,i-11,i+9,i+10,i+11]:
                        
                    if list_squares[a] is True:
                        numb+=1
                    
                number_of_adjacent_bombs.append(numb)
                
    global list_positions
    list_positions = []            
    for i in range(10):
        for u in range(10):
            list_positions.append((i*50,u*50))            
    global dict_adj_pos                    
    dict_adj_pos = dict(zip(list_positions,number_of_adjacent_bombs))    
    print(number_of_adjacent_bombs)
    print(list_positions)
    print(dict_adj_pos)

def adjacent(i):
    num = list_positions.index(i)
    if num%10 == 0:
        if num == 0:
            return (list_positions[num+1],list_positions[num+10],list_positions[num+11])
        
        elif num == 90:
            return (list_positions[num+1],list_positions[num-10],list_positions[num-9])
        
        else:
            return (list_positions[num+1],list_positions[num-10],list_positions[num+10],list_positions[num+11], list_positions[num-9])
            
    elif num%10 == 9:
        
        if num == 9:
            return (list_positions[num-1],list_positions[num+10],list_positions[num+9])
        
        elif num == 99:
            return (list_positions[num-1],list_positions[num-10],list_positions[num-11])
        
        else:
            return (list_positions[num-1],list_positions[num-10],list_positions[num-11],list_positions[num+9],list_positions[num+10])
    
    elif num<9:
        return (list_positions[num-1],list_positions[num+1],list_positions[num+10],list_positions[num+9],list_positions[num+11])
    
    elif num > 90:
        return (list_positions[num-1],list_positions[num+1],list_positions[num-10],list_positions[num-9],list_positions[num-11])
    
    else:
        return (list_positions[num-1],list_positions[num+1],list_positions[num-10],list_positions[num-9],list_positions[num-11],list_positions[num+9],list_positions[num+10],list_positions[num+11])

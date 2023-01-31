import random

list_squares=[i for i in range(100)]
list_bombs = random.sample(list_squares, 20)
for i in list_bombs:
    list_squares[i] = True

print(list_squares)

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
            

list_positions = []            
for i in range(10):
    for u in range(10):
        list_positions.append((i*50,u*50))            
                     
dict_adj_pos = dict(zip(list_positions,number_of_adjacent_bombs))    
print(number_of_adjacent_bombs)
print(list_positions)
print(dict_adj_pos)
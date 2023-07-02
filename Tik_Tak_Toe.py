import random
#player_2 decision
def playerTwo():
   x= random.randint(0,2)
   y=random.randint(0,2)
   return [x,y]
#process the players queries
def game(_input,Table,id):
  if Table[_input[0]][_input[1]]==' ':
    if id%2==0:
        Table[_input[0]][_input[1]]='X'
    else:
        Table[_input[0]][_input[1]]='O'
  else:
        if id%2==0:
            print("this coordination already in used") 
            player=chekString(input("Enter the coordinate(X,Y) separated by space: "))
            cordinates=list(map(int,player.split()))
            game(cordinates,Table,id)
        else:
            player=playerTwo()
            game(player,Table,id)
  return Table
# this method check if the string follows instructions
def chekString(str):
   if str.find(" ")==-1:
    str=input("Please separate number by space: ")
    while(str.find(" ")==-1):
            str=input("Please separate number by space: ")
    else:
        return str
   return str
# this method define the winner
def winner(Table):
    cond_1=(Table[0][2]==Table[1][2]==Table[2][2]!=' ' or Table[0][0]==Table[1][0]==Table[2][0]!=' ' or Table[0][1]==Table[1][1]==Table[2][1]!=' ')
    cond_2=Table[0][2]==Table[1][2]==Table[2][2]!=' '
    cond_3=Table[0][1]==Table[1][1]==Table[2][1]!=' '
    cond_4=Table[0][0]==Table[1][0]==Table[2][0]!=' '
    for Y in range(len(Table)):  
        if (Table[Y][0]==Table[Y][1]==Table[Y][2])and Table[Y][0]!=' ':
            return [False,Table[Y][0]]
    if (Table[0][0]==Table[1][1]==Table[2][2]!= ' ' or Table[0][2]==Table[1][1]==Table[2][0]!= ' ') :
        return [False,Table[1][1]]
    elif  cond_1 :
        if cond_2:
            return[False,Table[0][2]]
        elif cond_3:
            return[False,Table[0][1]]
        elif cond_4:
            return[False,Table[0][0]]
    return[True," "]
      
#The main code
Table=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
for i in range(9):
    check=winner(Table)
    if  check[0]:
        Old_Table=Table
        if i%2==0:
            player_1=chekString(input("Enter the coordinate(X,Y) separated by space: "))
            coordinates=list(map(int,player_1.split()))
            Table=game(coordinates,Old_Table,i)
        else:
            player_2=playerTwo()
            Table=game(player_2,Old_Table,i)
        print(f"    0    1     2\n0 {Table[0]}\n1 {Table[1]}\n2 {Table[2]}")
    else:
        print(f"{check[1]} player are the winner!!")
        break
print("Game over")



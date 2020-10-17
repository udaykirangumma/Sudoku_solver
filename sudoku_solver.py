def display_array(my_list):
#displays the bigger array to input numbers --- actual sudoku format
    print('     1  '+' 2 '+'  3 '+'    4 '+'  5 '+'  6 '+'    7 '+'  8 '+'  9 ')
    print('   _____________ _____________ _____________')
    print(' A | '+(my_list[0][0]) + ' | ' + (my_list[0][1]) + ' | ' + (my_list[0][2]) + ' | | '
          +(my_list[0][3]) + ' | ' + (my_list[0][4]) + ' | ' + (my_list[0][5])+' | | '+
          (my_list[0][6])+' | ' +(my_list[0][7])+ ' | '+ (my_list[0][8])+' |')
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' B | '+(my_list[1][0]) + ' | ' + (my_list[1][1]) + ' | ' + (my_list[1][2]) + ' | | '
          +(my_list[1][3]) + ' | ' + (my_list[1][4]) + ' | ' + (my_list[1][5])+' | | '+
          (my_list[1][6])+' | ' +(my_list[1][7])+ ' | '+ (my_list[1][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' C | '+(my_list[2][0]) + ' | ' + (my_list[2][1]) + ' | ' + (my_list[2][2]) + ' | | '
          +(my_list[2][3]) + ' | ' + (my_list[2][4]) + ' | ' + (my_list[2][5])+' | | '+
          (my_list[2][6])+' | ' +(my_list[2][7])+ ' | '+ (my_list[2][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print('   _____________ _____________ _____________')
    print(' D | ' + (my_list[3][0]) + ' | ' + (my_list[3][1]) + ' | ' + (my_list[3][2]) + ' | | '
          + (my_list[3][3]) + ' | ' + (my_list[3][4]) + ' | ' + (my_list[3][5]) + ' | | ' +
          (my_list[3][6]) + ' | ' + (my_list[3][7]) + ' | ' + (my_list[3][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' E | ' + (my_list[4][0]) + ' | ' + (my_list[4][1]) + ' | ' + (my_list[4][2]) + ' | | '
          + (my_list[4][3]) + ' | ' + (my_list[4][4]) + ' | ' + (my_list[4][5]) + ' | | ' +
          (my_list[4][6]) + ' | ' + (my_list[4][7]) + ' | ' + (my_list[4][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' F | ' + (my_list[5][0]) + ' | ' + (my_list[5][1]) + ' | ' + (my_list[5][2]) + ' | | '
          + (my_list[5][3]) + ' | ' + (my_list[5][4]) + ' | ' + (my_list[5][5]) + ' | | ' +
          (my_list[5][6]) + ' | ' + (my_list[5][7]) + ' | ' + (my_list[5][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print('   _____________ _____________ _____________')
    print(' G | ' + (my_list[6][0]) + ' | ' + (my_list[6][1]) + ' | ' + (my_list[6][2]) + ' | | '
          + (my_list[6][3]) + ' | ' + (my_list[6][4]) + ' | ' + (my_list[6][5]) + ' | | ' +
          (my_list[6][6]) + ' | ' + (my_list[6][7]) + ' | ' + (my_list[6][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' H | ' + (my_list[7][0]) + ' | ' + (my_list[7][1]) + ' | ' + (my_list[7][2]) + ' | | '
          + (my_list[7][3]) + ' | ' + (my_list[7][4]) + ' | ' + (my_list[7][5]) + ' | | ' +
          (my_list[7][6]) + ' | ' + (my_list[7][7]) + ' | ' + (my_list[7][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')
    print(' I | ' + (my_list[8][0]) + ' | ' + (my_list[8][1]) + ' | ' + (my_list[8][2]) + ' | | '
          + (my_list[8][3]) + ' | ' + (my_list[8][4]) + ' | ' + (my_list[8][5]) + ' | | ' +
          (my_list[8][6]) + ' | ' + (my_list[8][7]) + ' | ' + (my_list[8][8]+' |'))
    print('   |___|__' + '_|___'+'| |'+'___|__' + '_|___'+'| |'+'___|__' + '_|___|')

def display_smaller_array(my_list):

    #displays smaller array when a block is selected to have easier insertion of numbers

    print('     1  ' + ' 2 ' + '  3 ' + '    4 ' + '  5 ' + '  6 ' + '    7 ' + '  8 ' + '  9 ')
    print('   _____________ _____________ _____________')
    print(' o | ' + (my_list[0]) + ' | ' + (my_list[1]) + ' | ' + (my_list[2]) + ' | | '
          + (my_list[3]) + ' | ' + (my_list[4]) + ' | ' + (my_list[5]) + ' | | ' +
          (my_list[6]) + ' | ' + (my_list[7]) + ' | ' + (my_list[8]) + ' |')
    print('   |___|__' + '_|___' + '| |' + '___|__' + '_|___' + '| |' + '___|__' + '_|___|')




def choose_and_enter_number():
    my_lst = [[' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],
              [' ',' ',' ',' ',' ',' ',' ',' ',' '],]
    display_array(my_lst)
    flag=True
    alphabet=['A','B','C','D','E','F','G','H','I']
    numbers=['1','2','3','4','5','6','7','8','9']


    while flag:

        print('Please choose an alphabet to select a block or enter "done" to start solving')
        i=input().upper()

        if i=='DONE':
            flag=False
            display_array(my_lst)
            return my_lst

        elif i in alphabet:
            n=alphabet.index(i)
            numbers_line = my_lst[n]
            display_smaller_array(numbers_line)
            rep_num=True

            while rep_num:
                m=input("Please enter/erase a number or enter ok to exit this block  : ").lower()
                if m=="ok":
                    rep_num=False
                    display_array(my_lst)
                elif m in numbers:
                    num_replace=input("enter number you want to place here or 'e' to erase the cell: ").lower()
                    if num_replace=='e':
                        my_lst[n][int(m)-1]=" "
                        display_smaller_array(numbers_line)
                    else:
                        my_lst[n][int(m)-1]=num_replace
                        numbers_line[int(m)-1]=num_replace
                        display_smaller_array(numbers_line)
                else:
                        print("please enter valid number")
        else:
            print('Please enter a valid alphabet to choose a block!')

    print("The sudoku format is complete now it will be solved")




def logic(m,n,x,my_list):
    logic=True
    #check logic for rows and columns
    for i in range(9):
        if my_list[m][i]==x:
            logic=False
        elif my_list[i][n]==x:
            logic=False
        else:
            pass

    #logic check for the boxes
    for a in range(0,3):
        for b in range(0,3):
            m1=(m//3)*3
            n1=(n//3)*3
            if my_list[m1+a][n1+b]==x:
                logic=False
            else:
                pass
    return logic

def solver(my_list):
    numbers=['1','2','3','4','5','6','7','8','9']
    for i in range(9):
        for j in range(9):
            if my_list[i][j]==' ':
                for x in numbers:
                    if logic(i,j,x,my_list)==True:
                        my_list[i][j]=x
                        solver(my_list)
                        #keeps on repeating as long as the logic stays true
                        my_list[i][j]=' '
                        #to make the first block empty, before the recursion one
                return my_list
    display_array(my_list)



def working():
    print('hello this solver will solve the sudoku and give you a solution')
    solver(choose_and_enter_number())
    i=input("do you wanna solve more press 'y' for yes and 'n' for no: ")
    if i.lower()=='y':
        working()
    elif i.lower()=='n':
        exit()
    else:
        print('sorry not a valid response the program will now exit')

working()
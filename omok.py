# omok,  a  game  of paduk with five checkers placed in a row.
# computer network team, 10
# 160513 ver1. no rule , play game

# player 는 1과 2 교대로 1=0, 2=1
# player가 두는 돌은 0->player 번호로 맵핑
#init

player=0    
row,col=-1,-1 # init input row col
running=True
Winner = False

def display():    # 판을 보여줌 13x13
    for i in range(15):
        for j in range(15):
            print(locate[i][j],end=" ")
        print()
def isSize(n): # 놓은 위치가 맞는지 확인
    if(2 <= n and n <= 14 and int==type(n)):
        #판안에 존재하며 타입은 인트형이라면
        return True
    return False
def isEmpty(row,col):
    if(locate[row-1][col-1]>2): return True # 플레이어 돌은 0과 1 이므로 2보다크면빈자리
    return False

def checkWin(P,row,col):   # 승리 조건 판별
    rowcount = -1          # 각 방향으로 카운트를 세서 5이상이 되면 끝
    colcount = -1
    diagonalcount = -1
    diagonalcount2 = -1

    temp_row = 15-(row-1)  # 리스트 범위를 넘어가는 곳에서 오류가 나서 범위를 제한하기 위한 변수
    temp_col = 15-(col-1)

    if(temp_row >= temp_col):   # 11,11이상의 자리에서 탐색하기 위한 임시 변수
        temp_range = temp_col
    else:
        temp_range = temp_row
    
    if(P==0 and locate[row-1][col-1]==0):   # player가 0이고 마지막에 놓은 돌이 0일때
        if(temp_range<5):                   # 11,11이상의 자리라면
            for k in range(temp_range):     # 벽쪽 방향은 임시 변수 range만큼 탐색
                if(locate[row-1][col-1]==locate[row+k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-1][col+k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row+k-1][col+k-1]):
                    diagonalcount = diagonalcount +1
            for k in range(4):              # 반대쪽 방향으로 4칸 탐색
                if(locate[row-1][col-1]==locate[row-k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1] == locate[row-1][col-k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row-k-1][col-k-1]):
                    diagonalcount = diagonalcount +1
            if(temp_row<temp_col):          # 그 중에서 11,11 을 중심으로한 대각선 탐색
                for k in range(temp_range): # temp_row와 temp_col을 비교해서 큰쪽으로 많이 탐색, 작은쪽으로 적게탐색
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
                for k in range((7-temp_range)):
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
            elif(temp_row>temp_col):
                for k in range(temp_range):
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
                for k in range((7-temp_range)):
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
            elif(temp_row==temp_col):      # 11,11이라면 양쪽 모두 3칸씩 탐색
                for k in range(3):
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
        else:
            for k in range(4):             # 그 외경우는 모두 각방향으로 4칸씩 탐색
                if(locate[row-1][col-1]==locate[row+k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-1][col+k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row-1][col-k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row+k-1][col+k-1]):
                    diagonalcount = diagonalcount +1
                if(locate[row-1][col-1] == locate[row-k-1][col-k-1]):
                    diagonalcount = diagonalcount +1
                if(locate[row-1][col-1] == locate[row-k-1][col+k-1]):
                    diagonalcount2 = diagonalcount2 +1
                if(locate[row-1][col-1] == locate[row+k-1][col-k-1]):
                    diagonalcount2 = diagonalcount2 +1

    elif(P==1 and locate[row-1][col-1]==1):   # 마찬가지로 player가 1일때
        if(temp_range<5):
            for k in range(temp_range):
                if(locate[row-1][col-1]==locate[row+k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-1][col+k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row+k-1][col+k-1]):
                    diagonalcount = diagonalcount +1
            for k in range(4):
                if(locate[row-1][col-1]==locate[row-k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1] == locate[row-1][col-k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row-k-1][col-k-1]):
                    diagonalcount = diagonalcount +1
            if(temp_row<temp_col):
                for k in range(temp_range):
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
                for k in range((7-temp_range)):
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
            elif(temp_row>temp_col):
                for k in range(temp_range):
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
                for k in range((7-temp_range)):
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    else:
                        break
            elif(temp_row==temp_col):
                for k in range(3):
                    if(locate[row-1][col-1] == locate[row-1+k][col-1-k]):
                        diagonalcount2 = diagonalcount2 + 1
                    if(locate[row-1][col-1] == locate[row-1-k][col-1+k]):
                        diagonalcount2 = diagonalcount2 + 1
        else:
            for k in range(4):
                if(locate[row-1][col-1]==locate[row+k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-k-1][col-1]):
                    rowcount = rowcount + 1
                if(locate[row-1][col-1]==locate[row-1][col+k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row-1][col-k-1]):
                    colcount = colcount + 1
                if(locate[row-1][col-1] == locate[row+k-1][col+k-1]):
                    diagonalcount = diagonalcount +1
                if(locate[row-1][col-1] == locate[row-k-1][col-k-1]):
                    diagonalcount = diagonalcount +1
                if(locate[row-1][col-1] == locate[row-k-1][col+k-1]):
                    diagonalcount2 = diagonalcount2 +1
                if(locate[row-1][col-1] == locate[row+k-1][col-k-1]):
                    diagonalcount2 = diagonalcount2 +1

    if(5 <= rowcount or 5<= colcount or 5<= diagonalcount or 5<= diagonalcount2):
        if(rowcount - 2 >= 3 or colcount - 2 >=3 or diagonalcount - 2 >=3 or diagonalcount2 - 2 >=3): # 6목 예외조건
            print("6목입니다")
            return False
        else:
            return True
    else:
        return False



#미구현

##        print(not)
##def checkRule(P,row,col):

    
locate=[[5 for i in range(15)] for j in range(15)] # 벽은 9로 채우고 안쪽은 5로 채움
for i in range(15):
    for j in range(15):
        if i==0 or j==0:
            locate[i][j]=9
        if i==14 or j==14:
            locate[i][j]=9

#플레이어 이름은 리스트로 이름, 돌번호 로 매핑 시킬 수 있기때문에 나중에 작업.
               

while running :
    error=True
    display()
    if(player==0):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row)+1; col=int(col)+1
                print(isSize(row),isSize(col))
                if(isSize(row) and isSize(col) and isEmpty(row,col)): error=False;
                elif(isSize(row) == False or isSize(col) == False or isEmpty(row,col) == False): print("놓을 수 있는 범위 밖입니다") # 돌이 벽에 부딪힐때
                else: print("already",row-1,col-1)
            except:
                print("Player 1 input error")
            
    elif(player==1):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row)+1; col=int(col)+1
                if(isSize(row) and isSize(col) and isEmpty(row,col)): error=False;
                elif(isSize(row) == False or isSize(col) == False or isEmpty(row,col) == False): print("놓을 수 있는 범위 밖입니다")
                else: print("already",row-1,col-1)
            except:
                print("Player 2 input error")

    locate[row-1][col-1]=player # 위치에 돌을 놓는다
    Winner = checkWin(player,row,col) # 승리조건을 탐색
    print(Winner)
    if(Winner): #어떤 플레이어가 승리했을 시 
        print(player,'is Winner');
        while True:
            if(int(input("continue play game? 1=y"))==1): break
            else:
                if(int(input("진짜끝냄? 그럼 1 입력해"))==1): running=False;break
    else:
        player=(player+1)%2 # next player

print("Omok is Terminated...")

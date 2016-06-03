# omok,  a  game  of paduk with five checkers placed in a row.
# computer network team, 10
# 160513 ver1. no rule , play game

# player 는 1과 2 교대로 1=0, 2=1
# player가 두는 돌은 0->player 번호로 맵핑
#init
def display():    # 판을 보여줌 13x13
    for i in range(13):
        for j in range(13):
            print(locate[i][j],end=" ")
        print()
def isSize(n): # 놓은 위치가 맞는지 확인
    if(1 <= n and n <= 13 and int==type(n)):
        #판안에 존재하며 타입은 인트형이라면
        return True
    return False
def isEmpty(row,col):
    if(locate[row-1][col-1]>2): return True # 플레이어 돌은 0과 1 이므로 2보다크면빈자리
    return False

class queue:   # 승리 판별 및 금수 체크를 위한 queue
    lst=[]
    def __init__(self):
        self.lst=[]
    def __init__(self,x,y):
        self.lst=[]
        self.lst.append([x,y])
    def push(self, row,col):
        self.lst.insert(0,[row,col])
    def pop(self):
        
        a,b=self.lst.pop()
        return a,b
    def isEmpty(self):
        if(len(self.lst)==0):return True
        return False
        
#구현 check win
def checkWin(P,row,col):# P:Player
    
    QXX=queue(row,col)#-
    QXY=queue(row,col)#\
    QYX=queue(row,col)#/
    QYY=queue(row,col)#|
    print(QXX.lst)
    
    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXX.isEmpty()):#-        
        ROW,COL=QXX.pop()        
        cnt+=1
        print("XX",cnt)
        if(locate[ROW][COL-1]==P and visit[ROW][COL-1]==0 and COL-1>=0): visit[ROW][COL-1]=1;QXX.push(ROW,COL-1)
        if(locate[ROW][COL+1]==P and visit[ROW][COL+1]==0 and COL+1<=12):visit[ROW][COL+1]=1;QXX.push(ROW,COL+1)
    if(cnt==5): return True
    
    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXY.isEmpty()):#\
        ROW,COL=QXY.pop()
        cnt+=1
        print("XY",cnt,QXY.lst,ROW,COL)
        if(locate[ROW-1][COL-1]==P and visit[ROW-1][COL-1]==0 and ROW-1>= 0 and COL-1>=0): visit[ROW-1][COL-1]=1;QXY.push(ROW-1,COL-1)
        if(locate[ROW+1][COL+1]==P and visit[ROW+1][COL+1]==0 and ROW+1<= 12 and COL+1<=12): visit[ROW+1][COL+1]=1;QXY.push(ROW+1,COL+1)
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYX.isEmpty()):#/
        ROW,COL=QYX.pop()
        cnt+=1
        print("YX",cnt)
        if(locate[ROW-1][COL+1]==P and visit[ROW-1][COL+1]==0 and ROW-1>=0 and COL+1 <= 12): visit[ROW-1][COL+1]=1;QYX.push(ROW-1,COL+1)
        if(locate[ROW+1][COL-1]==P and visit[ROW+1][COL-1]==0 and ROW+1<=12 and COL-1 >= 0): visit[ROW+1][COL-1]=1;QYX.push(ROW+1,COL-1)
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYY.isEmpty()):#|
        ROW,COL=QYY.pop()
        cnt+=1
        print("YY",cnt)
        if(locate[ROW-1][COL]==P and visit[ROW-1][COL]==0 and ROW-1>=0): visit[ROW-1][COL]=1; QYY.push(ROW-1,COL)
        if(locate[ROW+1][COL]==P and visit[ROW+1][COL]==0 and ROW+1<=12):visit[ROW+1][COL]=1; QYY.push(ROW+1,COL)
    if(cnt==5): return True

    return False
# 미구현
# 막힌 수, 띄어진 수 구현 안됨. 
def checkRule(P,row,col):
    QXX=queue(row,col)#-
    QXY=queue(row,col)#\
    QYX=queue(row,col)#/
    QYY=queue(row,col)#|    
    #6개 경우의 수 - \ | /
    Jump_1=0
    cnt_1=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXX.isEmpty()):#-        
        ROW,COL=QXX.pop()        
        cnt_1+=1
        Jump_1+=1
        print("XX",cnt_1)
        print("XX",Jump_1)
        if(locate[ROW][COL-1]==P and visit[ROW][COL-1]==0 and COL-1>=0):visit[ROW][COL-1]=1;QXX.push(ROW,COL-1)
        if(locate[ROW][COL+1]==P and visit[ROW][COL+1]==0 and COL+1<=12):visit[ROW][COL+1]=1;QXX.push(ROW,COL+1)
        if(locate[ROW][COL-3]==P and visit[ROW][COL-3]==0 and COL-3>=2):visit[ROW][COL-3]=1;QXX.push(ROW,COL-3)
        if(locate[ROW][COL+3]==P and visit[ROW][COL+3]==0 and COL+3<=10):visit[ROW][COL+3]=1;QXX.push(ROW,COL+3)
        if(locate[ROW][COL-4]==P and visit[ROW][COL-4]==0 and COL-4>=3):visit[ROW][COL-4]=1;QXX.push(ROW,COL-4)
        if(locate[ROW][COL+4]==P and visit[ROW][COL+4]==0 and COL+4<=9):visit[ROW][COL+4]=1;QXX.push(ROW,COL+4)
        

    Jump_2=0
    cnt_2=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXY.isEmpty()):#\
        ROW,COL=QXY.pop()
        cnt_2+=1
        Jump_2+=1
        print("XY",cnt_2,QXY.lst,ROW,COL)
        print("XY",Jump_2)
        if(locate[ROW-1][COL-1]==P and visit[ROW-1][COL-1]==0 and ROW-1>= 0 and COL-1>=0): visit[ROW-1][COL-1]=1;QXY.push(ROW-1,COL-1)
        if(locate[ROW+1][COL+1]==P and visit[ROW+1][COL+1]==0 and ROW+1<= 12 and COL+1<=12): visit[ROW+1][COL+1]=1;QXY.push(ROW+1,COL+1)
        if(locate[ROW-3][COL-3]==P and locate[ROW-3][COL-3]==0 and ROW-3>=2 and COL-3>=0): visit[ROW-3][COL-3]=1;QXX.push(ROW-3,COL-3)
        if(locate[ROW+3][COL+3]==P and locate[ROW+3][COL+3]==0 and ROW+3<=10 and COL+3<=12): visit[ROW+3][COL+3]=1;QXX.push(ROW+3,COL+3)
        if(locate[ROW-4][COL-4]==P and locate[ROW-4][COL-4]==0 and ROW-4>=3 and COL-4>=0): visit[ROW-4][COL-4]=1;QXX.push(ROW-4,COL-4)
        if(locate[ROW+4][COL+4]==P and locate[ROW+4][COL+4]==0 and ROW+4<=9 and COL+4<=12): visit[ROW+4][COL+4]=1;QXX.push(ROW+4,COL+4)

    
    Jump_3=0
    cnt_3=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYX.isEmpty()):#/
        ROW,COL=QYX.pop()
        cnt_3+=1
        Jump_3+=1
        print("YX",cnt_3)
        print("YX",Jump_3)
        if(locate[ROW-1][COL+1]==P and visit[ROW-1][COL+1]==0 and ROW-1>=0 and COL+1 <= 12): visit[ROW-1][COL+1]=1;QYX.push(ROW-1,COL+1)
        if(locate[ROW+1][COL-1]==P and visit[ROW+1][COL-1]==0 and ROW+1<=12 and COL-1 >= 0): visit[ROW+1][COL-1]=1;QYX.push(ROW+1,COL-1)
        if(locate[ROW-3][COL+3]==P and visit[ROW-3][COL+3]==0 and ROW-3>=2 and COL+3 <= 12): visit[ROW-3][COL+3]=1;QXX.push(ROW-3,COL+3)
        if(locate[ROW+3][COL-3]==P and visit[ROW+3][COL-3]==0 and ROW+3<=10 and COL-3 >= 0): visit[ROW+3][COL-3]=1;QXX.push(ROW+3,COL-3)
        if(locate[ROW-4][COL+4]==P and visit[ROW-4][COL+4]==0 and ROW-4>=3 and COL+4 <= 12): visit[ROW-4][COL+4]=1;QXX.push(ROW-4,COL+4)
        if(locate[ROW+4][COL-4]==P and visit[ROW+4][COL-4]==0 and ROW+4<=9 and COL-4 >= 0): visit[ROW+4][COL-4]=1;QXX.push(ROW+4,COL-4)
    

    Jump_4=0
    cnt_4=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYY.isEmpty()):#|
        ROW,COL=QYY.pop()
        cnt_4+=1
        Jump_4+=1
        print("YY",cnt_4)
        print("YY",Jump_4)
        if(locate[ROW-1][COL]==P and visit[ROW-1][COL]==0 and ROW-1>=0): visit[ROW-1][COL]=1; QYY.push(ROW-1,COL)
        if(locate[ROW+1][COL]==P and visit[ROW+1][COL]==0 and ROW+1<=12): visit[ROW+1][COL]=1; QYY.push(ROW+1,COL)
        if(locate[ROW-3][COL]==P and visit[ROW-3][COL]==0 and ROW-3>=2): visit[ROW-3][COL]=1; QYY.push(ROW-3,COL)
        if(locate[ROW+3][COL]==P and visit[ROW+3][COL]==0 and ROW+3<=10): visit[ROW+3][COL]=1; QYY.push(ROW+3,COL)
        if(locate[ROW-4][COL]==P and visit[ROW-4][COL]==0 and ROW-4>=3): visit[ROW-4][COL]=1; QYY.push(ROW-4,COL)
        if(locate[ROW+4][COL]==P and visit[ROW+4][COL]==0 and ROW+4<=9): visit[ROW+4][COL]=1; QYY.push(ROW+4,COL)

        
    print(cnt_1,cnt_2,cnt_3,cnt_4)
    if(cnt_1==3 and cnt_2==3):return False
    if(cnt_1==3 and cnt_3==3):return False
    if(cnt_1==3 and cnt_4==3):return False
    if(cnt_2==3 and cnt_3==3):return False
    if(cnt_2==3 and cnt_4==3):return False
    if(cnt_3==3 and cnt_4==3):return False
    
    if(cnt_1==1 and cnt_2==1 and Jump_1==2 and Jump_2==2):return False
    if(cnt_1==1 and cnt_3==1 and Jump_1==2 and Jump_3==2):return False
    if(cnt_1==1 and cnt_4==1 and Jump_1==2 and Jump_4==2):return False
    if(cnt_2==1 and cnt_3==1 and Jump_2==2 and Jump_3==2):return False
    if(cnt_2==1 and cnt_4==1 and Jump_2==2 and Jump_4==2):return False
    if(cnt_3==1 and cnt_4==1 and Jump_3==2 and Jump_4==2):return False

    if(cnt_1==1 and cnt_2==1 and Jump_1==3 and Jump_2==3):return False
    if(cnt_1==1 and cnt_3==1 and Jump_1==3 and Jump_3==3):return False
    if(cnt_1==1 and cnt_4==1 and Jump_1==3 and Jump_4==3):return False
    if(cnt_2==1 and cnt_3==1 and Jump_2==3 and Jump_3==3):return False
    if(cnt_2==1 and cnt_4==1 and Jump_2==3 and Jump_4==3):return False
    if(cnt_3==1 and cnt_4==1 and Jump_3==3 and Jump_4==3):return False

    if(cnt_1==4 and cnt_2==4): return False
    if(cnt_1==4 and cnt_3==4): return False
    if(cnt_1==4 and cnt_4==4): return False
    if(cnt_2==4 and cnt_3==4): return False
    if(cnt_2==4 and cnt_4==4): return False
    if(cnt_3==4 and cnt_4==4): return False

    return True      
    

locate=[[5 for i in range(13)] for j in range(13)] # 벽은 9로 채우고 안쪽은 5로 채워서 판 초기화
#플레이어 이름은 리스트로 이름, 돌번호 로 매핑 시킬 수 있기때문에 나중에 작업.
player=0    
row,col=-1,-1 # init input row col
Winner=False # 승리를 판별 boolean
running=True

while running :
    error=True
    display()
    if(player==0):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row); col=int(col)
                print(isSize(row),isSize(col))
                print(checkRule(player,row-1,col-1))
                if(isSize(row) and isSize(col) and isEmpty(row,col)):
                    if(checkRule(player,row-1,col-1)):
                        error=False;
                    elif(isSize(row) == False or isSize(col) == False or isEmpty(row,col) == False): print("놓을 수 있는 범위 밖입니다") #범위 밖 예외처리
                    else:
                        print("Player 1 Rule Break")
                else: print("already",row,col)
            except:
                print("Player 1 input error")
            
    elif(player==1):
        while(error):
            try:
                row,col=(input("돌을 놓을 자리를 입력 (행 열) : ").split())
                row=int(row); col=int(col)
                if(isSize(row) and isSize(col) and isEmpty(row,col)): error=False;
                elif(isSize(row) == False or isSize(col) == False or isEmpty(row,col) == False): print("놓을 수 있는 범위 밖입니다")
                else: print("already",row,col)
            except:
                print("Player 2 input error")
    
    locate[row-1][col-1]=player # 위치에 돌을 놓는다
    Winner=checkWin(player,row-1,col-1)
    if(Winner): #어떤 플레이어가 승리했을 시 
        print(player,'is Winner');
## error 수정 요함        
        while True: 
            if(int(input("continue play game? 1=y"))==1):
                locate=[[5 for i in range(13)] for j in range(13)] # 벽은 9로 채우고 안쪽은 5로 채워서 판 초기화
                break
            else:
                if(int(input("진짜끝냄? 그럼 1 입력해"))==1): running=False;break
## error 수정 요함
    else:
        player=(player+1)%2 # next player

print("Omok is Terminated...")

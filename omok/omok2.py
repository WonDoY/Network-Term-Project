# omok,  a  game  of paduk with five checkers placed in a row.
# computer network team, 10
# 160513 ver1. no rule , play game
# 160515 ver2. + checkWin
# 160523 ver3. + checkRule
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

class queue:
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
##class stack:
#stack list를 사용 해서 넣을 경우 .append(argv) / .pop()
#
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
    
    Rule3 = 0 # 막히지 않은 3
    Rule4 = 0 # 막히지 않은 4 세기
       
    #case 1
    left='';right='';
    
    row_left=row; col_left=col-1;
    
    row_right=row; col_right=col+1;
    
    #case 2
    up='';down='';
    
    row_up=row-1;  col_up=col;
    
    row_down=row+1; col_down=col;
    
    #case 3
    leftup='';rightdown='';
    
    row_leftup=row-1; col_leftup=col-1;
    
    row_rightdown=row+1; col_rightdown=col+1;
    
    #case 4
    leftdown='';rightup='';
    
    row_leftdown=row+1; col_leftdown=col-1;
    
    row_rightup=row-1; col_rightup=col+1;
        
    for i in range(7):
        #case 1
        if(col_left >= 0) :
            left=str(locate[row_left][col_left])+left
            col_left-=1
        if(col_right <= 12) :
            right=right+str(locate[row_right][col_right])
            col_right+=1
            
        #case 2
        if(row_up >= 0) :
            up=str(locate[row_up][col_up])+up
            row_up-=1
        if(row_down <= 12):
            down=down+str(locate[row_down][col_down])
            row_down+=1

        #case 3
        if(row_leftup >= 0 and col_leftup >= 0):
            leftup=str(locate[row_leftup][col_leftup])+leftup
            row_leftup-=1; col_leftup-=1
        if(row_rightdown <= 12 and col_rightdown <= 12):
            rightdown=rightdown+str(locate[row_rightdown][col_rightdown])
            row_rightdown+=1; col_rightdown+=1

        #case 4
        if(row_leftdown <= 12 and col_leftdown >= 0):
            leftdown=str(locate[row_leftdown][col_leftdown])+leftdown
            row_leftdown+=1; col_leftdown-=1
        if(row_rightup >= 0 and col_rightup <= 12):
            rightup=rightup+str(locate[row_rightup][col_rightup])
            row_rightup-=1; col_rightup+=1
    line_left_right =left+'0'+right
    line_up_down =up+'0'+down
    line_leftup_rightdown=leftup+'0'+rightdown
    line_leftdown_rightup=leftdown+'0'+rightup
    mping3=['500505','505005','50005','50500005','505005005','505000505','500505005','500500505','50050005','50005005','50000505','5000005']    
    mping4=['500005','5050005','5005005','5000505',
            '5000050005','50500050005','50050000505','50050005005','5000500005','50005050005']

    print(line_left_right)
    print(line_up_down)
    print(line_leftup_rightdown)
    print(line_leftdown_rightup)
    for read in mping3:
        if(line_left_right.find(read)!=-1): Rule3+=1
        if(line_up_down.find(read)!=-1): Rule3+=1
        if(line_leftup_rightdown.find(read)!=-1): Rule3+=1
        if(line_leftdown_rightup.find(read)!=-1): Rule3+=1
    for read in mping4:
        if(line_left_right.find(read)!=-1): Rule4+=1
        if(line_up_down.find(read)!=-1): Rule4+=1
        if(line_leftup_rightdown.find(read)!=-1): Rule4+=1
        if(line_leftdown_rightup.find(read)!=-1): Rule4+=1
    print("Counting : ",Rule3,Rule4)
    if(Rule4>=2): return False
    if(Rule3>=2): return False
    return True     
        
                                      
   
locate=[[5 for i in range(13)] for j in range(13)] # 판 초기화
#플레이어 이름은 리스트로 이름, 돌번호 로 매핑 시킬 수 있기때문에 나중에 작업.
##locate[2][3] = 0
##locate[3][3] = 0
##locate[6][3] = 0
##locate[7][3] = 0
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
                print(isSize(row),isSize(col), isEmpty(row,col),checkRule(player,row-1,col-1))
                print(checkRule(player,row-1,col-1))
                
                if(isSize(row) and isSize(col) and isEmpty(row,col)):
                    if(checkRule(player,row-1,col-1)):
                        error=False;
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
                locate=[[5 for i in range(13)] for j in range(13)] # 판 초기화
                break
            else:
                if(int(input("진짜끝냄? 그럼 1 입력해"))==1): running=False;break
## error 수정 요함
    else:
        player=(player+1)%2 # next player

print("Omok is Terminated...")



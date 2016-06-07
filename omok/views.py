from django.shortcuts import render
from .models import Omok
from django.http import HttpResponse
from django.http import HttpResponseRedirect
user_1 = ""
# Create your views here.
def index(request): # index 이름 바꾸기 나중
	return render(request, 'omok/index.html') #닉네임 부분

def out(request, Id, name): # out 이름 바꾸기 나중 
	I = UserInfo.objects.get(id=name)
	room = RoomInfo.objects.get(id=int(Id))
	potal = {'room' : room, 'I': I }	
	if request.POST.get('OK') : 
		room.user_2 = 'none'
		room.pull = 1
		room.save()
	return render(request, 'omok/out.html',potal) #방나가

def not_name(request): # index_ing 이름 바꾸기 나중에 
	if request.POST.get('title') == '':
		return render(request,'omok/not_name.html')
   
	else:
		str = request.POST.get('title', False)
		UserInfo.objects.create(name=str)
		user = UserInfo.objects.get(name=str)
		request.session['user_id']=request.POST['title']
		user.one_or_two = 2
		user.save()
		return HttpResponseRedirect("/main/{}/".format(user.id))

def main(request, name):
	room = RoomInfo.objects.filter(full=1)
	I = UserInfo.objects.get(id=name)  
	potal = {'rooms':room, 'I':I }
	return render(request, 'omok/main.html', potal)
   
def make(request,myname):

	me=UserInfo.objects.get(id=myname)
	context={'me':me}
	return render(request, 'omok/make.html', context)


def omok(request, room_id, myname):
	global ready
	
	# me 이름 매칭 가져옴 DB
	me = UserInfo.objects.get(id=myname)
	# 
	room = RoomInfo.objects.get(id=int(room_id))

	board = []


	omok=omokBoard.objects.filter(room_number=room_id)

	if(omok):
		#str=request.POST.get('move', False)
		load=omok[0].board

		index=0
		
		for row in range(13):
			for col in range(13):
				board[row][col] = load[index]
				index+=1
		# save board load

		context={'board':board,'str':str,'room':room,'me':me}
		
		return render(request, 'omok/omok.html',context)


	else:
		b=""
		for i in board:
			for j in i:
				b=b+j
			# string +=

		# 생성
		omokBoard.objects.create(board=b, room_number=room_id)
		context={'board':board,'room':room,'me':me}
		
		return render(request, 'omok/omok.html',context)


def omok_ing(request, room_id, myname):


	me = UserInfo.objects.get(id=myname)
	# 위치 입력 
	place=request.POST.get('pos', False)
	# ->pos
	


	# gomoku board init
	board = [[5 for i in range(13)] for j in range(13)] 
	


	Omok=omokBoard.objects.filter(room_number=room_id)
	omok=Omok[0]
	load=omok.board

	
	index=0	
	for row in range(13):
		for col in range(13):
			board[row][col]=load[index]
			index+=1
	# match up


	place = place.split()
	pos_r = int(place[0])
	pos_c = int(place[1])
	
	#piece와 place을 인자로 받아 piece의 place동작이 올바른 동작인지 판별하는 함수 필요
	#동작이 적절하면 아래 실행

	## 수를 놓는다. user 의 no 을 알아야함.
	if(isSize(pos_r) and isSize(pos_c) and isEmpty(pos_r,pos_c)):
        if(checkRule(0,pos_r-1,pos_c-1)): #
        	board[pos_r][pos_c] = 0




	

	
	loader=""
	for i in board:
		for j in i:
			loader=loader+j

	omok.board = loader
	omok.save()


	return HttpResponseRedirect("/room/{}/omok/{}".format(room_id, me.id))




def make(request,myname):

	me=UserInfo.objects.get(id=myname)
	context={'me':me}



	return render(request, 'omok/make.html', context)
   




def make_ing(request, myname):

   user = UserInfo.objects.get(name=request.session['user_id'])


   user.one_or_two = 1


   str = request.POST.get('roomname', False)


   RoomInfo.objects.create(name=str)


   room = RoomInfo.objects.get(name=str)


   room.user1 = user.name


   room.save()


   context = {'roominform' : room , 'room_no' : room.id }
   
   
   return HttpResponseRedirect("/room/{}/{}".format(room.id, myname))


def room(request, room_id, myname):

	
	me=UserInfo.objects.get(id=myname)
	room = RoomInfo.objects.get(id=int(room_id))


	if(room.full == 0):
		room.user1=me.name
		room.full = 1
		room.save()
		context={'room': room,'me':me}


		return render(request, 'omok/room.html',context)


	elif(room.full == 1 and room.user1!=me.name):
		room.user2 = me.name
		room.full = 2 
		room.save()
		context={'room' : room, 'me':me }


		return render(request, 'omok/room.html',context)




	elif(room.user1!=me.name and room.user2!=me.name and room.full==2):
		
		return HttpResponseRedirect("/main/{}/".format(myname))



	else:
		"""
		저장 후 반환 
		"""
		context={'room' : room,'me':me }

		return render(request, 'omok/room.html',context)




def room_to_omok(requset, room_id, myname):


	me=UserInfo.objects.get(id=myname)
	room=RoomInfo.objects.get(id=room_id)




	if room.user1=='none' or room.user2=='none':

		return HttpResponseRedirect("/room/{}/{}".format(room.id, myname))



	global ok_1
	global ok_2
	ok_1=0
	ok_2=0


	while True:

		if room.user1==me.name:
			ok_1=1
			

		if room.user2==me.name:
			ok_2=1
			

		if ok_1 == 1 and ok_2 == 1:
			
			return HttpResponseRedirect("/room/{}/omok/{}".format(room.id, myname))
		





def isSize(n): # 놓은 위치가 맞는지 확인
    if(1 <= n and n <= 13 and int==type(n)):
        #판안에 존재하며 타입은 인트형이라면
        return True
    return False


def isEmpty(row,col):
	board = [[5 for i in range(13)] for j in range(13)] 
	


	Omok=omokBoard.objects.filter(room_number=room_id)
	omok=Omok[0]
	load=omok.board

	
	index=0	
	for row in range(13):
		for col in range(13):
			board[row][col]=load[index]
			index+=1


    if(board[row-1][col-1]>2): return True # 플레이어 돌은 0과 1 이므로 2보다크면빈자리
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
    
    
    board = [[5 for i in range(13)] for j in range(13)] 
	


	Omok=omokBoard.objects.filter(room_number=room_id)
	omok=Omok[0]
	load=omok.board

	
	index=0	
	for row in range(13):
		for col in range(13):
			board[row][col]=load[index]
			index+=1


    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXX.isEmpty()):#-        
        ROW,COL=QXX.pop()        
        cnt+=1
        print("XX",cnt)

        try :
            if(board[ROW][COL-1]==P and visit[ROW][COL-1]==0 and COL-1>=0):  visit[ROW][COL-1]=1;QXX.push(ROW,COL-1)
        except:
            print()
        try:
            if(board[ROW][COL+1]==P and visit[ROW][COL+1]==0 and COL+1<=12):visit[ROW][COL+1]=1;QXX.push(ROW,COL+1)
        except:
            print()
        
        
    if(cnt==5): return True
    
    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QXY.isEmpty()):#\
        ROW,COL=QXY.pop()
        cnt+=1
        print("XY",cnt,QXY.lst,ROW,COL)
        try:
            if(board[ROW-1][COL-1]==P and visit[ROW-1][COL-1]==0 and ROW-1>= 0 and COL-1>=0): visit[ROW-1][COL-1]=1;QXY.push(ROW-1,COL-1)
        except:
            print()
        try:
            if(board[ROW+1][COL+1]==P and visit[ROW+1][COL+1]==0 and ROW+1<= 12 and COL+1<=12): visit[ROW+1][COL+1]=1;QXY.push(ROW+1,COL+1)
        except:
            print()
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYX.isEmpty()):#/
        ROW,COL=QYX.pop()
        cnt+=1
        print("YX",cnt)
        try:
            if(board[ROW-1][COL+1]==P and visit[ROW-1][COL+1]==0 and ROW-1>=0 and COL+1 <= 12): visit[ROW-1][COL+1]=1;QYX.push(ROW-1,COL+1)
        except:
            print()
        try:
            if(board[ROW+1][COL-1]==P and visit[ROW+1][COL-1]==0 and ROW+1<=12 and COL-1 >= 0): visit[ROW+1][COL-1]=1;QYX.push(ROW+1,COL-1)
        except:
            print()
    if(cnt==5): return True

    cnt=0
    visit=[[0 for x in range(13)] for y in range(13)]
    visit[row][col]=1
    while (not QYY.isEmpty()):#|
        ROW,COL=QYY.pop()
        cnt+=1
        print("YY",cnt)
        try:
            if(board[ROW-1][COL]==P and visit[ROW-1][COL]==0 and ROW-1>=0): visit[ROW-1][COL]=1; QYY.push(ROW-1,COL)
        except:
            print()
        try:
            if(board[ROW+1][COL]==P and visit[ROW+1][COL]==0 and ROW+1<=12):visit[ROW+1][COL]=1; QYY.push(ROW+1,COL)
        except:
            print()
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
    

    board = [[5 for i in range(13)] for j in range(13)] 
	


	Omok=omokBoard.objects.filter(room_number=room_id)
	omok=Omok[0]
	load=omok.board

	
	index=0	
	for row in range(13):
		for col in range(13):
			board[row][col]=load[index]
			index+=1




    for i in range(7):
        #case 1
        if(col_left >= 0) :
            left=str(board[row_left][col_left])+left
            col_left-=1
        if(col_right <= 12) :
            right=right+str(board[row_right][col_right])
            col_right+=1
            
        #case 2
        if(row_up >= 0) :
            up=str(board[row_up][col_up])+up
            row_up-=1
        if(row_down <= 12):
            down=down+str(board[row_down][col_down])
            row_down+=1

        #case 3
        if(row_leftup >= 0 and col_leftup >= 0):
            leftup=str(board[row_leftup][col_leftup])+leftup
            row_leftup-=1; col_leftup-=1
        if(row_rightdown <= 12 and col_rightdown <= 12):
            rightdown=rightdown+str(board[row_rightdown][col_rightdown])
            row_rightdown+=1; col_rightdown+=1

        #case 4
        if(row_leftdown <= 12 and col_leftdown >= 0):
            leftdown=str(board[row_leftdown][col_leftdown])+leftdown
            row_leftdown+=1; col_leftdown-=1
        if(row_rightup >= 0 and col_rightup <= 12):
            rightup=rightup+str(board[row_rightup][col_rightup])
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
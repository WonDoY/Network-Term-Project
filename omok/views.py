#views.py


ready=0;
user1=""
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

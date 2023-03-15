from django.shortcuts import render, redirect
from .models import GameData, UserInfo

# Create your views here.
try:
    obj = GameData.objects.get(pk=1)
except:
    obj = GameData()

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    global val, navbarLogin
    if obj.isLogin:
        navbarLogin = '<a href="logout" id="loginIcon" class="navbarIcons">logout</a>'
    else:
        navbarLogin = '<a href="login" id="loginIcon" class="navbarIcons">login</a>'
    return render(request, 'home.html', {'navbarLogin':navbarLogin, 'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})

def login(request):
    return render(request, 'login.html')

def logout(request):
    obj.isLogin = False
    return redirect('home')

def aboutus(request):
    return render(request, 'aboutus.html')

def verify(request):
    global obj
    username = request.POST['username']
    password = request.POST['password']
    flag = True
    ind = 1
    while flag:
        try:
            obj1 = UserInfo.objects.get(pk=ind)
            if obj1.username == username and obj1.password == password:
                obj.isLogin = True
                return redirect('home')
            ind += 1
        except:
            flag = False
    return redirect('login')

def signup(request):
    return render(request, 'signup.html')

def insertData(request):
    name = request.POST['name']
    username = request.POST['username']
    password = request.POST['password']
    print(name,username,password)
    
    flag = True
    ind = 1
    while flag:
        try:
            obj1 = UserInfo.objects.get(pk=ind)
            if obj1.username == username:
                return redirect('signup')
            ind += 1
        except:
            flag = False
    obj = UserInfo()
    obj.name = name
    obj.username = username
    obj.password = password
    obj.save()

    return redirect('home')


# global variables

# 0 for x
# 1 for o
# 2 for empty
obj.grid = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]
obj.save()

val = [
    '<input type="submit" name="box1" class="boxes">',
    '<input type="submit" name="box2" class="boxes">',
    '<input type="submit" name="box3" class="boxes">',
    '<input type="submit" name="box4" class="boxes">',
    '<input type="submit" name="box5" class="boxes">',
    '<input type="submit" name="box6" class="boxes">',
    '<input type="submit" name="box7" class="boxes">',
    '<input type="submit" name="box8" class="boxes">',
    '<input type="submit" name="box9" class="boxes">'
]

againValue = ''
classValue = ''
navbarLogin = '<a href="login" id="loginIcon" class="navbarIcons">login</a>'

def minimax(grid, sym):
    if win(grid,0):
        return 1
    if win(grid,1):
        return -1
    if draw(grid):
        return 0
    if sym == 0:
        mx = 0
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 2:
                    grid[i][j] = sym
                    ev = minimax(grid, (sym+1)%2)
                    mx = max(mx,ev)
                    grid[i][j] = 2
        return mx
    mn = 10
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 2:
                grid[i][j] = sym
                ev = minimax(grid, (sym+1)%2)
                mn = min(mn,ev)
                grid[i][j] = 2
    return mn

def comp():
    global obj, val
    grid = [list(map(int,i)) for i in obj.grid]
    mn = 10
    optimalCh = -1
    for i in range(9):
        if grid[i//3][i%3] == 2:
            grid[i//3][i%3] = 1
            temp = minimax(grid, 0)
            if temp < mn:
                mn = temp
                optimalCh = i
            grid[i//3][i%3] = 2
    if optimalCh == -1:
        return
    obj.grid[optimalCh//3][optimalCh%3] = 1
    obj.save()    

def clean():
    global obj, val
    for i in range(9):
        if obj.grid[i//3][i%3] == 2:
            val[i] = '<img src="static/blank.png" alt="blank" height="95%" width="95%">'

def win(grid,symbol):
    if grid[0][0] == symbol and grid[0][1] == symbol and grid[0][2] == symbol:
        return True
    if grid[1][0] == symbol and grid[1][1] == symbol and grid[1][2] == symbol:
        return True
    if grid[2][0] == symbol and grid[2][1] == symbol and grid[2][2] == symbol:
        return True
    if grid[0][0] == symbol and grid[1][0] == symbol and grid[2][0] == symbol:
        return True
    if grid[0][1] == symbol and grid[1][1] == symbol and grid[2][1] == symbol:
        return True
    if grid[0][2] == symbol and grid[1][2] == symbol and grid[2][2] == symbol:
        return True
    if grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol:
        return True
    if grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol:
        return True
    return False

def draw(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 2:
                return False
    return True

def reset(request):
    global obj, val, againValue, classValue, navbarLogin
    
    for i in range(9):
        # reseting the grid
        obj.grid[i//3][i%3] = 2
        
        #reseting the vals
        val[i] = '<input type="submit" name="box{}" class="boxes">'.format(i+1)
    obj.save()

    #reseting the winValue and againValue
    winValue = ''
    againValue = ''
    classValue = ''

    return render(request, 'home.html', {'navbarLogin':navbarLogin, 'classValue':classValue,'again':againValue,'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})

def showResetScreen(result):
    global againValue, classValue
    classValue = 'class=blur'
    if result == 0:
        text = "Player Won!"
    elif result == 1:
        text = "Computer Won!"
    else:
        text = "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbspDraw!"
    againValue = '''
                <div id="resultText">
                    {}
                </div>
                <form action="reset">
                <input type="submit" value="Play again" id="resetBtn">
                </form>
    '''.format(text)

def drawShapes():
    global obj, val
    for i in range(9):
        if obj.grid[i//3][i%3] == 0:
            val[i] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
        elif obj.grid[i//3][i%3] == 1:
            val[i] = '<img src="static/circle.png" alt="O" height="95%" width="95%">'

def playing(request):
    global obj, val, againValue, classValue, navbarLogin
    if request.POST.get('box1',False) == 'Submit':
        obj.grid[0][0] = 0
    elif request.POST.get('box2',False) == 'Submit':
        obj.grid[0][1] = 0
    elif request.POST.get('box3',False) == 'Submit':
        obj.grid[0][2] = 0
    elif request.POST.get('box4',False) == 'Submit':
        obj.grid[1][0] = 0
    elif request.POST.get('box5',False) == 'Submit':
        obj.grid[1][1] = 0
    elif request.POST.get('box6',False) == 'Submit':
        obj.grid[1][2] = 0
    elif request.POST.get('box7',False) == 'Submit':
        obj.grid[2][0] = 0
    elif request.POST.get('box8',False) == 'Submit':
        obj.grid[2][1] = 0
    elif request.POST.get('box9',False) == 'Submit':
        obj.grid[2][2] = 0
    
    obj.save()
    drawShapes()
    comp()
    drawShapes()

    if win(obj.grid,0):
        winValue = 'Player Win!'
        clean()
        showResetScreen(0)
    if win(obj.grid,1):
        winValue = 'Computer Win!'
        clean()
        showResetScreen(1)
    if draw(obj.grid):
        winValue = "Draw"
        showResetScreen(2)
    return render(request, 'home.html', {'navbarLogin':navbarLogin, 'classValue':classValue,'again':againValue,'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})
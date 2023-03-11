from django.shortcuts import render
from time import sleep

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def home(request):
    global val
    return render(request, 'home.html', {'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})

# global variables

# 0 for x
# 1 for o
# 2 for empty
grid = [
    [2,2,2],
    [2,2,2],
    [2,2,2]
]

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
    global grid, val
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
    grid[optimalCh//3][optimalCh%3] = 1
    val[optimalCh] = '<img src="static/circle.png" alt="O" height="95%" width="95%">'
    

def clean():
    global grid, val
    for i in range(9):
        if grid[i//3][i%3] == 2:
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
    global grid, val, againValue, classValue
    
    for i in range(9):
        # reseting the grid
        grid[i//3][i%3] = 2
        
        #reseting the vals
        val[i] = '<input type="submit" name="box{}" class="boxes">'.format(i+1)

    #reseting the winValue and againValue
    winValue = ''
    againValue = ''
    classValue = ''

    return render(request, 'home.html', {'classValue':classValue,'again':againValue,'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})

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

def playing(request):
    global grid, val, againValue, classValue
    
    if request.POST.get('box1',False) == 'Submit':
        grid[0][0] = 0
        val[0] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box2',False) == 'Submit':
        grid[0][1] = 0
        val[1] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box3',False) == 'Submit':
        grid[0][2] = 0
        val[2] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box4',False) == 'Submit':
        grid[1][0] = 0
        val[3] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box5',False) == 'Submit':
        grid[1][1] = 0
        val[4] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box6',False) == 'Submit':
        grid[1][2] = 0
        val[5] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box7',False) == 'Submit':
        grid[2][0] = 0
        val[6] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box8',False) == 'Submit':
        grid[2][1] = 0
        val[7] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    elif request.POST.get('box9',False) == 'Submit':
        grid[2][2] = 0
        val[8] = '<img src="static/cross.png" alt="X" height="95%" width="95%">'
    
    comp()

    if win(grid,0):
        winValue = 'Player Win!'
        clean()
        showResetScreen(0)
    if win(grid,1):
        winValue = 'Computer Win!'
        clean()
        showResetScreen(1)
    if draw(grid):
        winValue = "Draw"
        showResetScreen(2)
    return render(request, 'home.html', {'classValue':classValue,'again':againValue,'btn1':val[0], 'btn2':val[1], 'btn3':val[2], 'btn4':val[3], 'btn5':val[4], 'btn6':val[5], 'btn7':val[6], 'btn8':val[7], 'btn9':val[8]})
from Grid import Grid
#defining the main fucntion to include all the functionality.
def main():
    
#putting grid(20) because game will be played on torus of (2-d grid of)20x20.
    run = Grid(20)

#Grid value for three different patterns viz pulsar, block and golsperglidergun    
    pulsar= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],];
                        
    Block =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],];
                    
    GolsperGliderGun=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0],
                        [0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1],
                        [0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1,1],
                        [1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0],
                        [1,1,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0],
                        [0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
                        [0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],];
    
    print("Pulsar")
    
    run.board=pulsar.copy()    
    run.printBoard()
    
    print("Block")
                        
    run.board=Block.copy()      
    run.printBoard()
        
    print("GolsperGliderGun")
    
    run.board=GolsperGliderGun.copy()     
    run.printBoard()
#putting the initial pattern of the game as given above.
    
    pattern_first = ''

     
    pattern_first = input('Enter 1 for pulsar, 2 for Block and 3 for GolsperGliderGun. To end the game enter any other symbol: ')
    
    if(pattern_first=='1'):
        run.board=pulsar.copy()    
    elif(pattern_first=='2'):
        run.board=Block.copy()   
    elif(pattern_first=='3'):
        run.board=GolsperGliderGun.copy()    
    else:
        return
    run.printBoard()

#Creating input to enter the symbol and calling the function nextpattern and printboard to go for nextpattern or to end the game
    symbol = 'y'
    while symbol == 'y' or symbol == 'Y':
        symbol = input('If you want to print the next pattern enter Y/y or if you want to end the game enter any other symbol: ')
        run.nextPattern()
        run.printBoard()



main()

'''
    Created on Mar 8, 2020
    This program determines the status of the board
    Parameters: not setup yet
'''
import hashlib
import math

def errorChecking(parms):
    # Default values for blank, light, and dark variables for 'magic numbers'
    light = 1
    dark = 2
    blank = 0
    board = []
    lowerBound = 0
    upperBound = 9
    
    # Check if two of the light, dark, and blank values are common; if they are, assign errorFlag = 5
    if(('light' in parms and 'dark' in parms and parms['light'] == parms['dark']) or ('light' in parms and 'blank' in parms and parms['light'] == parms['blank']) \
        or ('dark' in parms and 'blank' in parms and parms['dark'] == parms['blank'])):
        return [light, dark, blank, board, 5]
    
    # Check if the parameters exist and are not assigned null values; if they have null values, assign errorFlag of 3
    if(('light' in parms and (parms['light'] is None or parms['light'] is '')) or ('dark' in parms and (parms['dark'] is None or parms['dark'] is '')) \
        or ('blank' in parms and (parms['blank'] is None or parms['blank'] is '')) or ('board' in parms and (parms['board'] is None or parms['board'] is '' or parms['board'] is [])) \
            or ('integrity' in parms and (parms['integrity'] is None or parms['integrity'] is ''))):
        return [light, dark, blank, board, 3]
            
    # Try to convert board from string to array if it is received through the URL
    if('board' in parms and isinstance(parms['board'], str)):
        try:
            boardArray = parms['board'].split(',')
            for i in boardArray:
                if('[' in i):
                    board.append(int(i.replace('[', '')))
                elif(']' in i):
                    board.append(int(i.replace(']', '')))
                else:
                    board.append(int(i))
        except ValueError:
            return [light, dark, blank, board, 2]
    
    # Check if the board is a valid n x n board (where n is not odd and is 8 <= n <= 16)
    if(board == [] and (('board' not in parms) or 'board' in parms and len(parms['board']) not in [36, 64, 100, 144, 196, 256])):
        return [light, dark, blank, board, 4] # Board size is not correct
    elif(board != [] and (len(board) not in [36, 64, 100, 144, 196, 256])):
        return [light, dark, blank, board, 4] # Board size is not correct
            
    # Check if the parameters exist and are integers; if not, assign errorFlag of 2
    if('light' in parms and (type(parms['light']) != type(0))):
        try:
            if(isinstance(parms['light'], float)): # Determine if the string parameter is also a double then try to convert it
                return [light, dark, blank, board, 2]
            else:
                int(parms['light'])
        except ValueError:
            return [light, dark, blank, board, 2]
    if('dark' in parms and (type(parms['dark']) != type(0))):
        try:
            if(isinstance(parms['dark'], float)): # Determine if the string parameter is also a double then try to convert it
                return [light, dark, blank, board, 2]
            else:
                int(parms['dark'])
        except ValueError:
            return [light, dark, blank, board, 2]
    if('blank' in parms and (type(parms['blank']) != type(0))):
        try:
            if(isinstance(parms['blank'], float)): # Determine if the string parameter is also a double then try to convert it
                return [light, dark, blank, board, 2]
            else:
                int(parms['blank'])
        except ValueError:
            return [light, dark, blank, board, 2]
    if('integrity' in parms and (type(parms['integrity']) != type(''))):
        return [light, dark, blank, board, 6]
    
    # Determine if inputs exist for blank, light, dark, and size and pass them in if they do
    if('light' in parms):
        if(int(parms['light']) >= lowerBound and int(parms['light']) <= upperBound):
            light = int(parms['light'])
        else:
            return [light, dark, blank, board, 1]
    if('dark' in parms):
        if(int(parms['dark']) >= lowerBound and int(parms['dark']) <= upperBound):
            dark = int(parms['dark'])
        else:
            return [light, dark, blank, board, 1]
    if('blank' in parms):
        if(int(parms['blank']) >= lowerBound and int(parms['blank']) <= upperBound):
            blank = int(parms['blank'])
        else:
            return [light, dark, blank, board, 1]
    
    # Check if the tokens provided are actually in the board; if they aren't, assign errorFlag = 7
    if(board == [] and ('light' in parms and 'board' in parms and parms['light'] not in parms['board']) or ('dark' in parms and 'board' in parms and parms['dark'] not in parms['board']) \
       or ('blank' in parms and 'board' in parms and parms['blank'] not in parms['board'])):
        return [light, dark, blank, board, 7]
    elif(board != [] and ((light not in board) or (dark not in board) or (blank not in board))):
        return [light, dark, blank, board, 7]
    
    # All validation checks passed
    return [light, dark, blank, board, 0]

def determineNextPlayer(light, dark, board):
    # Determine who the next player is based on the number of pieces on the board
    return dark if((board.count(light) + board.count(dark)) % 2 == 0) else light

def isOnBoard(x, y, size):
    # Check whether or not a set of coordinates is on the board
    return x >= 0 and x < size and y >= 0 and y < size 

def checkValidMoves(light, dark, blank, board):
    # Local variables
    boardIndex = 0
    lightCanMove = False
    darkCanMove = False
    
    # Initialize size of each row/column and matrix with default values
    size = int(math.sqrt(len(board)))
    matrix = [[i for i in range(size)] for j in range(size)]
    
    # Fill matrix with board values
    for x in range(size):
        for y in range(size):
            matrix[x][y] = board[boardIndex]
            boardIndex += 1
        
    # Check all valid moves
    for x in range(size):
        for y in range(size):
            for xPath, yPath in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]: # One step in any direction from initial space
                xStart = x + xPath
                yStart = y + yPath
                xPlaceholder = x
                yPlaceholder = y
                if(isOnBoard(xStart, yStart, size)):
                    if(matrix[x][y] == light and matrix[xStart][yStart] == blank):
                        while isOnBoard(xPlaceholder, yPlaceholder, size):
                            xPlaceholder -= xPath
                            yPlaceholder -= yPath
                            if(isOnBoard(xPlaceholder, yPlaceholder, size) and matrix[xPlaceholder][yPlaceholder] == blank): # Blank space found in path; not valid
                                break
                            if(isOnBoard(xPlaceholder, yPlaceholder, size) and matrix[xPlaceholder][yPlaceholder] == dark): # Same color piece found later in path; dark has a valid move
                                darkCanMove = True
                    xPlaceholder = x
                    yPlaceholder = y
                    if(matrix[x][y] == dark and matrix[xStart][yStart] == blank):
                        while isOnBoard(xPlaceholder, yPlaceholder, size):
                            xPlaceholder -= xPath
                            yPlaceholder -= yPath
                            if(isOnBoard(xPlaceholder, yPlaceholder, size) and matrix[xPlaceholder][yPlaceholder] == blank): # Blank space found in path; not valid
                                break
                            if(isOnBoard(xPlaceholder, yPlaceholder, size) and matrix[xPlaceholder][yPlaceholder] == light): # Same color piece found later in path; dark has a valid move
                                lightCanMove = True
    
    # Returns two boolean values in an array indicating which players can move and which cannot
    return [lightCanMove, darkCanMove]

def checkIntegrity(light, dark, blank, board, nextPlayer, foundIntegrity):
    # Initialize size of each row/column and matrix with default values
    boardIndex = 0
    integrity = ''
    boardSize = int(math.sqrt(len(board)))
    matrix = [[i for i in range(boardSize)] for j in range(boardSize)] # Creates matrix from the board
    
    # Fill matrix with board values
    for x in range(boardSize):
        for y in range(boardSize):
            matrix[x][y] = board[boardIndex]
            boardIndex += 1
            
    # Create integrity hash with column order of board combined with token values
    for x in zip(*matrix):
        for y in x:
            integrity += str(y)
    integrity += "/" + str(light) + "/" + str(dark) + "/" + str(blank) + "/" + str(nextPlayer)
    updatedIntegrity = hashlib.sha256()
    updatedIntegrity.update(str.encode(integrity))
    
    # Compare the integrity that was given with the one just created and return boolean value indicating if they match or not
    return updatedIntegrity.hexdigest() != foundIntegrity

def _status(parms):
    # Get light, dark, blank, and errorFlag values while also checking for errors
    [light, dark, blank, board, errorFlag] = errorChecking(parms)
    
    # If no errors were raised previously, continue
    if(errorFlag == 0):
        # Determine who the next player is and check for any remaining valid moves
        if(board != []): # Board was read in from the URL
            [canLightMove, canDarkMove] = checkValidMoves(light, dark, blank, board)
            nextPlayer = determineNextPlayer(light, dark, board)
        else: # Board was passed via a unit test case
            [canLightMove, canDarkMove] = checkValidMoves(light, dark, blank, parms['board'])
            nextPlayer = determineNextPlayer(light, dark, parms['board'])
        
        if('integrity' in parms and board != []):
            if(checkIntegrity(light, dark, blank, board, nextPlayer, parms['integrity'])):
                errorFlag = 6 # Integrity hash was incorrect
        elif('integrity' in parms and 'board' in parms):
            if(checkIntegrity(light, dark, blank, parms['board'], nextPlayer, parms['integrity'])):
                errorFlag = 6 # Integrity hash was incorrect
        else:
            errorFlag = 6 # Integrity hash was not found
            
    # Create result to return
        if(canLightMove and canDarkMove):
            result = {'status': 'ok'}
        elif(not canLightMove and canDarkMove):
            result = {'status': 'dark'}
        elif(canLightMove and not canDarkMove):
            result = {'status': 'light'}
        else:
            result = {'status': 'end'}
        
    # Create result to return (overrides previous result if integrity is not correct)
    if(errorFlag == 1):
        result = {'status': 'error: one of the parameters is out of the specified bounds'}
    elif(errorFlag == 2):
        result = {'status': 'error: one of the parameters is not the correct type'}
    elif(errorFlag == 3):
        result = {'status': 'error: one of the parameters was passed a null value'}
    elif(errorFlag == 4):
        result = {'status': 'error: the board size is not valid or was missing'}
    elif(errorFlag == 5):
        result = {'status': 'error: the light, dark and blank parameters have a value in common'}
    elif(errorFlag == 6):
        result = {'status': 'error: the integrity hash is incorrect or missing'}
    elif(errorFlag == 7):
        result = {'status': 'error: the token values provided do not match the tokens listed in the board'}
    return result
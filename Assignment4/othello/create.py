'''
    Created on Mar 8, 2020
    This program creates the Reversi/Othello board from given parameters
    Parameters: {'light': Number that represents the light piece, 'dark': Number that represents the light piece, 'blank': Number that represents empty spaces,
        'size': Number that represents the number of rows and columns in the board}
'''
import hashlib

def _create(parms):
    # Default values for blank, light, dark, and size and variables for 'magic numbers'
    lowerBound = 0
    upperBound = 9
    sizeLowerBound = 6
    sizeUpperBound = 16
    blank = 0
    light = 1
    dark = 2
    size = 8
    errorFlag = 0
    
    # Check if two of the light, dark, and blank values are common; if they are, assign errorFlag = 5
    if('light' in parms and 'dark' in parms and parms['light'] == parms['dark']):
        errorFlag = 5
    if('light' in parms and 'blank' in parms and parms['light'] == parms['blank']):
        errorFlag = 5
    if('dark' in parms and 'blank' in parms and parms['dark'] == parms['blank']):
        errorFlag = 5
    
    # Check if the parameters exist and are not assigned null values; if they have null values, assign errorFlag of 3
    if(errorFlag == 0):
        if(('light' in parms and (parms['light'] is None or parms['light'] is '')) or ('dark' in parms and (parms['dark'] is None or parms['dark'] is '')) \
            or ('blank' in parms and (parms['blank'] is None or parms['blank'] is '')) or ('size' in parms and (parms['size'] is None or parms['size'] is ''))):
            errorFlag = 3
    
    # Check if the parameters exist and are integers; if not, assign errorFlag of 2
    if(errorFlag == 0):
        if('light' in parms and (type(parms['light']) != type(0))):
            try:
                int(parms['light'])
            except ValueError:
                errorFlag = 2
        if('dark' in parms and (type(parms['dark']) != type(0))):
            try:
                int(parms['dark'])
            except ValueError:
                errorFlag = 2
        if('blank' in parms and (type(parms['blank']) != type(0))):
            try:
                int(parms['blank'])
            except ValueError:
                errorFlag = 2
        if('size' in parms and (type(parms['size']) != type(0))):
            try:
                if(isinstance(parms['size'], str) and parms['size'].find('.') == -1): # Determine if the string parameter is also a double then try to convert it
                    int(parms['size'])
                else:
                    errorFlag = 2
            except ValueError:
                errorFlag = 2
            
    # If errorFlag is still 0 then all previous checks passed
    if(errorFlag == 0):
        # Determine if inputs exist for blank, light, dark, and size and pass them in if they do
        if('light' in parms):
            if(int(parms['light']) >= lowerBound and int(parms['light']) <= upperBound):
                light = int(parms['light'])
            else:
                errorFlag = 1
        if('dark' in parms):
            if(int(parms['dark']) >= lowerBound and int(parms['dark']) <= upperBound):
                dark = int(parms['dark'])
            else:
                errorFlag = 1
        if('blank' in parms):
            if(int(parms['blank']) >= lowerBound and int(parms['blank']) <= upperBound):
                blank = int(parms['blank'])
            else:
                errorFlag = 1
        if('size' in parms):
            if(int(parms['size']) >= sizeLowerBound and int(parms['size']) <= sizeUpperBound):
                if(int(parms['size']) % 2 == 0):
                    size = int(parms['size'])
                else:
                    errorFlag = 4  # Odd value (inside bounds) was passed
            else:
                errorFlag = 1
        
    # If all previous checks have passed then create the board and integrity hash
    if(errorFlag == 0):
        # Create board
        for i in range (2, 8):
            externalBlanks = (size * i) + i # Number of blank values to fill outside the light and dark values in the integrity hash (outside blank values in column-major order of board)
            internalBlanks = size - 2       # Number of blank values to fill in between the light and dark values in the integrity hash (inside blank values in column-major order of board)
            k = 0
            boardSize = externalBlanks * 2 + internalBlanks + 4
            internalBlanksIndex1 = externalBlanks + 2
            internalBlanksIndex2 = externalBlanks + 2 + internalBlanks
            externalBlanksIndex1 = externalBlanks + 2 + internalBlanks + 2
            externalBlanksIndex2 = externalBlanks + 2 + internalBlanks + 2 + externalBlanks
            if((i * 2 + 2) == size):
                board = [None] * boardSize # Fill board with None values
                for j in range(0, externalBlanks): # Fill beginning of board with blank values
                    board[j] = blank
                    k = j                                                    # K gets value of last index with a blank value
                board[k+1] = light                                           # Fill next spot with a light value
                board[k+2] = dark                                            # Fill next spot with a dark value
                for j in range(internalBlanksIndex1, internalBlanksIndex2):  # Fill inside portion of board with blanks
                    board[j] = blank
                    k = j                                                    # K gets value of last index with a blank value
                board[k+1] = dark                                            # Fill next spot with a light value
                board[k+2] = light                                           # Fill next spot with a dark value
                for j in range(externalBlanksIndex1, externalBlanksIndex2):  # Fill remainder of board with blank values
                    board[j] = blank
        
        # Create integrity SHA256 hash based on board size
        for i in range (2, 8):
            externalBlanks = (size * i) + i # Number of blank values to fill outside the light and dark values in the integrity hash (outside blank values in column-major order of board)
            internalBlanks = size - 2       # Number of blank values to fill in between the light and dark values in the integrity hash (inside blank values in column-major order of board)
            if((i * 2 + 2) == size):
                integrity = (str(blank) * externalBlanks) + str(light) + str(dark) + (str(blank) * internalBlanks) + str(dark) + str(light) + (str(blank) * externalBlanks) + "/" + \
                    str(light) + "/" + str(dark) + "/" + str(blank) + "/" + str(dark)
        updatedIntegrity = hashlib.sha256()
        updatedIntegrity.update(str.encode(integrity))
    
    # Create result to return
    if(errorFlag == 0):
        result = {'board': board, 'tokens': {'light': light, 'dark': dark, 'blank': blank}, 'status': 'ok', 'integrity': updatedIntegrity.hexdigest()}
    elif(errorFlag == 1):
        result = {'status': 'error: one of the parameters is out of the specified bounds'}
    elif(errorFlag == 2):
        result = {'status': 'error: one of the parameters is not an integer'}
    elif(errorFlag == 3):
        result = {'status': 'error: one of the parameters was passed a null value'}
    elif(errorFlag == 4):
        result = {'status': 'error: the size parameter was passed an odd value'}
    elif(errorFlag == 5):
        result = {'status': 'error: the light, dark and blank parameters have a value in common'}
    return result

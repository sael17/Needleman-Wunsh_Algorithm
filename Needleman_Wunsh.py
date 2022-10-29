import sys
import csv


"""
Function to print the output matrix. This function is mainly used for testing 
purposes
argument -- 2D (n*m) array that represents a matrix 

"""
def print_matrix(matrix:list[list]) -> None:
    for row in matrix:
        print(row)
    
"""
Main function of the program. This function is the one that handles all the logic
of the Needleman-Wunsh algorithm to align two DNA nucleoids or sequences.
arguments: string1 -> first sequence
           string2 -> second sequence 
Return: string representing both sequences aligned globally and the score obtained 
from the alignment

"""
def Needleman_Wunsh(string1: str, string2: str) -> str: 
    
    """
    Function tasked to return the score of two strings when comparing their 
    characters.
        1 if Ai == Bi
        -1 if Ai != Bi
        
    """
    def score(index_i:int, index_j:int) -> int:
        return 1 if string2[index_i] == string1[index_j] else -1
    
    # backtracking
    # backtracking choses the max score from up,left and diagonal
    # diagonal: no strikes (insert both characters as is)
    # up: strike sequence 1
    # left: strike sequence 2

    """
    Function tasked to conduct the backtracking of the built matrix in order
    to build the alignment strings. 
    
    Return: It returns the alignments string formatted as 
    expected: alignment1 alignment2 score 
    
    """
    def backtracking() -> str:
        
        """
        Future optimization for this: used lists and the join() function in order
        to avoid building a new string everytime we add a character, since this
        is what happens when we do string concanation.
        
        """
        sequence_1 = ""
        sequence_2 = ""
        
        # start from the result (last cell in the grid)
        row = n-1
        col = m-1
        
        # we only want to stop when we both row and col are 0
        # (0,0) means that we are at the beginning
        while row != 0 or col != 0:
            # calculate scores to determine where the backtracking should move
            # backtracking choses the max score from up,left and diagonal
            # up: strike sequence 1
            # left: strike sequence 2
            
            
            # level of priority: Diagonal > Left > up
            diagonal_score = matrix[row-1][col-1] + score(row-1,col-1)
            left_score = matrix[row][col-1] + d
            up_score = matrix[row-1][col] + d
            
            # next line is for debugging purposes
            # print("Scores:" + str(diagonal_score) + "," + str(left_score) + "," + str(up_score))
            
            # diagonal: no strikes (insert both characters as is) & move diagonally
            if diagonal_score > left_score and diagonal_score > up_score:
                sequence_1 = string1[col-1] + sequence_1
                sequence_2 = string2[row-1] + sequence_2
                row -= 1
                col -= 1
            
            # second case: go left
            # >= in order to give priority to the left and match the outputs
            # from the online calculator
            elif left_score >= diagonal_score and left_score >= up_score:
                sequence_1 = string1[col-1] + sequence_1
                sequence_2 = "-" + sequence_2
                col -= 1
            
            # last case: go up    
            else:
                sequence_2 = string2[row-1] + sequence_2
                sequence_1 = "-" + sequence_1
                row -= 1
        
        # return aligened sequences 
        return sequence_1 + " " + sequence_2 + " " + str(matrix[n-1][m-1])
        
 
    # rows
    n = abs(len(string2)) + 1
    # cols
    m = abs(len(string1)) + 1
    # penalty gap
    d = -2
    # n*m matrix (table)
    matrix = []

    # initialise matrix
    for row in range(n):
        matrix.append([])
        for col in range(m):
            matrix[row].append(0)

    # initalise rows 
    for col in range(m):
        matrix[0][col] = d*col

    # initalise cols
    for row in range(n):
        matrix[row][0] = d*row

    # fill matrix from left to right
    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = max(matrix[i-1][j-1]+score(i-1, j-1),
                               matrix[i][j-1]+d,
                               matrix[i-1][j]+d)
     
    # next line is for testing purposes        
    # print_matrix(matrix)
    
    return backtracking()


# we specify the newline keyword argument and pass an empty string
# this is because depending on the system, strings may end with a newline,
# This technique makes sure that that the csv module works correctly accross all platforms
if len(sys.argv) > 1:
    csv_file = open(sys.argv[1],newline="")
    reader = csv.reader(csv_file)  # the first line is the header

    header = next(reader)  # skip the header (first line)
    for row in reader:
        print(Needleman_Wunsh(row[0],row[1]))
   



 
# string1 = "ATGCT"
# string2 = "AGCT"
# print(needleman_Wunsh(string1, string2))
# # sequence1, sequence2
# # GATTACA, GTCGACGCA
# string2 = "GATTACA"
# string1 = "GTCGACGCA"
# # GATTAC--A
# print(needleman_Wunsh(string1, string2))

# string1 = "GATTACA"
# string2 = "GTCGACGCA"
# # GATTAC--A
# print(needleman_Wunsh(string1, string2))

# string2 = "TAFFBQF"
# string1 = "REFFJ"
# # GATTAC--A
# print(needleman_Wunsh(string1, string2))





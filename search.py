# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    """
    "*** YOUR CODE HERE ***"
    #First Initialize Open and Closed List.
    #For DFS Open will be Stack and Closed is set. Closed List is for Explored/Visited Nodes
    openList = util.Stack()
    closedList = set()
    
    #Get Start Node Position and Insert First Source node in OpenList
    startNodeState = problem.getStartState()
    
    #Make Tuple of State of Node and Directions/actions List to reach there from Start Node
    startNode = (startNodeState, [])
    openList.push(startNode)
    
    #Now Until Open List is Not Empty Check For every Node by taking it from Stack(OpenList) [LIFO] whether
    # it is Goal State or Not and if its Goal state than return the Directions/Actions List, otherwise
    # check if that node is not already in Visited/Closed List and if not than add to closed list and add 
    # that node's all Successors to OpenList with their Direction/Aactions List.
    while not openList.isEmpty():
        #Left End of Open (stack)
        leftmostNode = openList.pop()
        if problem.isGoalState(leftmostNode[0]):
            #print("Goal State Reached !!! ")
            #print("Actions : ")
            #print(currentNode[1])
            return leftmostNode[1]
        
        if leftmostNode[0] not in closedList:
            closedList.add(leftmostNode[0])
            for successor in problem.getSuccessors(leftmostNode[0]):
                childNodeState = successor[0]
                childNodeActions = leftmostNode[1] + [successor[1]]
                childNode = (childNodeState, childNodeActions)
                openList.push(childNode)
    return None

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #First Initialize Open and Closed List.
    #For BFS Open will be Queue and Closed is set. Closed List is for Explored/Visited Nodes
    openList = util.Queue()
    closedList = set()
    
    #Get Start Node Position and Insert First Source node in OpenList
    startNodeState = problem.getStartState()
    
    #Make Tuple of State of Node and Directions/actions List to reach there from Start Node
    startNode = (startNodeState, [])
    openList.push(startNode)
    
    #Now Until Open List is Not Empty Check For every Node by taking it from Queue(OpenList) [FIFO] whether
    # it is Goal State or Not and if its Goal state than return the Directions/Actions List, otherwise
    # check if that node is not already in Visited/Closed List and if not than add to closed list and add 
    # that node's all Successors to OpenList with their Direction/Aactions List.
    while not openList.isEmpty():
        #right End of Open (Queue)
        leftmostNode = openList.pop()
        if problem.isGoalState(leftmostNode[0]):
            #print("Goal State Reached !!! ")
            #print("Actions : ")
            #print(currentNode[1])
            return leftmostNode[1]
        
        if leftmostNode[0] not in closedList:
            closedList.add(leftmostNode[0])
            for successor in problem.getSuccessors(leftmostNode[0]):
                childNodeState = successor[0]
                childNodeActions = leftmostNode[1] + [successor[1]]
                childNode = (childNodeState, childNodeActions)
                openList.push(childNode)
    return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #First Initialize Open and Closed List.
    #For UCS Open will be PriorityQueue which will take Nodes from Queue based on their Priority 
    # rather than FIFO like normal Queue and Closed is set. Closed List is for Explored/Visited Nodes
    openList = util.PriorityQueue()
    closedList = set()
    
    #Get Start Node Position and Insert First Source node in OpenList
    startNodeState = problem.getStartState()
    
    #Make Tuple of State of Node and Directions/actions List to reach there from Start Node and 
    # 2nd value as its Priority Cost
    startNode = ((startNodeState, []), 0)
    openList.update(startNode, 0)
    
    #Now Until Open List is Not Empty Check For every Node by taking it from Priority Queue(OpenList) [Based on Cost] 
    # whether it is Goal State or Not and if its Goal state than return the Directions/Actions List, otherwise
    # check if that node is not already in Visited/Closed List and if not than add to closed list and add 
    # that node's all Successors to OpenList with their Direction/Aactions List and Priority Cost.
    while not openList.isEmpty():
        leftmostNode = openList.pop()
        if problem.isGoalState(leftmostNode[0][0]):
            #print("Goal State Reached !!! ")
            #print("Actions : ")
            #print(currentNode[1])
            return leftmostNode[0][1]
        
        if leftmostNode[0][0] not in closedList:
            closedList.add(leftmostNode[0][0])
            for successor in problem.getSuccessors(leftmostNode[0][0]):
                childNodeState = successor[0]
                childNodeActions = leftmostNode[0][1] + [successor[1]]
                childNodeCost = leftmostNode[1] + successor[2]
                childNode = ((childNodeState, childNodeActions), childNodeCost)
                openList.update(childNode, childNodeCost)
    return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #First Initialize Open and Closed List.
    #For A* Open will be PriorityQueue which will take Nodes from Queue based on their Total Cost 
    # which is g(n)[calculated in UCS] plus heuristic cost rather than FIFO like normal Queue and 
    # Closed is set. Closed List is for Explored/Visited Nodes
    openList = util.PriorityQueue()
    closedList = set()
    
    #Get Start Node Position and Insert First Source node in OpenList
    startNodeState = problem.getStartState()
    
    #Make Tuple of State of Node and Directions/actions List to reach there from Start Node and 
    # 2nd value as its Priority Cost
    startNode = ((startNodeState, []), 0)
    openList.update(startNode, 0)
    
    #Now Until Open List is Not Empty Check For every Node by taking it from Priority Queue(OpenList) [Based on Cost] 
    # whether it is Goal State or Not and if its Goal state than return the Directions/Actions List, otherwise
    # check if that node is not already in Visited/Closed List and if not than add to closed list and add 
    # that node's all Successors to OpenList with their Direction/Aactions List and TotalCost.
    while not openList.isEmpty():
        leftmostNode = openList.pop()
        if problem.isGoalState(leftmostNode[0][0]):
            #print("Goal State Reached !!! ")
            #print("Actions : ")
            #print(currentNode[1])
            return leftmostNode[0][1]
        
        if leftmostNode[0][0] not in closedList:
            closedList.add(leftmostNode[0][0])
            for successor in problem.getSuccessors(leftmostNode[0][0]):
                childNodeState = successor[0]
                childNodeActions = leftmostNode[0][1] + [successor[1]]
                childNodeCost = leftmostNode[1] + successor[2]
                childNode = ((childNodeState, childNodeActions), childNodeCost)
                openList.update(childNode, childNodeCost + heuristic(successor[0], problem))
    return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

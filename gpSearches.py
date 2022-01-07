#uninformed searches

#In this script we will use a map of nodes represnting cities and use several different search algorithms 
#to find the shortest route to our destination

#first we will use a simple breadth first search

#create helper function to take list with all nodes(and their mother node) used to find a goal node. Then traceback the route taken.
def bfspathtraceback (poppedlist, chased):
  if chased[1] == None:
    print('Route trace complete')
    


  else:
    for i in poppedlist:
      if i[0] == chased[1]:
        print (i)
        bfspathtraceback(poppedlist, i)

#function to run the breadth first search and find the shortest route to the goal node using the map of cities/nodes
def bstsearch (map, node, goal):

  #create list to store nodes that have been visited in order to avoid loop
  visited = []
  #List for nodes thats links have been searched and popped from the que
  popped = []
  #List for que of all nodes in the map
  que = []
  #Add start node to que and visited
  que.append([node, None])
  visited.append(node)

  #while loop to trigger the search
  while que:

    #pop first in que to m var, add to popped for trace back and check if node is goal destination then break loop
    m = que.pop(0)
    popped.append(m)
    if m[0] == goal:
      print('Breadth First Search complete, the quickest route is:')
      print(m)
      bfspathtraceback(popped, popped[-1])
      break

    #for loop in current popped nodes peers/neighbours, if not already in visited list add to the que
    else:
      for peers in map[m[0]]:
        if peers not in visited:
          que.append([peers, m[0]])
          visited.append(peers)


#map of each city/node and its peers/neighbours
mappeers = {
  'arad' : ['zer','tim', 'sibu'],
  'zer' : ['arad', 'ord'],
  'ord' : ['zer', 'sibu'],
  'tim' : ['arad', 'rim'],
  'sibu' : ['arad', 'ord', 'fag', 'rim'],
  'rim' : ['tim', 'pit', 'sibu'],
  'fag': ['buk', 'sibu'],
  'pit': ['rim', 'buk']
}

#run the search giving start node and goal node
bstsearch(mappeers, 'arad' ,'buk')


#Here we use uniform cost search which takes into account the cost / distance of moving from each node. In this case it is number representing miles.


#helper func to take the name of two linked nodes and store value for distance between them
distdict ={}

def insertdistance(node1,node2,distancy):
    distdict[node1+node2] = distancy
    distdict[node2+node1] = distancy

insertdistance('arad', 'zer', 75)
insertdistance('arad', 'tim', 118)
insertdistance('arad', 'sibu', 140)
insertdistance('zer', 'ord', 71)
insertdistance('ord', 'sibu', 151)
insertdistance('tim', 'rim', 145)
insertdistance('sibu', 'fag', 99)
insertdistance('sibu', 'rim', 80)
insertdistance('rim', 'pit', 97)
insertdistance('fag', 'buk', 211)
insertdistance('pit', 'buk', 101)


#now we use breadth first but add a condition to pop/select node with least accumalated distance.
#the function takes a map representing cities and the start and goal city/node
def UniformCostSearch (map, node, goal):

  visited = []
  popped = []
  que = []
  #append original start node and length 0 to que.
  que.append([node, None, 0])
  visited.append(node)

  while que:

    #for loop through que lists to find node with lowest distance travel and then report its index to be popped
    d= 0
    index = 0
    for i in que:
      if i[2] < que[d][2]:
        d = index
      index += 1
    #print('lowest distance travelled node is', que[d])

    m = que.pop(d)
    popped.append(m)
    visited.append(m[0])
    if m[0] == goal:
      print('Uniform Cost Search complete, the quickest route is:')
      print(m)
      bfspathtraceback(popped, popped[-1])
      break

    #for loop in current popped node from que and add its peers to back of que and visited if not already visited.
    else:
      for peers in map[m[0]]:
        if peers != m[0]:
          if peers not in visited:
            #append the peer its mother and the distance travelled in order to be added added to previous mothers distances
            que.append([peers, m[0], m[2]+distdict[peers+m[0]]])

#run the program with start and goal node
UniformCostSearch(mappeers, 'arad', 'buk')


# informed search

#Here we use a* search. a* is more intelligent than previous search algorithms because it 
#takes into account extra info about the position of the goal relative to current node. 
#Using this hueristic we can add another layer of intelligence to our gps
#This search uses the same formula as uniform cost, calculating distance in miles 
#but uses a heuristic to make better choices on the route to take

def astar (map, node, goal):

  #create visited and que lists to track and avoid loops or revisitin
  visited = []
  popped = []
  que = []
  #append original start node 
  que.append([node, None, 0, nodeheristics[node]])
  #add original start node to visisted and que to stop it popping origin twice
  visited.append(node)

  while que:

    #for loop through que lists to find node with lowest distance travel + a* heuristic and then report index to be popped
    d= 0
    index = 0
    for i in que:
      if i[2] < que[d][2]:
        d = index
      index += 1
    #print('lowest distance travelled node is', que[d])

    m = que.pop(d)
    popped.append(m)
    visited.append(m[0])
    if m[0] == goal:
      print('A* Search complete, the quickest route is:')
      print(m)
      bfspathtraceback(popped, popped[-1])
      break

    else:
      for peers in map[m[0]]:
        if peers != m[0]:
          if peers not in visited:
            #append the peer, its mother and the distance travelled value, to get to it added to previous mothers distances + its nodes huristic(h)
            que.append([peers, m[0], m[2]+distdict[peers+m[0]]+nodeheristics[peers]])

# create new dictionary with heuristic value added to each node

nodeheristics = {
  'arad' : 366 ,
  'zer' : 324 ,
  'ord' : 380,
  'tim' : 329,
  'sibu' : 253,
  'rim' : 193,
  'fag': 176,
  'pit': 100,
  'buk' : 0 }

#run the search
astar(mappeers, 'arad', 'buk')
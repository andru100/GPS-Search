#uninformed searches

#depth first search searches each nodes peers goes down level first then back tracks. Its good for decision tree or binary trees searches where its weighted and can cut search in half
#not good for infinate trees or graphs because it will infinitely go down left side. if used in a graph must use visitted [] to make sure not stuck in loop

#breadth first search goes level by level and finds the answer in the shotest steps from beginning node. but need a func to track how it got there.
#always finds shortest route by testing in levels so every oprion that takes two steps before everyone that takes 3 steps.

#created helper func to take a solved popped list and traceback the route of last val list with gaol as node val and trace back its mothers
#using recursion saying for loop in popped list if i[0] = current ones mother print and run again chasing its mother.. stop when mother is none because reached the start node
def bfspathtraceback (poppedlist, chased):
  if chased[1] == None:
    print('ur at the begining node has no mother')


  else:
    for i in poppedlist:
      if i[0] == chased[1]:
        print (i)
        bfspathtraceback(poppedlist, i)

#breadth first search always findest shortes steps to the goal in a tree or graph search
#so used it to search a map graph with peers and finde quickest route (in steps) to gal destination
#steps are to take args for the map, the starting node and the goal destination

def bstsearch (map, node, goal):

  #create visited and que lists to track and avoid loops or revisiting + add start node to que which will
  #be popped into visited in while loop used for recursion
  visited = []
  popped = []
  que = []
  #visited.append([node, 'none'])
  que.append([node, None])
  #add original start node to visisted and que to stop it popping origin twice eg thinking its ok to c its neighbor as peer and readding to que fuking up traceback!
  #keep visisted a simple track of jus node key no need to carry mother because makes harder to do a if in statement on list of lists
  visited.append(node)

  #while que has a value loop
  while que:

    #pop first in que to m var add topopped for trace back and check if found gaol destination and break while
    m = que.pop(0)
    popped.append(m)
    if m[0] == goal:
      print('found it')
      #print last node to be chased because traceback is recursion and if u say print at beggining it will keep doig it.
      print(m)
      bfspathtraceback(popped, popped[-1])
      break

    #do for loop in current popped val from que node and add its peers to back of que and visited if not already visited... visited maens scene, cant use que because some get popped so will be missing!
    else:
      for peers in map[m[0]]:
        if peers not in visited:
          que.append([peers, m[0]])
          visited.append(peers)


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

bstsearch(mappeers, 'arad' ,'buk')


#Uniform cost search is same a bst except it takes inro account the cost / distance of moving from each node
#it adds peers to the que like bst but adds them with the added up cost of last steps aswell
#then instead of popping the fisrt in que it pops the priority one which is one with lowest cost!
#so it will do for loop through que and pull 1 with min cost variable add to visited etc
#can be done with class and giving each node a sel.cost and the longness of creating a dict with every poss step from node to nodes cost
#long byt do once u get bored or for portfolio!

#helper func to take the name of two linked nodes and store value for distance to travel there it creates two vals with names reversed
#so if search looks backtrack it can find var.

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


#now use breadth first but add a condition to pop/select node with least accumalated distance. need to add a tracker variable for total distance
#travelled to get to node. add to list containing mother node. could also do sel.mother and self.distravelled with classes and pointers
#can keep traceback func from b4 so jus change search

def dijifiksearch (map, node, goal):

  #create visited and que lists to track and avoid loops or revisiting + add start node to que which will
  #be popped into visited in while loop used for recursion
  visited = []
  popped = []
  que = []
  #append original start node and length 0 to que([node, 'none', 0])
  que.append([node, None, 0])
  #add original start node to visisted and que to stop it popping origin twice eg thinking its ok to c its neighbor as peer and readding to que fuking up traceback!
  #keep visisted a simple track of jus node key no need to carry mother because makes harder to do a if in statement on list of lists
  visited.append(node)

  #while que has a value loop
  while que:

    #for loop through que lists to find lowest var of distance travel and then report index to be popped
    d= 0
    index = 0
    #check if d is empty
    for i in que:
      if i[2] < que[d][2]:
        d = index
      index += 1
    print('lowest distance travelled node is', que[d])

    #pop the one in que thats 3rd variable for distance is shortest to m var add topopped for trace back and check if found gaol destination and break while
    m = que.pop(d)
    popped.append(m)
    #visited becomes popped so nodes can be revistsed but have to use extra list cos u want to do if node not in
    #only want to carry node name and not whole list so can iterate heck
    visited.append(m[0])
    if m[0] == goal:
      print('found it')
      #print last node to be chased because traceback is recursion and if u say print at beggining it will keep doig it.
      print(m)
      bfspathtraceback(popped, popped[-1])
      break

    #do for loop in current popped val from que node and add its peers to back of que and visited if not already visited... visited maens scene, cant use que because some get popped so will be missing!
    else:
      for peers in map[m[0]]:
        if peers != m[0]:
          if peers not in visited:
            #append the peer its mother and the distance travelled to get to it added to previous mothers distances
            que.append([peers, m[0], m[2]+distdict[peers+m[0]]])
            #visited.append(peers)

dijifiksearch(mappeers, 'arad', 'buk')


# informed search
# a* search is informed because it has extra info about the position of the goal using hueristic (h)
#its jus a dijivic/uniform cost search which takes into account lowest cost to node / distance but adds the hurestic h value of the node
#to the calculation of which one to explore/pop next. all u need to do is add the h value to the dictionry of node values and peers and add
#it to the calculation. eg node cost/distance value + heuristic/distance to node value.

def astar (map, node, goal):

  #create visited and que lists to track and avoid loops or revisiting + add start node to que which will
  #be popped into visited in while loop used for recursion
  visited = []
  popped = []
  que = []
  #append original start node and length 0 cos start and heuristic value tho not needed cos its at begging to que([node, 'none', 0])
  que.append([node, None, 0, nodeheristics[node]])
  #add original start node to visisted and que to stop it popping origin twice eg thinking its ok to c its neighbor as peer and readding to que fuking up traceback!
  #keep visisted a simple track of jus node key no need to carry mother because makes harder to do a if in statement on list of lists
  visited.append(node)

  #while que has a value loop
  while que:

    #for loop through que lists to find lowest var of distance travel + a* heuristic and then report index to be popped
    d= 0
    index = 0
    #check if d is empty
    for i in que:
      if i[2] < que[d][2]:
        d = index
      index += 1
    print('lowest distance travelled node is', que[d])

    #pop the one in que thats 3rd variable for distance is shortest to m var add topopped for trace back and check if found gaol destination and break while
    m = que.pop(d)
    popped.append(m)
    #visited becomes popped instead of discovered peers so nodes can be revistsed but have to use extra list cos u want to do if node not in
    #only want to carry node name and not whole list so can iterate heck
    visited.append(m[0])
    if m[0] == goal:
      print('found it')
      #print last node to be chased because traceback is recursion and if u say print at beggining it will keep doig it.
      print(m)
      #bfspathtraceback(popped, popped[-1])
      break

    #do for loop in current popped val from que node and add its peers to back of que and visited if not already visited... visited maens scene, cant use que because some get popped so will be missing!
    #m[0] holds the current popped nodes naame so use it to search map dict for its peers
    #then check the peers havent been popped cos then shortest distance found already and that its not its mother so dont backtrack (should be m[1]??
    #then add to que list with peer node, its mother, and distance travelled so far + distance from mother to that node using distdict which key
    # is concantation of node name eg peers from for loop and m[0] which is mother then and h value using node name in heuristicnode dict
    else:
      for peers in map[m[0]]:
        if peers != m[0]:
          if peers not in visited:
            #append the peer its mother and the distance travelled value to get to it added to previous mothers distances + its nodes huristic(h)
            que.append([peers, m[0], m[2]+distdict[peers+m[0]]+nodeheristics[peers]])
            #visited.append(peers)

# create new dictionary with heuristic value added to each node for a*

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

astar(mappeers, 'arad', 'buk')
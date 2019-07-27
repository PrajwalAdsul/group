def getAllNodes(*a):
	nodes = set()
	for x in a:
		f = open(x, "r")
		l = f.readlines()
		for x in l:
			y = x.split(" ")
			nodes.add(int(y[0]))
			nodes.add(int(y[1]))
		f.close()
	return nodes

def buildAdjList(d, *a):
	for x in a:
		f = open(x, "r")
		l = f.readlines()
		for x in l:
			y = x.split(" ")
			d[int(y[0])].append(int(y[1]))
		f.close()
	return d	

def dfsUtil(d, i, visited, stack):
	visited[i] = True
	for x in d[i]: 
		if not visited[x]:
			dfsUtil(d, x, visited, stack)
	stack.append(i)

def dfs(d):
	visited = [False] * len(d)
	stack = []
	for i in d.keys():
		if not visited[i]:
			dfsUtil(d, i, visited, stack)
	return stack

def getRev(d):
	rev = dict()
	for x in range(len(d)):
		rev[x] = list()
	for x in d.keys():
		for y in d[x]:
			rev[y].append(x)
	return rev

def sccdfsUtil(rev, i, visited, l):
	visited[i] = True
	for x in rev[i]: 
		if not visited[x]:
			dfsUtil(rev, i, visited, l)
	l.append(i)

def sccdfs(rev, s):
	visited = [False] * len(rev)
	res = list()
	s.reverse()
	for i in s:
		if not visited[i]:
			l = list()
			sccdfsUtil(rev, i, visited, l)
			if(len(l) > 1):
				l.pop(len(l) - 1)
			res.append(l)
	return res

def getSCCs(d):
	s = dfs(d)
	rev = getRev(d)
	SCCs = sccdfs(rev, s)
	print(SCCs)

def getmap(*a):
	d = dict()
	nodes = getAllNodes(*a)
	for i in nodes:
		d[i] = list()
	d = buildAdjList(d, *a)
	SCCs = getSCCs(d)

if __name__ == '__main__':
	l = getmap('pages.txt', 'authors.txt', 'likes.txt', 'follow.txt')

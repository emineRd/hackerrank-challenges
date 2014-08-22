l1 = raw_input().split()
N = int(l1[0])
M = int(l1[1])

EDGES = []

for i in range(M):
	l1 = raw_input().split()
	l1[0] = int(l1[0])
	l1[1] = int(l1[1])
	EDGES.append(l1)

TREE = []
INFO = []

def find_children(x):
	CHILDREN = []

	for i in range(M):
		if EDGES[i][1] == x:
			CHILDREN.append(EDGES[i][0])
			grand = find_children(EDGES[i][0])
			for g in grand: 
				CHILDREN.append(g)

	return CHILDREN

def generate_tree():
	global TREE

	for i in range(N):
		TREE.append([i+1])

	for i in range(N):
		TREE[i].append(find_children(i+1))

generate_tree()

count = 0 
for i in range(N):
	if len(TREE[i][1]) % 2 == 1 : 
		count +=1

print count-1

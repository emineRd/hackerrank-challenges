GEM_LIST = []
POTENTIALS = []
N = input()

for i in range(N):
	n = raw_input()
	GEM_LIST.append(n)

#manage gem_list
def explore():
	
	for g in GEM_LIST:
		extract(g)

#find elements in the gem 
def extract(gem)
	global POTENTIALS
	g_els = []

	for particle in gem: 
		if particle in gem: 
			g_els.append(particle)

	POTENTIALS.append(g_els)

def compare():
	ex = list(POTENTIALS[0])
	non_element = []

	for i in range(N):
		if ex != [] and i+1<N:
			for k in POTENTIALS[0]:
				if k not in POTENTIALS[i+1]:
					if k not in non_element:
						non_element.append(k)
		else:
			for x in non_element: 
				ex.remove(x)

			return ex

explore()
result = compare()
print len(result)


































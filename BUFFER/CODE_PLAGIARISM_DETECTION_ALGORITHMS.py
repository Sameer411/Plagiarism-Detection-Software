from difflib import SequenceMatcher
def code_preprocessor(string_list):
	return string_list

def Rabin_Karp_hash_function(string):
	last_hash=0;
	for i in range(len(string)):
		if i != (len(string)-1):
			last_hash=((last_hash+ord(string[i]))*256)
			last_hash%=101
		else:
			last_hash=(last_hash+ord(string[i]))%101
	return last_hash

def Levenshtein_distance(t,tl,r,rl):
	cost=0
	if tl == 0 or rl == 0:
		return 0
	if t[tl-1] == r[rl-1]:
		cost=0
	else:
		cost=1
	return min(Levenshtein_distance(t,tl-1,r,rl)+1,Levenshtein_distance(t,tl,r,rl-1)+1,Levenshtein_distance(t,tl-1,r,rl-1)+cost)

#############################################################################################################################
def string_matching(test_address,reference_address):
	file = open(test_address,'r')
	temp = file.read()
	test_strings = temp.split('\n')
	file = open(reference_address,'r')
	temp = file.read()
	reference_strings = temp.split('\n')
	lines=[]

	for i in range(len(test_strings)):
		test_hash = Rabin_Karp_hash_function(test_strings[i])
		for j in range(len(reference_strings)):
			if len(test_strings[i])<=len(reference_strings[j]):
				for k in range(len(reference_strings[j])-len(test_strings[i])+1):
					reference_string = reference_strings[j]
					reference_string=reference_string[k:(k+len(test_strings[i])+1)]
					reference_hash = Rabin_Karp_hash_function(reference_string)
					if test_hash == reference_hash:
						if reference_string == test_strings[i]:
							lines.append((i,j))
			else:
				continue

	test_strings = code_preprocessor(test_strings)
	reference_strings = code_preprocessor(reference_strings)
	"""
	for i in range(len(test_strings)):
		print(test_string[i])
	for i in range(len(reference_strings)):
		print(reference_string[i])

	for i in range(len(test_strings)):
		test_hash = Rabin_Karp_hash_function(test_strings[i])
		for j in range(len(reference_strings)):
			if len(test_strings[i])<=len(reference_strings[j]):
				for k in range(len(reference_strings[j])-len(test_strings[i])+1):
					reference_string = reference_strings[j]
					reference_string=reference_string[k:(k+len(test_strings[i])+1)]
					reference_hash = Rabin_Karp_hash_function(reference_string)
					if test_hash == reference_hash:
						if reference_string == test_strings[i]:
							lines.append((i,j))
			else:
				continue
	"""
	"""
		LEVENSHTEIN DISTANCE FORMULA

	similarity=0
	distance=0;
	for i in range(len(test_strings)):
		test_string_tokens = test_strings[i].split(" ")
		for j in range(len(reference_strings)):
			reference_string_tokens = reference_strings[j].split(" ")
			for k in range(len(test_string_tokens)):
				for l in range(len(reference_string_tokens)):
					distance=Levenshtein_distance(test_string_tokens[k],len(test_string_tokens[k]),reference_string_tokens[l],len(reference_string_tokens[l]))
					similarity = ((len(test_string_tokens[k])-distance)/len(test_string_tokens[k]))
					print("COMPARING",test_string_tokens[k],"  ",reference_string_tokens[l],"\tSIMILARITY:",similarity)
	"""

	return lines
#############################################################################################################################
def tokenization(test_address,reference_address):
	file = open(test_address,'r')
	temp = file.read()
	test_strings = temp.split('\n')
	file = open(reference_address,'r')
	temp = file.read()
	reference_strings = temp.split('\n')
	lines=[]
	similarity=0;
	flag=0;

	for i in range(len(test_strings)):
		for j in range(len(reference_strings)):
			similarity=0
			matches=0
			test_string_tokens = test_strings[i].split(" ")

			#print(test_string_tokens)
			for x in range(len(test_string_tokens)):
				if test_string_tokens[x]==" ":
					test_string_tokens = test_string_tokens.remove(" ")
			for k in range(len(test_string_tokens)):
				#print("CHECKING ",test_string_tokens[k])
				reference_string_tokens = reference_strings[j].split(" ")
				for x in range(len(reference_string_tokens)):
					if reference_string_tokens[x]==" ":
						reference_string_tokens = reference_string_tokens.remove(" ")
				for l in range(len(reference_string_tokens)):
					if len(test_string_tokens[k])==len(reference_string_tokens[l]):
						#print("COMPARING ",test_string_tokens[k]," ",reference_string_tokens[l])
						if test_string_tokens[k]==reference_string_tokens[l]:
							"""
							for m in range(len(reference_string_tokens[l])-len(test_string_tokens[k])+1):
							flag=0;
							reference_string_token=reference_string_tokens[l]
							reference_string_token=reference_string_token[m:(m+len(test_string_tokens[k]))]
							#print("COMPARING ",test_string_tokens[k]," ",reference_string_token)
							if test_string_tokens[k]==reference_string_token:
							"""
							matches+=1
							break
							#print("MATCHED ",test_string_tokens[k]," ",reference_string_token)
			if matches>=len(test_string_tokens):
				matches=len(test_string_tokens)
		#	print("TEST ",i+1," REFERNCE ",j+1,"MATCHES: ",matches," LEN ",len(test_string_tokens))
			similarity=(matches/len(test_string_tokens))
			#print(similarity)
			if similarity>=0.69:
				#print("TEST ",i+1," REFERNCE ",j+1," SIMILARITY ",similarity)
				lines.append((i,j))
	#print(lines)
	return lines
#############################################################################################################################
def sequenceMatch(test_address,reference_address):
	with open(test_address) as file_1,open(reference_address) as file_2:
		file1_data = file_1.read()
		file2_data = file_2.read()
		similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
		print(similarity_ratio*100)
#############################################################################################################################
def program_dependancy_graph():
	print("PROGRAM DEPENDANCY GRAPH ALOGORITHM")
#############################################################################################################################
def metrics():
	print("METRICS MATCHING ALOGORITHM")

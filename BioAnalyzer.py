

#uses bio string to attempt to determine the political party that the tweeter belongs to
def LeftOrRight(string):
	stringToSearch = string.lower()
	index = 0
	LKeywords = ["resist","democrat","bernie","kamala","warren","notmypresident","lgbtq","blacklivesmatter","feelthebern","black lives matter","feel the bern","feminist","progressive","beto","obama","biden","dnc","metoo","impeach"]
	RKeywords = ["trump2020","nra","gop","maga","make america great again","2a","2ndamendment","conservative","wall","fake news","keep america great","prolife","pro-life","kag","americafirst", "america first","no collusion", "nocollusion"]
	
	#attempt to sumulate a 'specturm'
	for word in LKeywords:
		if word in stringToSearch:
			index -= 1
	for word in RKeywords:
		if word in stringToSearch:
			index += 1
	if index < 0:
		return "L"
	if index == 0:
		return "N"
	if index > 0:
		return "R"

def main():

	file = open("TwitterNodes.csv", "r")
	lefties = []
	righties = []
	neutralies = []
	for line in file:
		id = -1
		delim = True
		string = ""
		for char in line:
			string += char
			if (char ==',') and delim:
				string = string[:-1]
				delim = False
				id = int(string)
				string = ""
		party = LeftOrRight(string)

		if party == "L":
			lefties.append(id)
		elif party == "R":
			righties.append(id)
		else:
			neutralies.append(id)
	#print into format needed for gephi
	for i in range(len(lefties)):
		for j in range(i,len(righties)):
			print(str(lefties[i])+","+str(lefties[j]))


main()

#tweet class
class Tweet:
    def __init__(self, id, date, party):
        self.id = id
        self.date = date
        self.party = party


#organizes tweets from csv file and sorts them into groups based on date posted
reds = []
blues = []


file = open("TwitterNodesedges.csv","r")
for line in file:
	commacount = 0
	string = ""
	id = ""
	date = ""
	party = ""
	for char in line:
		string += char
		if (char == ","): 
			commacount += 1  
			string = string[:-1]
			if commacount == 1:
				id = string
				string = ""
			elif commacount == 2:
				date = string
				string = ""

	party = string

	t = Tweet(id,date,party)
	if t.party == "R\n":
		reds.append(t)
	if t.party == "L\n":
		blues.append(t)

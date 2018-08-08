pop = []
jpop = []

def collect_songs():
	song = "Type a music:"
	ask = "Type p or j. Type q to finish:"

	while True:
		genre = input(ask)
		if genre == "q":
			break

		if genre == "p":
			p = input(song)
			pop.append(p)

		elif genre == "j":
			j = input(song)
			jpop.append(j)

		else:
			print("inccorect value.")

	print("pop songs: ", pop)
	print("jpop songs: ", jpop)

collect_songs()

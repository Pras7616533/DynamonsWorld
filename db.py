#./db.py
import os

DB_File = "./db.txt"

def save_data(data):
	with open("./db_test.txt","w") as f:
		for type in data["type"].items():
			dimlist = list(data["type"][type[0]].keys())+list(data["type"][type[0]].values())
			f.write(f"Type.{type[0]}.{dimlist[0]}.{dimlist[2]}.{dimlist[1]}.{dimlist[3]}\n")
		for attack in data["attack"].items():
			dimlist = list(data["attack"][attack[0]].keys())+list(data["attack"][attack[0]].values())
			f.write(f"Attack.{attack[0]}.{dimlist[0]}.{dimlist[1]}\n")

	print("Data save")

def load_data():
	data = {
		"type": {
			"fire": {},
			"grass": {},
			"electric": {},
			"water": {},
			"dark": {}
		},
		"attack": {
			"normal": {},
			"fire": {},
			"grass": {},
			"electric": {},
			"water": {},
			"dark": {}
		}
	}

	if not os.path.exists(DB_File):
		return data

	with open(DB_File,"r") as file:
		for line in file:
			part = line.lower().strip().split(".")
			if part[0] == "type":
				data["type"][part[1]][part[2]] = part[3]
				data["type"][part[1]][part[4]] = part[5]

			elif part[1] == "normal":
				data["attack"]["normal"][part[2]] = part[3]

			elif part[1] == "fire":
				data["attack"]["fire"][part[2]] = part[3]

			elif part[1] == "grass":
				data["attack"]["grass"][part[2]] = part[3]

			elif part[1] == "electric":
				data["attack"]["electric"][part[2]] = part[3]

			elif part[1] == "water":
				data["attack"]["water"][part[2]] = part[3]

			elif part[1] == "dark":
				data["attack"]["dark"][part[2]] = part[3]


	print("Data loaded!... ")
	return data

if __name__ == "__main__":
	save_data(load_data())
	print(load_data())

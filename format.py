import db

def display_data(data):
	wish = input("Enter your wish (TYPE, ATTACK): ").lower()
	type = input("Enter the Type of Dynamons: ").lower()
	for Typing in data[wish][type].items():
		print(f"{Typing[0]} = {Typing[1]} ".upper())


def write_data(data):
	wish = input("Enter your wish (TYPE, ATTACK): ").lower()
	type = input("Enter the Type of Dynamons: ").lower()
	

if __name__ == "__main__":
	pass

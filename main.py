import db
import format as f

def main():
	data = db.load_data()
#	f.display_data(data)
	f.write_data(data)

if __name__ == "__main__":
	main()

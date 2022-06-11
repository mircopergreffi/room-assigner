
import yaml

def main():

	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)

	leaderboard = {}

	for m in config['preferences']:
		for member in config['preferences'][m]:
			points = config['preferences'][m][member]
			if member in leaderboard:
				leaderboard[member] = leaderboard[member] + points
			else:
				leaderboard[member] = points
	
	leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

	print(leaderboard)

if __name__ == "__main__":
	main()
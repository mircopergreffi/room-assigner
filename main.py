
from itertools import permutations, islice
import yaml

def config_check(config):
	if config['sum_of_beds'] < config['number_of_members']:
		print('Not enough beds for all members')
		return False
	return True

def calcualte_preference(permutation, config):
	pref = 0
	for room in permutation:
		for member1 in room:
			if not member1 in config['preferences']:
				pref += config['points_per_person']
				continue
			for member2 in room:
				if member1 == member2:
					continue
				if not member2 in config['preferences'][member1]:
					continue
				pref += config['preferences'][member1][member2]
	return pref

def main():
	
	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)
	
	config['sum_of_beds'] = sum(config['rooms'])
	config['number_of_members'] = len(config['members'])

	if not config_check(config):
		exit()
	
	# Generate all permutations
	perms = permutations(config['members'], config['number_of_members'])
	# Split the permutations into rooms
	perms = [iter(perm) for perm in perms]
	perms = [[list(islice(perm, room)) for room in config['rooms']] for perm in perms]
	# Sort all room alfabetically
	perms = [[sorted(room) for room in perm] for perm in perms]
	# Remove duplicates
	perms = [i for n,i in enumerate(perms) if i not in perms[:n]]

	prefs = [calcualte_preference(perm, config) for perm in perms]

	zipped = list(zip(perms, prefs))
	zipped.sort(key=lambda x: x[1], reverse=True)

	# Print the best permutation
	print('Best permutation:')
	for room in zipped[0][0]:
		print(room)
	print('With preference score:', zipped[0][1])

	print()

	# Print the worst permutation
	print('Worst permutation:')
	for room in zipped[-1][0]:
		print(room)
	print('With preference score:', zipped[-1][1])

	print()

	# Print all permutations
	for z in zipped:
		print(z)

if __name__=="__main__":
    main()
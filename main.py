
from itertools import permutations, islice
import yaml

def config_check(config):
	# Check if the number of beds is sufficient for the number of members
	if config['sum_of_beds'] < config['number_of_members']:
		print('ERROR: Not enough beds for all members')
		return False
	# Check if the preferences are valid
	for member in config['preferences']:
		for m in config['preferences'][member]:
			if (member == m):
				print('ERROR: Member', member, 'has a preference to itself')
				return False
			p = config['preferences'][member][m]
			if p < 0:
				print('ERROR: Member', member, 'has negative preference for', m)
				return False
			if p > config['number_of_members'] + 1:
				print('ERROR: Member', member, 'has preference for ', m, 'which is too high')
				return False
		if sum(config['preferences'][member].values()) < (config['number_of_members'] - 1) * config['points_per_person']:
			print('Warning: Member', member, 'has sum of preferences below maximum')
	return True

def calcualte_preference(permutation, config):
	pref = 0
	for room in permutation:
		for member1 in room:
			for member2 in room:
				if member1 == member2:
					continue
				if not member1 in config['preferences']:
					pref = pref + config['points_per_person']
					continue
				if not member2 in config['preferences'][member1]:
					continue
				pref = pref + config['preferences'][member1][member2]
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

	print()

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
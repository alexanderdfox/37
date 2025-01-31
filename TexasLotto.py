import math

# Function to calculate combinations (n choose k)
def combinations(n, k):
	return math.comb(n, k)

# Function to calculate the probability of winning with a given number of tickets
def probability_of_winning(odds, num_tickets):
	# Probability of not winning with a single ticket
	probability_not_winning = (odds - num_tickets) / odds
	# Probability of winning at least once with num_tickets
	probability_winning = 1 - probability_not_winning ** num_tickets
	return probability_winning

# Function to calculate the probability of getting at least one 3 or 7 in 6 numbers
def probability_of_getting_3_or_7(num_tickets):
	# Total numbers to choose from (1-54), numbers containing 3 or 7: 3, 7, 13, 17, 23, 27, 33, 37, 43, 47 (10 numbers)
	total_numbers = 54
	numbers_with_3_or_7 = 10
	remaining_numbers = total_numbers - numbers_with_3_or_7  # 44 numbers without 3 or 7
	
	# Total number of ways to choose 6 numbers from 54
	total_combinations = combinations(total_numbers, 6)
	
	# Number of ways to choose 6 numbers without any 3 or 7
	combinations_without_3_or_7 = combinations(remaining_numbers, 6)
	
	# Probability of not getting any 3 or 7 in a single ticket
	probability_not_getting_3_or_7 = combinations_without_3_or_7 / total_combinations
	
	# Probability of getting at least one 3 or 7 in a single ticket
	probability_getting_3_or_7 = 1 - probability_not_getting_3_or_7
	
	# Probability of getting at least one 3 or 7 with num_tickets
	probability_getting_3_or_7_with_tickets = 1 - (probability_not_getting_3_or_7 ** num_tickets)
	
	return probability_getting_3_or_7_with_tickets

# Function to calculate the probability of getting at least one set of 3 consecutive numbers
def probability_of_getting_3_consecutive(num_tickets):
	total_numbers = 54
	valid_consecutive_sets = 52  # Possible sets of three consecutive numbers: 1-2-3, 2-3-4, ..., 52-53-54
	
	# Total number of ways to choose 6 numbers from 54
	total_combinations = combinations(total_numbers, 6)
	
	# Number of ways to choose 6 numbers containing at least one sequence of 3 consecutive numbers
	combinations_with_consecutive = valid_consecutive_sets * combinations(51, 3)  # 3 consecutive + 3 more from remaining 51 numbers
	
	# Probability of getting at least one set of 3 consecutive numbers in a single ticket
	probability_getting_consecutive = combinations_with_consecutive / total_combinations
	
	# Probability of getting at least one set of 3 consecutive numbers with num_tickets
	probability_getting_consecutive_with_tickets = 1 - ((1 - probability_getting_consecutive) ** num_tickets)
	
	return probability_getting_consecutive_with_tickets

# Odds of winning for different prize tiers
odds_of_winning = {
	"Jackpot (6/6)": 25827165,
	"5/6 ($2,000)": 89678,
	"4/6 ($50)": 1526,
	"3/6 ($3)": 75
}

# Number of tickets purchased
num_tickets = 82

# Calculate the probability of winning with 82 tickets, getting at least one 3 or 7, and getting at least one set of 3 consecutive numbers
for prize, odds in odds_of_winning.items():
	prob_of_winning = probability_of_winning(odds, num_tickets)
	prob_of_getting_3_or_7 = probability_of_getting_3_or_7(num_tickets)
	prob_of_getting_consecutive = probability_of_getting_3_consecutive(num_tickets)
	
	print(f"For {prize}, with {num_tickets} tickets:")
	print(f"The probability of winning is: {prob_of_winning:.8f}")
	print(f"The odds of winning are approximately 1 in {1 / prob_of_winning:.0f}")
	print(f"The probability of getting at least one 3 or 7 is: {prob_of_getting_3_or_7:.8f}")
	print(f"The odds of getting at least one 3 or 7 are approximately 1 in {1 / prob_of_getting_3_or_7:.0f}")
	print(f"The probability of getting at least one set of 3 consecutive numbers is: {prob_of_getting_consecutive:.8f}")
	print(f"The odds of getting at least one set of 3 consecutive numbers are approximately 1 in {1 / prob_of_getting_consecutive:.0f}")
	print()

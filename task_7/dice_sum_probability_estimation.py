import numpy as np

DICE_SIDES = np.arange(1, 7)

def throw_dice(dice_count: int, num_of_rolls: int) -> np.ndarray:
    """
    Throwing dice multiple times
    Args:
        dice_count (int): The number of dice
        num_of_rolls (int): The number of rolls (experiments)
    """
    return np.random.choice(np.arange(1, 7), size=(num_of_rolls, dice_count))



def get_dice_sum_probability(sum: int, num_of_rolls: int, dice_count=2) -> float:
    """
    Using Monte Carlo method to calculate the probability of getting a certain sum when a given number of dice are thrown
    Args:
        sum (int): The target sum
        num_of_rolls (int): The number of rolls (experiments)
        dice_count (int, optional): The number of dice. Defaults to 2.
    """
    rolls = throw_dice(dice_count, num_of_rolls)
    rolls_sum = np.sum(rolls, axis=1)
    rolls_with_sum = np.count_nonzero(rolls_sum == sum)

    return rolls_with_sum / num_of_rolls


def estimate_probability(sum: int, num_experiments: int, num_of_rolls: int, dice_count=2) -> float:
    """
    Estimates the probability of getting a certain sum when a given number of dice are thrown
    Args:
        sum (int): The target sum
        num_of_rolls (int): The number of rolls (experiments)
        dice_count (int, optional): The number of dice. Defaults to 2.
    """
    total = 0 
    for _ in range(num_experiments):
        total += get_dice_sum_probability(sum, num_of_rolls, dice_count)
    return total / num_experiments


def run_experiment(num_of_rolls: int,  num_executions: int, dice_count=2) -> float:
    """
    Runs an experiment
    Args:
        sum (int): The target sum
        num_of_rolls (int): The number of rolls (experiments)
        num_executions (int): The number of executions
        dice_count (int, optional): The number of dice. Defaults to 2.
    """
    sums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    experiment_result = {sum: 0 for sum in sums}
    for sum in sums:
        experiment_result[sum] = round(estimate_probability(sum, num_executions, num_of_rolls) * 100, 2)
    print(experiment_result)
    return experiment_result
    

def main():
    num_of_rolls = [100, 1000, 10000]
    num_experiments = [100, 1000, 10000, 100000]
    results = {}
    for rolls in num_of_rolls:
        for experiments in num_experiments:
            print("=======================================")
            print(f"Number of rolls: {rolls}, Number of experiments: {experiments}")
            results[(rolls, experiments)] = run_experiment(7, rolls, experiments)
    
    # printing the results as a table
    print(f"\n|{'Rolls':<5} | {'Exper':<6} | {'Sum=2':<5} | {'Sum=3':<5} | {'Sum=4':<5} | {'Sum=5':<5} | {'Sum=6':<5} | {'Sum=7':<5} | {'Sum=8':<5} | {'Sum=9':<5} | {'Sum=10':<6} | {'Sum=11':<6} | {'Sum=12':<6}|")
    print(f"|{'-'*5:<5} | {'-'*5:<6} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<5} | {'-'*5:<6} | {'-'*5:<6} | {'-'*5:<6}|")
    for key, value in results.items():
        print(f"|{key[0]:<5} | {key[1]: <6} | {value[2]:<5} | {value[3]:<5} | {value[4]:<5} | {value[5]:<5} | {value[6]:<5} | {value[7]:<5} | {value[8]:<5} | {value[9]:<5} | {value[10]:<6} | {value[11]:<6} | {value[12]:<6}|")
if __name__ == "__main__":
    main()

import random
import time

def weighted_choice(probabilities):
    if sum(probabilities) != 1:
        raise ValueError("Probabilities must sum to 1.")
    cummulative_probabilities = []
    r = random.random()
    print(f"Random number generated: {r}")
    for i, p in enumerate(probabilities):
        cummulative_probabilities.append(sum(probabilities[:i+1]))
    for i in range(len(cummulative_probabilities)):
        if r < cummulative_probabilities[i]:
            return i

def main():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    print("\nWeighted random choices:")
    probabilities = [0.5, 0.3, 0.2]
    choices = ['Apple', 'Banana', 'Cherry']
    print(f"\nChoices and their probabilities for selection: {probabilities}")
    for _ in range(10):
        time.sleep(1.2)
        print()
        choice_index = weighted_choice(probabilities)
        print(f"{choices[choice_index]}\t- Probability: {probabilities[choice_index]*100}%")
    
    print("\n-------------------------------")
    
    probabilities = [0.1, 0.1, 0.8]
    print(f"\nChoices and their probabilities for selection: {probabilities}")
    for _ in range(10):
        time.sleep(1.2)
        print()
        choice_index = weighted_choice(probabilities)
        print(f"{choices[choice_index]}\t- Probability: {probabilities[choice_index]*100}%")
    #print(f"{RESET}")

if __name__ == "__main__":
    main()


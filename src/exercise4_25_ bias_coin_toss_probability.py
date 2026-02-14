import random
import time

def biased_coin_toss(p) -> int:
    return 0 if random.random() < p else 1

def main():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    print("\nTossing a coin 10 times using a biased coin (70% heads)...")
    p = 0.7
    for i in range(10):
        time.sleep(1.2)
        print(f"Toss #{i+1}: {GREEN + 'HEAD' + RESET if biased_coin_toss(p) == 0 else RED + 'TAIL' + RESET}")

    print("\nTossing a coin 10 times using a biased coin (30% heads)...")
    p = 0.3
    for i in range(10):
        time.sleep(1.2)
        print(f"Toss #{i+1}: {GREEN + 'HEAD' + RESET if biased_coin_toss(p) == 0 else RED + 'TAIL' + RESET}")

if __name__ == "__main__":
    main()

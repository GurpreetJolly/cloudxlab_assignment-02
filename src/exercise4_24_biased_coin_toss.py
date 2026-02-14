import random
import time

def biased_coin_toss() -> int:
    return 0 if random.random() < 0.7 else 1

def main():
    RED = '\033[31m'
    GREEN = '\033[32m'
    RESET = '\033[0m'
    print("\nTossing a coin 20 times using a biased coin (70% heads)...")
    for i in range(20):
        time.sleep(1.2)
        print(f"Toss #{i+1}: {GREEN + 'HEAD' + RESET if biased_coin_toss() == 0 else RED + 'TAIL' + RESET}")

if __name__ == "__main__":
    main()

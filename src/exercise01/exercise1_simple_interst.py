import logging

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger(__name__)

def calculate_interest(principal: float, rate: float, time: float) -> float:
    _logger.debug(f"Calculating interest for principal={principal}, rate={rate}%, time={time}yr.")
    interest = (principal * rate * time) / 100
    _logger.debug(f"Calculated interest: {interest}")
    return interest

def main():
    print ("\n*** Calculate simple interest ***")
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (in percentage): "))
    t = float(input("Enter time in years: "))

    interest = calculate_interest(p, r, t)
    print(f"The simple interest for principal {p}, rate of {r}%, for {t} years is: {interest}")

if __name__ == "__main__":
    main()

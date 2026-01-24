def solve_hanoi(n, source, target, auxiliary, moves=None):
    if moves is None:
        moves = []

    if n == 1:
        moves.append((source, target))
        print(f"Moving disk {n} from {source} to {target}")
    else:
        solve_hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        print(f"Moving disk {n} from {source} to {target}")
        solve_hanoi(n - 1, auxiliary, target, source, moves)

    return moves

def main():
    print("\n*** Tower of Hanoi Solver ***")
    # n = int(input("Enter the number of disks: "))

    moves = solve_hanoi(64, 'A', 'C', 'B')
    print(f"Returns: {len(moves)}")
    # print(f"\nThe solution for {n} disks is:")
    # for i, move in enumerate(moves, start=1):
    #     print(f"Move {i}: from {move[0]} to {move[1]}")

if __name__ == "__main__":
    main()

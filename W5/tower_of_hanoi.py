import time

NumberofMoves = 0
# TowerOfHanoi.py
def main():
    n = eval(input("Enter number of disks: "))
    
    # Find the solution recursively
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')

# The function for finding the solution to move n disks
# from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global NumberofMoves
    if n == 1: # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)

        NumberofMoves += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        moveDisks(n - 1, auxTower, toTower, fromTower)        
        
        NumberofMoves += 1
main() # Call the main function

print(f"Total number of moves: {NumberofMoves}")

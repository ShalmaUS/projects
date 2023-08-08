from pythonProjects.alien import Alien
import random
import time

def new_aliens_collection(position_data):
    return [Alien(x, y) for (x, y) in position_data]

def print_game_board(aliens, player_x, player_y, player_icon,player_name, player_health, recovery_point):
    max_x = max(max(alien.x for alien in aliens), player_x) if aliens else player_x
    max_y = max(max(alien.y for alien in aliens), player_y) if aliens else player_y

    for y in range(max_y + 1):
        row = ""
        for x in range(max_x + 1):
            if x == player_x and y == player_y:
                row += player_icon + " "
            elif x == recovery_point[0] and y == recovery_point[1]:
                row += "+ "
            else:
                alien_at_location = next((alien for alien in aliens if alien.x == x and alien.y == y), None)
                if alien_at_location:
                    row += f"A "
                else:
                    row += ". "
        print(row)

    print(f"\n{player_name}'s Health: {player_health}")

def main():
    player_name = input("Enter your name: ")
    player_icon = player_name[0].upper()
    player_health = 3
    recovery_point = (random.randint(1, 10), random.randint(1, 10))
    print("-------------------------------------------------------------------------------------------------------")
    print(f"                            Welcome to Darthvader's War, {player_name}!!")
    print("-------------------------------------------------------------------------------------------------------")
    player_x, player_y = 0, 0
    aliens_data = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(5)]
    aliens = new_aliens_collection(aliens_data)

    while player_health > 0:
        print_game_board(aliens, player_x, player_y, player_icon,player_name, player_health, recovery_point)

        action = input("Enter 'w' for up, 'a' for left, 's' for down, 'd' for right, 'q' to quit, 'h' to shoot, or 'r' to heal: ")
        if action == 'q':
            print("Game Over. Thanks for playing!")
            break
        elif action in ['w', 'a', 's', 'd']:
            new_x, new_y = player_x, player_y
            if action == 'w':
                new_y -= 1
            elif action == 'a':
                new_x -= 1
            elif action == 's':
                new_y += 1
            elif action == 'd':
                new_x += 1

            if 0 <= new_x <= 10 and 0 <= new_y <= 10:
                player_x, player_y = new_x, new_y
            else:
                print("Invalid move. You can't go beyond the game boundaries.")
            
            for alien in aliens:
                if abs(alien.x - player_x) <= 1 and abs(alien.y - player_y) <= 1:
                    print("An alien attacked you!")
                    player_health -= 1
                    break

        elif action == 'h':
            alien_to_shoot = None
            for alien in aliens:
                if abs(alien.x - player_x) <= 1 and abs(alien.y - player_y) <= 1:
                    alien_to_shoot = alien
                    break
            
            if alien_to_shoot:
                print("You shot an alien!")
                alien_to_shoot.hit()
                if not alien_to_shoot.is_alive():
                    aliens.remove(alien_to_shoot)
                    print("You defeated an alien!")
            else:
                print("No aliens adjacent to you to shoot.")
        
        elif action == 'r':
            if player_x == recovery_point[0] and player_y == recovery_point[1]:
                print("You are healing...")
                time.sleep(1) 
                player_health = min(3, player_health + 1)
                print("You are fully healed!")

        if player_health <= 0:
            print("Game Over. You are out of health.")
            break

        if not aliens:
            print("Congratulations! You've defeated all the aliens.")
            break

if __name__ == "__main__":
    main()

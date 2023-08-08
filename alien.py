class Alien:
    total_aliens_created = 0

    def __init__(self, x, y, health=3):
        self.x = x
        self.y = y
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Robot:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = "N"  # N, E, S, W

    def move_forward(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def turn_left(self):
        directions = ["N", "W", "S", "E"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def turn_right(self):
        directions = ["N", "E", "S", "W"]
        self.direction = directions[(directions.index(self.direction) + 1) % 4]

    def status(self):
        print(f"Robot: {self.name}")
        print(f"Position: ({self.x}, {self.y})")
        print(f"Direction: {self.direction}")


# ---- Simulation ----
r1 = Robot("Robo1")

r1.move_forward()
r1.turn_right()
r1.move_forward()
r1.move_forward()
r1.turn_left()
r1.move_forward()
r1.turn_right()
r1.status()

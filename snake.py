class BodyPart(object):
    def __init__(self, pos):
        self.pos = pos

        
class Snake(object):
    def __init__(self, grid, starting_pos, starting_direction, body_part_count, color_b, color_f):
        self.grid = grid
        self.pos = starting_pos
        if starting_direction < 0 or starting_direction > 3:
            print("Invalid direction")
            exit()
        self.direction = int(starting_direction) # 0, 1, 2, 3 for East, North, West, South
        self.body_part_count = body_part_count
        self.color_b = color_b
        self.color_f = color_f
        self.body = []
        self.last_pos = None

        self.create_body()

    def create_body(self):
        self.head = BodyPart(self.pos)
        self.body.append(self.head)
        for i in range(1, self.body_part_count + 1):
            self.body.append(BodyPart([self.pos[0] - self.grid.boxsize * i, self.pos[1]]))

    def move(self):
        self.last_pos = self.body[-1].pos
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].pos = self.body[i-1].pos.copy()

        if self.direction == 0: self.head.pos[0] += self.grid.boxsize
        elif self.direction == 1: self.head.pos[1] -= self.grid.boxsize
        elif self.direction == 2: self.head.pos[0] -= self.grid.boxsize
        else: self.head.pos[1] += self.grid.boxsize

        self.check_for_collision()


    def check_for_collision(self):
        for body_part in self.body[1:]:
            if body_part.pos[0] == self.head.pos[0] and body_part.pos[1] == self.head.pos[1]:
                self.grid.application.game_over()

        if self.head.pos[0] > (self.grid.cols - 1) * self.grid.boxsize or self.head.pos[0] < 0 or self.head.pos[1] < 0 or self.head.pos[1] > (self.grid.rows - 1) * self.grid.boxsize:
            self.grid.application.game_over()

        # check for apple collision
        if self.head.pos[0] == self.grid.apple.pos[0] and self.head.pos[1] == self.grid.apple.pos[1]:
            self.grid.application.score += 1
            self.grid.spawn_apple()
            self.body.append(BodyPart(self.last_pos.copy()))

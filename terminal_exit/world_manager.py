"""Simple world manager with a couple of demo rooms and movement."""


class Room:
    def __init__(self, name, description, options=None, neighbors=None, coord=(0, 0)):
        self.name = name
        self.description = description
        self.options = options or []
        self.neighbors = neighbors or {}
        self.coord = coord
        self.visited = False


class WorldManager:
    def __init__(self):
        # minimal demo map with coordinates
        self.rooms = {}
        self._build_demo()
        self.current_room = self.rooms['Awakening Point']
        self.current_room.visited = True

    def _build_demo(self):
        # Coordinates chosen so that "north" appears above on the minimap
        a = Room('Awakening Point', 'A dim corridor with flickering symbols.', ['Go North', 'Examine Wall'], coord=(0, 1))
        b = Room('Void Corridor', 'A longer hallway; the lights glitch in waves.', ['Go South', 'Go East', 'Examine Console'], coord=(0, 0))
        c = Room('Junction', 'A junction with several paths. A humming sound comes from the East.', ['Go West', 'Go East'], coord=(1, 0))
        a.neighbors = {'north': 'Void Corridor'}
        b.neighbors = {'south': 'Awakening Point', 'east': 'Junction'}
        c.neighbors = {'west': 'Void Corridor'}
        self.rooms[a.name] = a
        self.rooms[b.name] = b
        self.rooms[c.name] = c

    def move(self, direction):
        dir_key = direction.lower()
        cur = self.current_room
        if dir_key in cur.neighbors:
            self.current_room = self.rooms[cur.neighbors[dir_key]]
            self.current_room.visited = True
        else:
            print('You cannot go that way.')

    def render_minimap(self):
        # build small bounding box from existing coords
        coords = [r.coord for r in self.rooms.values()]
        xs = [c[0] for c in coords]
        ys = [c[1] for c in coords]
        minx, maxx = min(xs), max(xs)
        miny, maxy = min(ys), max(ys)
        rows = []
        for y in range(miny, maxy + 1):
            row = ''
            for x in range(minx, maxx + 1):
                found = None
                for r in self.rooms.values():
                    if r.coord == (x, y):
                        found = r
                        break
                if found is None:
                    row += '   '
                else:
                    if self.current_room is found:
                        row += ' P '
                    elif found.visited:
                        row += ' . '
                    else:
                        row += ' ? '
            rows.append(row)
        # return string lines
        header = 'MINIMAP'
        return [header] + rows

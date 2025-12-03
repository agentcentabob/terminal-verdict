"""World management with zones and interactive rooms."""


class Room:
    """Represents a single room/location."""
    def __init__(self, name, description, options=None, neighbors=None, coord=(0, 0), zone='awakening'):
        self.name = name
        self.description = description
        self.options = options or []
        self.neighbors = neighbors or {}
        self.coord = coord
        self.zone = zone
        self.visited = False
        self.examined_objects = {}  # Track what's been examined
        self.items = []  # Items available in this room


class WorldManager:
    """Manages the game world structure."""
    def __init__(self):
        self.rooms = {}
        self._build_world()
        self.current_room = self.rooms['Awakening Point']
        self.current_room.visited = True

    def _build_world(self):
        """Build the game world structure."""
        
        # AWAKENING POINT - Entry zone, safe area for learning
        awakening = Room(
            'Awakening Point',
            'You stand in a dim corridor. Flickering symbols line corroded walls.\nThe air hums with energy. This is where you woke up.',
            ['Go North', 'Examine Wall', 'Examine Floor'],
            coord=(0, 2),
            zone='awakening'
        )
        
        # VOID CORRIDOR - First exploration area
        void = Room(
            'Void Corridor',
            'The corridor stretches deeper. Lights flicker in waves.\nA corrupted console pulses with faint light in the shadows.',
            ['Go South', 'Go East', 'Examine Console', 'Examine Symbols'],
            coord=(0, 1),
            zone='awakening'
        )
        
        # JUNCTION - Branching path
        junction = Room(
            'Junction',
            'Multiple paths meet here. A humming sound echoes from the East.\nThe air feels different—almost electric.',
            ['Go West', 'Go East', 'Go North', 'Listen'],
            coord=(1, 1),
            zone='awakening'
        )
        
        # DATA RUINS - Second zone, more dangerous
        data_ruins = Room(
            'Data Ruins',
            'Larger chamber filled with broken servers and twisted metal.\nGlowing red error lights pulse like dying heartbeats.',
            ['Go West', 'Go North', 'Examine Servers', 'Look for Items'],
            coord=(2, 1),
            zone='data_ruins'
        )
        
        # PROCESSING DEPTHS - Deeper into the system
        processing = Room(
            'Processing Depths',
            'You descend into chambers of pure machinery. The humming is deafening.\nLiquid drips from above, pooling in strange patterns.',
            ['Go South', 'Go East', 'Examine Machinery'],
            coord=(1, 2),
            zone='processing'
        )
        
        # MEMORY CHAMBER - Lore location
        memory = Room(
            'Memory Chamber',
            'Hundreds of data crystals line the walls, each pulsing with stored information.\nA feeling of profound loneliness fills this space.',
            ['Go West', 'Examine Crystals', 'Search for Records'],
            coord=(2, 2),
            zone='processing'
        )
        
        # Set up connections
        awakening.neighbors = {'north': 'Void Corridor'}
        void.neighbors = {'south': 'Awakening Point', 'east': 'Junction'}
        junction.neighbors = {'west': 'Void Corridor', 'east': 'Data Ruins', 'north': 'Processing Depths'}
        data_ruins.neighbors = {'west': 'Junction', 'north': 'Memory Chamber'}
        processing.neighbors = {'south': 'Junction', 'east': 'Memory Chamber'}
        memory.neighbors = {'south': 'Data Ruins', 'west': 'Processing Depths'}
        
        # Add rooms to world
        for room in [awakening, void, junction, data_ruins, processing, memory]:
            self.rooms[room.name] = room

    def move(self, direction):
        """Move in a direction."""
        dir_key = direction.lower()
        cur = self.current_room
        if dir_key in cur.neighbors:
            self.current_room = self.rooms[cur.neighbors[dir_key]]
            self.current_room.visited = True
        else:
            print('You cannot go that way.')

    def render_minimap(self):
        """Render a minimap of visited areas."""
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
                        row += ' ◉ '  # Current position
                    elif found.visited:
                        row += ' · '  # Visited
                    else:
                        row += ' ? '  # Unvisited
            rows.append(row)
        return rows

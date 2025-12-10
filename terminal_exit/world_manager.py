"""World management with zones and interactive rooms."""


class Room:
    """Represents a single room/location."""
    def __init__(self, name, description, options=None, neighbors=None, coord=(0, 0), zone='awakening', encounter=None):
        self.name = name
        self.description = description
        self.options = options or []
        self.neighbors = neighbors or {}
        self.coord = coord
        self.zone = zone
        self.visited = False
        self.examined_objects = {}  # Track what's been examined
        self.items = []  # Items available in this room
        self.encounter = encounter  # Enemy encounter key
        self.encounter_cleared = False


class WorldManager:
    """Manages the game world structure."""
    def __init__(self):
        self.rooms = {}
        self._build_world()
        self.current_room = self.rooms['Awakening Point']
        self.current_room.visited = True

    def _build_world(self):
        """Build the game world structure with consistent map connections."""
        
        # AWAKENING POINT - Entry zone, safe area for learning
        awakening = Room(
            'Awakening Point',
            'You stand in a dim corridor. Flickering symbols line corroded walls.\nThe air hums with energy. This is where you woke up.',
            ['Examine Wall', 'Examine Floor'],
            coord=(0, 0),
            zone='awakening'
        )
        
        # VOID CORRIDOR - First exploration area
        void = Room(
            'Void Corridor',
            'The corridor stretches deeper. Lights flicker in waves.\nA corrupted console pulses with faint light in the shadows.',
            ['Examine Console', 'Examine Symbols'],
            coord=(0, 1),
            zone='awakening',
            encounter='glitch'
        )
        
        # LOST CHAMBERS - New area, deeper exploration
        lost = Room(
            'Lost Chambers',
            'A vast chamber with broken architecture. Vines of corrupted code crawl across walls.\nEverything here feels abandoned, forgotten.',
            ['Examine Architecture', 'Examine Vines'],
            coord=(1, 1),
            zone='awakening'
        )
        
        # JUNCTION - Branching path
        junction = Room(
            'Junction',
            'Multiple paths meet here. A humming sound echoes from the East.\nThe air feels different—almost electric.',
            ['Examine Paths', 'Listen to Hum'],
            coord=(1, 0),
            zone='awakening'
        )
        
        # DATA RUINS - Second zone, more dangerous
        data_ruins = Room(
            'Data Ruins',
            'Larger chamber filled with broken servers and twisted metal.\nGlowing red error lights pulse like dying heartbeats.',
            ['Examine Servers', 'Examine Metal'],
            coord=(2, 0),
            zone='data_ruins',
            encounter='phantom'
        )
        
        # CORRUPTED VAULT - Hidden chamber
        vault = Room(
            'Corrupted Vault',
            'An imposing chamber with sealed doors. Strange symbols mark everything.\nYou feel the weight of secrets stored here.',
            ['Examine Doors', 'Examine Symbols'],
            coord=(3, 0),
            zone='data_ruins'
        )
        
        # PROCESSING DEPTHS - Deeper into the system
        processing = Room(
            'Processing Depths',
            'You descend into chambers of pure machinery. The humming is deafening.\nLiquid drips from above, pooling in strange patterns.',
            ['Examine Machinery', 'Examine Liquid'],
            coord=(1, 2),
            zone='processing',
            encounter='fragment'
        )
        
        # CORE NEXUS - Central hub
        nexus = Room(
            'Core Nexus',
            'You stand before immense crystalline structures pulsing with power.\nThe air itself seems alive with energy.',
            ['Examine Crystals', 'Feel Energy'],
            coord=(2, 2),
            zone='processing'
        )
        
        # MEMORY CHAMBER - Lore location
        memory = Room(
            'Memory Chamber',
            'Hundreds of data crystals line the walls, each pulsing with stored information.\nA feeling of profound loneliness fills this space.',
            ['Examine Crystals', 'Examine Information'],
            coord=(3, 2),
            zone='processing',
            encounter='echo'
        )
        
        # Set up CONSISTENT bidirectional connections
        awakening.neighbors = {'north': 'Void Corridor'}
        void.neighbors = {'south': 'Awakening Point', 'east': 'Junction', 'north': 'Lost Chambers'}
        lost.neighbors = {'south': 'Void Corridor', 'north': 'Junction'}
        junction.neighbors = {'west': 'Void Corridor', 'east': 'Data Ruins', 'north': 'Processing Depths', 'south': 'Lost Chambers'}
        data_ruins.neighbors = {'west': 'Junction', 'north': 'Memory Chamber', 'east': 'Corrupted Vault'}
        vault.neighbors = {'west': 'Data Ruins'}
        processing.neighbors = {'south': 'Junction', 'east': 'Memory Chamber', 'north': 'Core Nexus'}
        nexus.neighbors = {'south': 'Memory Chamber', 'west': 'Processing Depths'}
        memory.neighbors = {'south': 'Data Ruins', 'west': 'Processing Depths', 'north': 'Core Nexus'}
        
        # Add rooms to world
        for room in [awakening, void, lost, junction, data_ruins, vault, processing, nexus, memory]:
            self.rooms[room.name] = room

    def move(self, direction):
        """Move in a direction using up/down/left/right.
        
        Args:
            direction: 'up', 'down', 'left', or 'right'
            
        Returns:
            tuple: (success: bool, message: str, new_room: Room or None)
        """
        dir_key = direction.lower()
        
        # Map directional input to coordinate changes
        direction_map = {
            'up': (0, -1),      # decrease y
            'down': (0, 1),     # increase y
            'left': (-1, 0),    # decrease x
            'right': (1, 0)     # increase x
        }
        
        if dir_key not in direction_map:
            msg = "Invalid direction. Use: up, down, left, or right."
            return False, msg, None
        
        # Calculate target coordinates
        dx, dy = direction_map[dir_key]
        target_x = self.current_room.coord[0] + dx
        target_y = self.current_room.coord[1] + dy
        target_coord = (target_x, target_y)
        
        # Find room at target coordinate
        target_room = None
        for room in self.rooms.values():
            if room.coord == target_coord:
                target_room = room
                break
        
        if target_room is None:
            msg = "You've hit a wall! There's nothing in that direction."
            return False, msg, None
        
        # Move to the new room
        self.current_room = target_room
        self.current_room.visited = True
        return True, f"You move {direction}...", target_room

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

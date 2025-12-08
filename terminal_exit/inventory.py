"""Inventory and item helpers with better organization."""


class Item:
    def __init__(self, name, desc='', item_type='gear', key=False):
        self.name = name
        self.desc = desc
        self.item_type = item_type  # 'gear', 'upgrade', 'key_item', 'consumable'
        self.key = key  # Can't be discarded if True


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, name, desc='', item_type='gear', key=False):
        """Add an item to inventory."""
        # Auto-detect item type for known items
        if name == 'Health Potion':
            item_type = 'consumable'
        
        item = Item(name, desc, item_type, key)
        self.items.append(item)
        return item
    
    def add(self, item):
        """Add existing item object."""
        self.items.append(item)

    def show(self):
        """Display inventory in a nice format."""
        from .ascii_art import cprint, draw_fancy_box
        
        if not self.items:
            draw_fancy_box('INVENTORY', ['(empty)'], width=60, color='yellow')
            return
        
        # Organize by type
        key_items = [i for i in self.items if i.key]
        upgrades = [i for i in self.items if i.item_type == 'upgrade']
        gear = [i for i in self.items if i.item_type == 'gear' and not i.key]
        consumables = [i for i in self.items if i.item_type == 'consumable']
        
        lines = []
        
        if key_items:
            lines.append('━━ KEY ITEMS ━━')
            for item in key_items:
                lines.append(f'  ✦ {item.name}')
            lines.append('')
        
        if upgrades:
            lines.append('━━ AI UPGRADES ━━')
            for item in upgrades:
                lines.append(f'  ◆ {item.name}')
            lines.append('')
        
        if gear:
            lines.append('━━ GEAR & TOOLS ━━')
            for item in gear:
                lines.append(f'  ▪ {item.name}')
            lines.append('')
        
        if consumables:
            lines.append('━━ CONSUMABLES ━━')
            for item in consumables:
                lines.append(f'  ● {item.name}')
        
        draw_fancy_box('INVENTORY', lines, width=60, color='yellow')


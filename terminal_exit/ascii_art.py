"""ASCII art and lightweight color helpers.

Provides gorgeous Candy Box-style ASCII graphics, large expressive AI faces,
and a cohesive visual design system.
"""
try:
    from colorama import init as _init_colorama, Fore, Style
    _init_colorama()
    COLORAMA_AVAILABLE = True
except Exception:
    COLORAMA_AVAILABLE = False

# GORGEOUS AI FACES - Candy Box style, larger and more expressive
FACES = {
    'happy': [
        '╔══════════════════════╗',
        '║                      ║',
        '║      ^  ◉  ^        ║',
        '║       \\ │ /         ║',
        '║        ◡ ◡ ◡       ║',
        '║                      ║',
        '╚══════════════════════╝',
    ],
    'neutral': [
        '╔══════════════════════╗',
        '║                      ║',
        '║      ◉  ·  ◉        ║',
        '║                      ║',
        '║       ───────       ║',
        '║                      ║',
        '╚══════════════════════╝',
    ],
    'thinking': [
        '╔══════════════════════╗',
        '║                      ║',
        '║      ◉ ‿  ◉        ║',
        '║         ‿           ║',
        '║       ═════════      ║',
        '║        (thinking)    ║',
        '╚══════════════════════╝',
    ],
    'nervous': [
        '╔══════════════════════╗',
        '║                      ║',
        '║      ◉ ~ ◉         ║',
        '║        ~~           ║',
        '║      ~~~~~~~        ║',
        '║                      ║',
        '╚══════════════════════╝',
    ],
    'sad': [
        '╔══════════════════════╗',
        '║                      ║',
        '║      •  ⌢  •       ║',
        '║        ⌢             ║',
        '║      ╭─────╮        ║',
        '║                      ║',
        '╚══════════════════════╝',
    ],
}


SMALL_FACE = {
    'happy': [
        '╔═══════════╗',
        '║  ^   ^   ║',
        '║   \\ /     ║',
        '╚═══════════╝',
    ],
}


# ═══════════════════════════════════════════════════════════════
# GORGEOUS GRAPHICS & LAYOUTS
# ═══════════════════════════════════════════════════════════════

TITLE_BANNER = [
    '╔══════════════════════════════════════════════════════════╗',
    '║                                                          ║',
    '║    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗   ║',
    '║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║   ║',
    '║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║   ║',
    '║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║   ║',
    '║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║   ║',
    '║       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝   ║',
    '║                                                          ║',
    '║                    ██╗███╗  ███╗ ██╗███╗   ███╗███╗███  ║',
    '║                   ███║████╗████║███║████╗ ████║███║███  ║',
    '║                  ██ ██║██╔███╔██║██ ██║██╔███╔██║███║██║  ║',
    '║                 █████║██║╚█╔╝██║█████║██║╚█╔╝██║███║█████║',
    '║                    ██║██║ ╚═╝ ██║    ██║██║ ╚═╝ ██║███║    ║',
    '║                                                          ║',
    '╚══════════════════════════════════════════════════════════╝',
]

def draw_fancy_box(title, lines, width=70, color='cyan', char='═'):
    """Draw a fancy bordered box with title."""
    top = '╔' + char * (width - 2) + '╗'
    title_line = f'║ ▸ {title:<{width-6}} ║'
    divider = '╠' + char * (width - 2) + '╣'
    
    print(_color_wrap(top, color))
    print(_color_wrap(title_line, color))
    print(_color_wrap(divider, color))
    
    for line in lines:
        text = str(line)[:width-4]
        print(_color_wrap(f'║  {text:<{width-4}} ║', color))
    
    print(_color_wrap('╚' + char * (width - 2) + '╝', color))


def draw_banner_box(title, lines, width=70, color='cyan'):
    """Draw a box with banner-style top."""
    top = '▓' * width
    header = f'  ▸ {title}'
    
    print(_color_wrap(top, color))
    print(_color_wrap(header, color))
    print(_color_wrap('▓' * width, color))
    print()
    
    for line in lines:
        text = str(line)
        print(_color_wrap(text, color))
    
    print()
    print(_color_wrap('▓' * width, color))


def draw_scene_box(description, width=70):
    """Draw a scene description box."""
    print()
    print(_color_wrap('╭' + '─' * (width - 2) + '╮', 'magenta'))
    
    # Word wrap description
    words = description.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += word + ' '
        else:
            if current_line:
                lines.append(current_line.strip())
            current_line = word + ' '
    if current_line:
        lines.append(current_line.strip())
    
    for line in lines:
        print(_color_wrap(f'│ {line:<{width-3}}│', 'magenta'))
    
    print(_color_wrap('╰' + '─' * (width - 2) + '╯', 'magenta'))
    print()


def draw_stats_bar(label, value, max_val, width=40, color='green'):
    """Draw a nice stats bar (HP, progress, etc)."""
    bar_width = width - len(label) - 8
    filled = int((value / max_val) * bar_width) if max_val > 0 else 0
    bar = '█' * filled + '░' * (bar_width - filled)
    percent = int((value / max_val) * 100) if max_val > 0 else 0
    line = f'{label:.<15} [{bar}] {percent:>3}%'
    print(_color_wrap(line, color))


def draw_menu(title, options, width=50, color='yellow'):
    """Draw a beautiful menu."""
    print()
    print(_color_wrap('╔' + '═' * (width - 2) + '╗', color))
    print(_color_wrap(f'║ ▶ {title.center(width-5)} ║', color))
    print(_color_wrap('╠' + '═' * (width - 2) + '╣', color))
    
    for i, option in enumerate(options, 1):
        opt_text = f'{i}. {option}'
        print(_color_wrap(f'║  {opt_text:<{width-4}} ║', color))
    
    print(_color_wrap('╚' + '═' * (width - 2) + '╝', color))
    print()


def _color_wrap(text, color_name):
    """Wrap text with color."""
    if not COLORAMA_AVAILABLE:
        return text
    color = getattr(Fore, color_name.upper(), '')
    return f"{color}{text}{Style.RESET_ALL}"


def render_face(state='neutral', large=True):
    """Render the AI face for a given state.

    If `large` is True, uses the larger expressive faces.
    """
    faceset = FACES if large else SMALL_FACE
    face = faceset.get(state, faceset.get('neutral'))
    for line in face:
        print(_color_wrap(line, 'cyan'))


def draw_box(title, lines, width=50, color='white'):
    """Draw a simple box with a title and lines of text.

    Lines will be wrapped/truncated to the width; returns nothing.
    """
    top = '╔' + '═' * (width - 2) + '╗'
    title_line = f'║ {title[:width-4]:^{width-4}} ║'
    print(_color_wrap(top, color))
    print(_color_wrap(title_line, color))
    print(_color_wrap('╠' + '═' * (width - 2) + '╣', color))
    for l in lines:
        # simple clip
        text = l[:width-4]
        print(_color_wrap(f'║ {text:<{width-4}} ║', color))
    print(_color_wrap('╚' + '═' * (width - 2) + '╝', color))


def cprint(text, kind='white'):
    # kind: white, cyan, green, yellow, magenta, red, blue, dim
    kind_map = {
        'white': 'WHITE',
        'cyan': 'CYAN',
        'green': 'GREEN',
        'yellow': 'YELLOW',
        'magenta': 'MAGENTA',
        'red': 'RED',
        'blue': 'BLUE',
        'dim': 'BLACK',
    }
    color_name = kind_map.get(kind, 'WHITE')
    print(_color_wrap(text, color_name))


def clear_screen():
    """Clear the terminal screen."""
    import os
    os.system('clear' if os.name != 'nt' else 'cls')


def wait_for_continue(prompt='Press Enter to continue...'):
    try:
        input(prompt)
    except Exception:
        pass

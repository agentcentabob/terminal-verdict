"""ASCII art and lightweight color helpers.

Provides small faces and larger, more expressive faces for the AI companion,
boxed render helpers, and a lightweight color wrapper that falls back when
`colorama` isn't available.
"""
try:
    from colorama import init as _init_colorama, Fore, Style
    _init_colorama()
    COLORAMA_AVAILABLE = True
except Exception:
    COLORAMA_AVAILABLE = False

# Small face (compact) and large expressive faces for the AI companion
FACES = {
    'happy': [
        '╔════════════════╗',
        '║   ( ◕ヮ◕)ﾉ     ║',
        '║    ~ HELLO ~   ║',
        '╚════════════════╝',
    ],
    'neutral': [
        '╔════════════════╗',
        '║   ( ◕w◕)      ║',
        '║    ...         ║',
        '╚════════════════╝',
    ],
    'thinking': [
        '╔════════════════╗',
        '║   ( ◕‿◕ )      ║',
        '║   ...analyzing ║',
        '╚════════════════╝',
    ],
    'nervous': [
        '╔════════════════╗',
        '║   ( ◕﹏◕ )     ║',
        '║    ...         ║',
        '╚════════════════╝',
    ],
    'sad': [
        '╔════════════════╗',
        '║   ( •́   •̀)   ║',
        '║    ...         ║',
        '╚════════════════╝',
    ],
}

SMALL_FACE = {
    'happy': [
        '╔═══════════╗',
        '║  ^   ^   ║',
        '║   \/     ║',
        '╚═══════════╝',
    ],
}


def _color_wrap(text, color_name):
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

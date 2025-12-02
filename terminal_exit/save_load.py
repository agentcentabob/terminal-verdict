"""Very small save/load helper using JSON for prototype state."""
import json
import os


class SaveLoad:
    SAVE_FILE = 'terminal_exit_save.json'

    def save(self, data):
        try:
            with open(self.SAVE_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception:
            return False

    def load(self):
        if not os.path.exists(self.SAVE_FILE):
            return None
        try:
            with open(self.SAVE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return None

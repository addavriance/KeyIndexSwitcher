from constants import UPPER_INDICES, LOWER_INDICES, UPPER_KEY, LOWER_KEY

from pynput.keyboard import Key, Controller, Listener, KeyCode
from enum import Enum


class IndexMode(Enum):
    Base = 0
    Upper = 1
    Lower = 2


class IndexConverter:
    def __init__(self):
        self.mode = IndexMode.Base

        self.keyboard = Controller()

        self.upper_key = UPPER_KEY
        self.lower_key = LOWER_KEY

        self.shortcut_pressed = False

        self.shortcut_keys = [Key.cmd, Key.alt, Key.ctrl, Key.cmd_r, Key.alt_r, Key.ctrl_r, Key.cmd_l, Key.alt_l, Key.ctrl_l, Key.alt_gr]

    def switch_mode(self, key: Key):
        if key == self.upper_key:
            self.mode = IndexMode.Upper if self.mode != IndexMode.Upper else IndexMode.Base
        elif key == self.lower_key:
            self.mode = IndexMode.Lower if self.mode != IndexMode.Lower else IndexMode.Base

    def on_press(self, key: Key | KeyCode):
        if key in self.shortcut_keys:
            self.shortcut_pressed = True

        if self.shortcut_pressed:
            return

        key in [self.upper_key, self.lower_key] and self.switch_mode(key)

        if self.mode == IndexMode.Upper:
            self.handle_key_press(key, UPPER_INDICES)
        elif self.mode == IndexMode.Lower:
            self.handle_key_press(key, LOWER_INDICES)

    def on_release(self, key):
        if key in self.shortcut_keys:
            self.shortcut_pressed = False

    def type_char(self, char):
        self.keyboard.type(char)

    def remove_char(self):
        self.keyboard.tap(Key.backspace)

    def handle_key_press(self, key: Key | KeyCode, index_mapping):
        try:
            char = key.char
        except AttributeError:
            return

        if char in index_mapping:

            index_char = index_mapping[char]

            self.remove_char()

            self.type_char(index_char)


if __name__ == "__main__":
    converter = IndexConverter()
    try:
        with Listener(on_press=converter.on_press, on_release=converter.on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("Bye!")

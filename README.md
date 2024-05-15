# KeyIndexSwitcher

KeyIndexSwitcher is a Python script that allows you to switch between different input modes (base, upper indices, and lower indices) by pressing specified function keys (F1 and F4 by default).

This tool is useful for typing mathematical and scientific notations that require superscript or subscript characters.

## Features

- Switch between base, upper indices, and lower indices input modes.
- Default keys for switching modes: F1 (upper indices) and F4 (lower indices).
- Easily customizable key mappings.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/addavriance/KeyIndexSwitcher.git
    cd KeyIndexSwitcher
    ```

2. **Install the required dependencies:**

    Make sure you have `pynput` installed. If not, you can install it using pip:

    ```bash
    pip install pynput
    ```

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Switching Modes:**
    - Press `F1` to switch to upper indices mode.
    - Press `F4` to switch to lower indices mode.
    - Press the same key again to switch back to base mode.

3. **Typing:**
    - In upper indices mode, characters such as `a`, `b`, `c`, etc., will be converted to their superscript equivalents.
    - In lower indices mode, characters such as `a`, `b`, `c`, etc., will be converted to their subscript equivalents.

## Customization

### Changing Key Mappings

You can change the keys used to switch modes by modifying the constants in `constants.py`:

```python
# constants.py

from pynput.keyboard import Key

UPPER_KEY = Key.f1  # Change this to your preferred key for upper indices
LOWER_KEY = Key.f4  # Change this to your preferred key for lower indices

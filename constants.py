from pynput.keyboard import Key

UPPER_INDICES = {
    "a": "ᶛ", "b": "ᵇ", "c": "ᶜ", "d": "ᵈ", "e": "ᵉ", "f": "ᶠ", "g": "ᵍ", "h": "ʰ", "i": "ᶦ", "j": "ʲ", "k": "ᵏ",
    "l": "ˡ", "m": "ᵐ",
    "n": "ⁿ", "o": "ᵒ", "p": "ᵖ", "q": "ʳ", "r": "ʳ", "s": "ˢ", "t": "ᵗ", "u": "ᵘ", "v": "ᵛ", "w": "ʷ", "x": "ˣ",
    "y": "ʸ", "z": "ᶻ",
    "A": "ᴬ", "B": "ᴮ", "C": "ᶜ", "D": "ᴰ", "E": "ᴱ", "F": "ᶠ", "G": "ᴳ", "H": "ᴴ", "I": "ᶦ", "J": "ᴶ", "K": "ᴷ",
    "L": "ᴸ", "M": "ᴹ",
    "N": "ᴺ", "O": "ᴼ", "P": "ᴾ", "Q": "°", "R": "ᴿ", "S": "ˢ", "T": "ᵀ", "U": "ᵁ", "V": "ⱽ", "W": "ʷ", "X": "ˣ",
    "Y": "ʸ", "Z": "ᶻ",
    "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹", "0": "⁰",
    "(": "⁽", ")": "⁾", "+": "⁺", "-": "⁻", "=": "⁼"
}

LOWER_INDICES = {
    "a": "ₐ", "b": "ᵦ", "c": "ᴄ", "d": "ᴅ", "e": "ₑ", "f": "ᵩ", "g": "ɢ", "h": "ₕ", "i": "ᵢ", "j": "ⱼ", "k": "ₖ",
    "l": "ₗ", "m": "ₘ",
    "n": "ₙ", "o": "ₒ", "p": "ₚ", "q": "ɢ", "r": "ᵣ", "s": "ₛ", "t": "ₜ", "u": "ᵤ", "v": "ᵥ", "w": "ᴡ", "x": "ₓ",
    "y": "ᵧ", "z": "ᴢ",
    "A": "ₐ", "B": "ᵦ", "C": "ᴄ", "D": "ᴅ", "E": "ₑ", "F": "ᵩ", "G": "ɢ", "H": "ₕ", "I": "ᵢ", "J": "ⱼ", "K": "ₖ",
    "L": "ʟ", "M": "ₘ",
    "N": "ₙ", "O": "ₒ", "P": "ₚ", "Q": "ɢ", "R": "ᵣ", "S": "ₛ", "T": "ₜ", "U": "ᵤ", "V": "ᵥ", "W": "ᴡ", "X": "ₓ",
    "Y": "ᵧ", "Z": "ᴢ",
    "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆", "7": "₇", "8": "₈", "9": "₉", "0": "₀",
    "(": "₍", ")": "₎", "+": "₊", "-": "₋", "=": "₌"
}

UPPER_KEY = Key.f1

LOWER_KEY = Key.f4

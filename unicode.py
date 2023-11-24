while True:
    symbol = input("Geben Sie ein Symbol ein (oder 'exit' zum Beenden): ")

    if symbol.lower() == 'exit':
        break

    try:
        unicode_value = ord(symbol)
        print(f"Unicode-Wert von '{symbol}': U+{unicode_value:04X}")
    except TypeError:
        print("Ungültiges Symbol. Bitte geben Sie ein einzelnes Zeichen ein.")

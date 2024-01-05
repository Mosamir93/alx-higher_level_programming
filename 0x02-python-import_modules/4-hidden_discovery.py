#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = [name for name in hidden_4.__dict__ if not name.startswith("__")]
    names.sort()

    for name in names:
        print(name)

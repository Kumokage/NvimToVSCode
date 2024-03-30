import re
import json

from modes import Modes
from utils import parse_command, remove_surroundings


remaps = {
        Modes.N.value: [],
        Modes.V.value: [],
        Modes.I.value: [],
        Modes.C.value: [],
        }
with open("remap.lua", "r") as fl:
    for line in fl:
        if not line.strip().startswith("vim.keymap.set"):
            continue
        result = re.search(r"\(.+\)", line)
        if result is None:
            continue
        mode, before, after = result.group()[1:-1].split(",")
        before = remove_surroundings(before)
        after = remove_surroundings(after)
        remap = {
            "before": list(parse_command(before)),
            "after": list(parse_command(after)),
        }

        match mode[1:-1]:
            case "n":
                remaps[Modes.N.value].append(remap)
            case "i":
                remaps[Modes.I.value].append(remap)
            case "c":
                remaps[Modes.C.value].append(remap)
            case "v" | "x":
                remaps[Modes.V.value].append(remap)
            case _:
                print("Don't now this mode: ", mode)
with open("result.json", 'w') as f:
    json.dump(remaps, f, indent=4)

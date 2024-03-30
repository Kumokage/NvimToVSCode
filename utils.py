def remove_surroundings(s: str):
    s = s.strip()
    if s[0] == '"':
        return s[1:-1]
    if s[0] == "[" and s[1] == "[":
        return s[2:-2]
    return s


def parse_command(s: str):
    buf = ""
    for i in s:
        if i == '"':
            yield f"\\{i}"
            continue
        if i == ">":
            buf += i
            yield f"{buf}"
            buf = ""
            continue
        if i == "<" or buf != "":
            buf += i
            continue
        yield f"{i}"

PARTS = [
    ("house that Jack built.", ""),
    ("malt", "that lay in"),
    ("rat", "that ate"),
    ("cat", "that killed"),
    ("dog", "that worried"),
    ("cow with the crumpled horn", "that tossed"),
    ("maiden all forlorn", "that milked"),
    ("man all tattered and torn", "that kissed"),
    ("priest all shaven and shorn", "that married"),
    ("rooster that crowed in the morn", "that woke"),
    ("farmer sowing his corn", "that kept"),
    ("horse and the hound and the horn", "that belonged to"),
]

def verse(n: int) -> str:
    """Return a single verse (1-indexed)."""
    parts = ["This is the " + PARTS[n-1][0]]
    # go backwards through earlier items
    for i in range(n-1, 0, -1):
        parts.append(PARTS[i][1] + " the " + PARTS[i-1][0])
    return " ".join(parts)

def recite(start_verse: int, end_verse: int) -> list[str]:
    """Return verses from start_verse to end_verse inclusive."""
    return [verse(i) for i in range(start_verse, end_verse+1)]

        
    





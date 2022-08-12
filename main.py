from random import sample

notes = [
	"A" , "A#", "Bb", "B" , "C" , "C#", "Db", "D" ,"D#",
    "Eb", "E" , "F" , "F#", "Gb", "G" , "G#", "Ab",
]

improper = ["B#", "Cb", "E#", "Fb"]

all_notes = notes + improper

doubles = [
	"A×"  , "B×"  , "C×"  , "D×"  , "E×"  , "F×"  , "G×"  ,
	"A#×" , "B#×" , "C#×" , "D#×" , "E#×" , "F#×" , "G#×" ,
	"Ab×" , "Bb×" , "Cb×" , "Db×" , "Eb×" , "Fb×" , "Gb×" ,
	"Adb" , "Bdb" , "Cdb" , "Ddb" , "Edb" , "Fdb" , "Gdb" ,
	"Abdb", "Bbdb", "Cbdb", "Dbdb", "Ebdb", "Fbdb", "Gbdb",
	"A#db", "B#db", "C#db", "D#db", "E#db", "F#db", "G#db",
]

naturals = {
	**dict.fromkeys(["A" , "G×" , "Bdb", "Cbdb"]        , "A"),
	**dict.fromkeys(["B" , "A×" , "Cb" , "Dbdb", "C#db"], "B"),
	**dict.fromkeys(["C" , "Bb×", "Ddb", "A#×" , "B#"  ], "C"),
	**dict.fromkeys(["D" , "C×" , "Edb", "Fbdb", "B#×" ], "D"),
	**dict.fromkeys(["E" , "D×" , "Fb" , "Gbdb", "F#db"], "E"),
	**dict.fromkeys(["F" , "Eb×", "Gdb", "E#"  , "D#×" ], "F"),
	**dict.fromkeys(["G" , "F×" , "Adb", "E#×" ]        , "G"),
}

sharps = {
	**dict.fromkeys(["G#", "Ab", "Gb×", "A#db", "F#×", "Bbdb"], "G#"),
	**dict.fromkeys(["A#", "Bb", "Ab×", "B#db", "G#×", "Cdb" ], "A#"),
	**dict.fromkeys(["C#", "Db", "Cb×", "D#db", "B×" , "Ebdb"], "C#"),
	**dict.fromkeys(["D#", "Eb", "Db×", "E#db", "C#×", "Fdb" ], "D#"),
	**dict.fromkeys(["F#", "Gb", "Fb×", "G#db", "E×" , "Abdb"], "F#"),
}

flats = {
	**dict.fromkeys(["Ab", "G#", "A#db", "Gb×", "F#×", "Bbdb"], "Ab"),
	**dict.fromkeys(["Bb", "A#", "B#db", "Ab×", "G#×", "Cdb" ], "Bb"),
	**dict.fromkeys(["Db", "C#", "D#db", "Cb×", "B×" , "Ebdb"], "Db"),
	**dict.fromkeys(["Eb", "D#", "E#db", "Db×", "C#×", "Fdb" ], "Eb"),
	**dict.fromkeys(["Gb", "F#", "G#db", "Fb×", "E×" , "Abdb"], "Gb"),
}

equivalents = {
	"A" : {"G": "G×", "B": "Bdb", "C": "Cbdb"},
	"B" : {"A": "A×", "C": "Cb" , "D": "Dbdb"},
	"C" : {"B": "B#", "D": "Ddb", "A": "A#×" },
	"D" : {"C": "C×", "E": "Edb", "F": "Fbdb" , "B": "B#×"},
	"E" : {"D": "D×", "F": "Fb" , "G": "Gbdb"},
	"F" : {"E": "E#", "G": "Gdb", "D": "D#db"},
	"G" : {"F": "F×", "A": "Adb", "E": "E#×" },

	"A#": {"B": "Bb", "G": "G#×", "C": "Cdb" },
	"B#": {"C": "C" , "D": "Ddb", "A": "A#×" },
	"C#": {"D": "Db", "B": "B×" , "E": "Ebdb"},
	"D#": {"E": "Eb", "C": "C#×", "F": "Fdb" },
	"E#": {"F": "F" , "G": "Gdb", "D": "D#db"},
	"F#": {"G": "Gb", "E": "E×" , "A": "Abdb"},
    "G#": {"A": "Ab", "F": "F#×", "B": "Bbdb"},

	"Ab": {"G": "G#", "F": "F#×", "B": "Bbdb"},
	"Bb": {"A": "A#", "G": "G#×", "C": "Cdb" },
	"Cb": {"B": "B" , "A": "A×" , "D": "Dbdb"},
	"Db": {"C": "C#", "B": "B×" , "E": "Ebdb"},
	"Eb": {"D": "D#", "C": "C#×", "F": "Fdb" },
	"Fb": {"E": "E" , "D": "D×" , "G": "Gbdb"},
	"Gb": {"F": "F#", "E": "E×" , "A": "Abdb"},
}


def gap(note1, note2):
    """returns the gap between the given notes as int,
    assuming note2 occurs after note1"""

    notes = [note1, note2]

    for i in range(2):
        notes[i] = sharp(flat(notes[i]))

    sequence = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    note1, note2 = notes
    gap = sequence.index(note2) - sequence.index(note1)

    return (gap + 12) if gap < 0 else gap


def sharp(note):
    """returns the next note in musical sequence"""

    if note in doubles:
        change = naturals if note in naturals else sharps
        note   = change[note]

    note += "#"
    note  = note.replace("b#", "")

    if note.count("#") == 2:
        note = note.replace("#", "") + "×"

    change = naturals if note in naturals else sharps
    return change[note]


def flat(note):
    """returns the previous note in musical sequence"""

    if note in doubles:
        change = naturals if note in naturals else flats
        note   = change[note]

    note += "b"
    note  = note.replace("#b", "")

    if note.count("b") == 2:
        note = note.replace("b", "") + "db"

    change = naturals if note in naturals else flats
    return change[note]


def is_scale(scale):
    """returns True if the given scale is valid, else False"""

    natural = {"A", "B", "C", "D", "E", "F", "G"}

    for note in natural:
        if note not in str(scale):
            return False

    for note in all_notes:
        if note in scale:
            for eq in equivalents[note]:
                if equivalents[note][eq] in scale:
                    return False

    return True


def is_mode(scale1, scale2):
    """returns True if the given scales are modes of each other, else False"""

    return set(scale1) == set(scale2)


def mode(scale, n):
    """returns the 'n'th mode of a 7-note scale"""

    if not isinstance(n, int):
        raise TypeError("'n' must be int")

    if not 1 <= n <= 7:
        raise ValueError("'n' must be between 1 and 7")

    return scale[n-1:] + scale[:n-1]


def transpose(scale, steps=0, key=None):
    """transposes a scale given number of halfsteps up or down
    if key is given, argument 'steps' will be ignored, transposes the scale to
    the given key
    returns the transposed scale as a list"""

    if isinstance(scale, tuple):
        scale = list(scale)

    if key is not None:
        key = key.replace("×", "##").replace("d", "b")

        base = key[0]
        for symbol in key[1:]:
            base = key = {"#": sharp, "b": flat}[symbol](base)

        steps  = gap(scale[0], key)
        steps -= 0 if "#" in key else 12

    if not isinstance(steps, int):
        raise TypeError("'steps' must be int")

    if not (steps % 12):
        if not is_scale(scale):
            natural = ["A", "B", "C", "D", "E", "F", "G"]
            mode_no = {natural[i]: i+1 for i in range(7)}[scale[0][:1]]

            mode_scale = mode(natural, mode_no)

            for i in range(7):
                if mode_scale[i] not in scale[i]:
                    scale[i] = equivalents[scale[i]][mode_scale[i]]

        return scale

    change = sharp if steps > 0 else flat
    for i in range(7):
        scale[i] = change(scale[i])

    return transpose(scale, steps-1 if steps > 0 else steps+1)


def triad_chords(scale):
    """returns the basic 3 - note triads allowed in a scale"""

    scale *= 2
    return [scale[i] + scale[i+2] + scale[i+4] for i in range(7)]


def seventh_chords(scale):
    """returns the 4 - note seventh chords allowed in a scale"""

    triads = triad_chords(scale) * 2
    return [scale[i] + triads[i+2] for i in range(7)]


def random_scale(root):
    """returns a random scale rooted on the given note as a tuple"""

    if root not in all_notes:
        raise ValueError("given 'root' is not a musical note")

    natural = ["A", "B", "C", "D", "E", "F", "G"]
    mode = {natural[i]: i for i in range(7)}[root[:1]]

    while True:
        scale = sorted(sample(all_notes, 7), key=(lambda x: x[0]))

        if not is_scale(scale):
            continue

        if "B#" in scale and "Cb" in scale:
            scale[1], scale[2] = "B", "C"

        if "E#" in scale and "Fb" in scale:
            scale[4], scale[5] = "E", "F"

        if root not in scale:
            continue

        return tuple(scale[mode:] + scale[:mode])
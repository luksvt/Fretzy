COMMON_TUNINGS = {
    4: ["Standard E", "Drop D"],
    5: ["Standard B", "Drop A"],
    6: [
        "Standard E", "Drop D", 
        "Standard D#", "Drop C#", 
        "Standard D", "Drop C", 
        "Standard C#", "Drop B", 
        "Standard C", "Drop A#", 
        "Standard B", "Drop A", 
        "Standard A"
    ],
    7: [
        "Standard B", "Drop A", 
        "Standard A#","Drop G#", 
        "Standard A", "Drop G", 
        "Standard G#", "Drop F#"
        ],
    8: ["Standard F#", "Drop E"]
}

TUNINGS_NOTES = {
    4: {
        "Standard E": ['G', 'D', 'A', 'E'],
        "Drop D": ['G', 'D', 'A', 'D'],
        # Add more 4-string tunings here...
    },
    5: {
        "Standard B": ['G', 'D', 'A', 'E', 'B'],
        "Drop A": ['G', 'D', 'A', 'E', 'A'],
        # Add more 5-string tunings here...
    },
    6: {
        "Standard E": ['E', 'B', 'G', 'D', 'A', 'E'],
        "Drop D": ['E', 'B', 'G', 'D', 'A', 'D'],
        "Standard D#": ['D#', 'A#', 'F#', 'C#', 'G#', 'D#'],
        "Drop C#": ['D#', 'A#', 'F#', 'C#', 'G#', 'C#'],
        "Standard D": ['D', 'A', 'F', 'C', 'G', 'D'],
        "Drop C": ['D', 'A', 'F', 'C', 'G', 'C'],
        "Standard C#": ['C#', 'G#', 'E', 'B', 'F#', 'C#'],
        "Drop B": ['C#', 'G#', 'E', 'B', 'F#', 'B'],
        "Standard C": ['C', 'G', 'D#', 'A#', 'F', 'C'],
        "Drop A#": ['C', 'G', 'D#', 'A#', 'F', 'A#'],
        "Standard B": ['B', 'F#', 'D', 'A', 'E', 'B'],
        "Drop A": ['B', 'F#', 'D', 'A', 'E', 'A'],
        "Standard A": ['A', 'E', 'C', 'G', 'D', 'A'],
    },
    7: {
        "Standard B": ['E', 'B', 'G', 'D', 'A', 'E', 'B'],
        "Drop A": ['E', 'B', 'G', 'D', 'A', 'E', 'A'],
        "Standard A#": ['D#', 'A#', 'F#', 'C#', 'G#', 'D#', 'A#'],
        "Drop G#": ['D#', 'A#', 'F#', 'C#', 'G#', 'D#', 'G#'],
        "Standard A": ['D', 'A', 'F', 'C', 'G', 'D', 'A'],
        "Drop G": ['D', 'A', 'F', 'C', 'G', 'D', 'G'],
        "Standard G#": ['C#', 'G#', 'E', 'B', 'F#', 'C#', 'G#'],
        "Drop F#": ['C#', 'G#', 'E', 'B', 'F#', 'C#', 'F#'],
        # Add more 7-string tunings here...
    },
    8: {
        "Standard F#": ['E', 'B', 'G', 'D', 'A', 'E', 'B', 'F#'],
        "Drop E": ['E', 'B', 'G', 'D', 'A', 'E', 'B', 'E'],
        # Add more 8-string tunings here...
    },
    # Add more string numbers and their tunings as needed
}

SCALES = {
    # Common scales
    "Major": [2, 2, 1, 2, 2, 2, 1],
    "Natural Minor": [2, 1, 2, 2, 1, 2, 2],
    "Harmonic Minor": [2, 1, 2, 2, 1, 3, 1],
    "Melodic Minor": [2, 1, 2, 2, 2, 2, 1],
    "Pentatonic Major": [2, 2, 3, 2, 3],
    "Pentatonic Minor": [3, 2, 2, 3, 2],
    "Blues": [3, 2, 1, 1, 3, 2],
    # Modes
    "Dorian": [2, 1, 2, 2, 2, 1, 2],
    "Phrygian": [1, 2, 2, 2, 1, 2, 2],
    "Lydian": [2, 2, 2, 1, 2, 2, 1],
    "Mixolydian": [2, 2, 1, 2, 2, 1, 2],
    "Aeolian": [2, 1, 2, 2, 1, 2, 2],  # Same as Natural Minor
    "Locrian": [1, 2, 2, 1, 2, 2, 2],
    # Exotic scales
    "Hungarian Minor": [2, 1, 3, 1, 1, 3, 1],
    "Neapolitan Minor": [1, 2, 2, 2, 1, 3, 1],
    "Neapolitan Major": [1, 2, 2, 2, 2, 2, 1],
    "Enigmatic": [1, 3, 2, 2, 2, 1, 1],
    "Double Harmonic": [1, 3, 1, 2, 1, 3, 1],
    "Spanish Gypsy": [1, 3, 1, 2, 1, 2, 2],
    "Hungarian Gypsy": [2, 1, 3, 1, 1, 2, 1],
    "Persian": [1, 3, 1, 1, 2, 3, 1],
    "Arabian": [2, 2, 1, 1, 2, 2, 2],
    "Japanese": [1, 4, 2, 1, 4],
    "Egyptian": [2, 3, 2, 3, 2],
    "Hirajoshi": [2, 1, 4, 1, 4],
    
    # Modal Scales
    "Mixolydian b6": [2, 2, 1, 2, 1, 2, 2],
    "Lydian Augmented": [2, 2, 2, 2, 1, 2, 1],

    # Harmonic Minor Modes
    "Phrygian Dominant": [1, 3, 1, 2, 1, 2, 2],
    "Locrian ♮6": [1, 2, 2, 1, 2, 2, 2],

    # Melodic Minor Modes
    "Lydian Dominant": [2, 2, 2, 1, 2, 1, 2],
    "Altered Scale": [1, 2, 1, 2, 2, 2, 2],

    # Symmetrical Scales
    "Whole Tone Scale": [2, 2, 2, 2, 2, 2],
    "Diminished Half-Whole": [1, 2, 1, 2, 1, 2, 1, 2],
    "Diminished Whole-Half": [2, 1, 2, 1, 2, 1, 2, 1],
    # ... more scales as needed ...
}

CHORDS = {
    "Major": [4, 3],
    "Minor": [3, 4],
    "Seventh": [4, 3, 3],
    "Minor Seventh": [3, 4, 3],
    "Major Seventh": [4, 3, 4],
    "Suspended Second": [2, 5],
    "Suspended Fourth": [5, 2],
    "Augmented": [4, 4],
    "Diminished": [3, 3],
    "Diminished Seventh": [3, 3, 3],
    "Half-Diminished": [3, 3, 4],
    "Minor Sixth": [3, 4, 2],
    "Major Sixth": [4, 3, 2],
    "Ninth": [4, 3, 3, 4],
    "Minor Ninth": [3, 4, 3, 4],
    "Major Ninth": [4, 3, 4, 3],
    "Add Nine": [4, 3, 7],
    "Eleventh": [4, 3, 3, 4, 3],
    "Minor Eleventh": [3, 4, 3, 4, 3],
    "Thirteenth": [4, 3, 3, 4, 3, 4],
    "Minor Thirteenth": [3, 4, 3, 4, 3, 4],
    
    # Extended Chords
    "Dominant 9th": [4, 3, 3, 4],
    "Dominant 11th": [4, 3, 3, 4, 3],
    "Dominant 13th": [4, 3, 3, 4, 3, 4],
    "Major 9": [4, 3, 4, 3],
    "Major 11": [4, 3, 4, 3, 2],
    "Major 13": [4, 3, 4, 3, 2, 2],

    # Altered Chords
    "7(b5)": [4, 3, 2],
    "7(#5)": [4, 4, 2],
    "7(b9)": [4, 3, 3, 1],
    "7(#9)": [4, 3, 3, 3],

    # Suspended Chords
    "Sus2": [2, 5],
    "Sus4": [5, 2],

    # Add Chords
    "Add9": [4, 3, 7],
    "Add11": [4, 3, 10],
    "Add13": [4, 3, 14],
    # ... more chords as needed ...
}

CHORD_PROGRESSIONS = {
    "Classic Rock: I-IV-V": ["I", "IV", "V"],
    "Jazz Standard: ii-V-I": ["ii", "V", "I"],
    "50s Progression: I-vi-IV-V": ["I", "vi", "IV", "V"],
    "Pop Punk: I-V-vi-IV": ["I", "V", "vi", "IV"],
    "Jazz Turnaround: ii-V-I-VI": ["ii", "V", "I", "VI"],
    "Blues: I-V-IV-V": ["I", "V", "IV", "V"],
    "Pop Ballad: vi-IV-I-V": ["vi", "IV", "I", "V"],
    "Doo-Wop: I-IV-VI-V": ["I", "IV", "VI", "V"],
    "Country: I-VI-II-V": ["I", "VI", "II", "V"],
    "Modern Pop: I-V-ii-VI": ["I", "V", "ii", "VI"],
    "Folk: I-II-IV-V": ["I", "II", "IV", "V"],
    "Soft Rock: I-III-IV-V": ["I", "III", "IV", "V"],
    "Soul: vi-ii-V-I": ["vi", "ii", "V", "I"],
    "Ambient: I-III-VI-II": ["I", "III", "VI", "II"],
    "Indie: I-ii-IV-V": ["I", "ii", "IV", "V"],
    "Jazz Modal: III-VI-II-V": ["III", "VI", "II", "V"],
    "Alternative Rock: I-VI-IV-V": ["I", "VI", "IV", "V"],
    "Progressive: I-IV-II-V": ["I", "IV", "II", "V"],
    "Psychedelic: I-III-VI-IV": ["I", "III", "VI", "IV"],
    "Classic Folk: I-II-iii-IV": ["I", "II", "iii", "IV"],
    "New Wave: I-IV-I-V": ["I", "IV", "I", "V"],
    "Grunge: I-IV-ii-V": ["I", "IV", "ii", "V"],
    "Garage Rock: I-V-IV-IV": ["I", "V", "IV", "IV"],
    "Canon Progression: I-V-vi-iii-IV": ["I", "V", "vi", "iii", "IV"],
    "Jazz Blues: I-vi-ii-V": ["I", "vi", "ii", "V"],
    "Modal Jazz: ii-iii-IV-I": ["ii", "iii", "IV", "I"],
    "Funk: vi-V-IV-III": ["vi", "V", "IV", "III"],
    "Latin Jazz: IV-I-IV-V": ["IV", "I", "IV", "V"],
    "Reggae: I-V-iii-IV": ["I", "V", "iii", "IV"],
    "Flamenco: I-VI-ii-V": ["I", "VI", "ii", "V"],
    # ... Add more progressions as needed ...
}



NOTE_COLORS = {
    "C": "#FFC0CB",  # Light Pink
    "C#": "#FFD700",  # Gold
    "D": "#F0E68C",  # Khaki
    "D#": "#32CD32",  # Lime Green
    "E": "#87CEFA",  # Light Sky Blue
    "F": "#BA55D3",  # Medium Orchid
    "F#": "#9370DB",  # Medium Purple
    "G": "#48D1CC",  # Medium Turquoise
    "G#": "#FF69B4",  # Hot Pink
    "A": "#FA8072",  # Salmon
    "A#": "#B0C4DE",  # Light Steel Blue
    "B": "#20B2AA"   # Light Sea Green
}

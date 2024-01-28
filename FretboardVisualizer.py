import tkinter as tk
from tkinter import ttk  # Import ttk for themed widgets
import tkinter.font as tkFont

# Constants and Global Variables
DEFAULT_NUM_STRINGS = 6
DEFAULT_NUM_FRETS = 24
DEFAULT_TUNING = ['E', 'B', 'G', 'D', 'A', 'E']  # Standard Tuning for 6 strings
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

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


def find_note_on_fretboard(open_note, fret):
    note_index = (NOTES.index(open_note) + fret) % len(NOTES)
    return NOTES[note_index]

def get_scale(root_note, scale_type):
    intervals = SCALES[scale_type]
    scale = [root_note]
    current_note = root_note
    for interval in intervals:
        current_index = (NOTES.index(current_note) + interval) % len(NOTES)
        current_note = NOTES[current_index]
        scale.append(current_note)
    return scale[:-1]

def get_chord_notes(root_note, chord_type):
    intervals = CHORDS[chord_type]
    chord_notes = [root_note]
    for interval in intervals:
        current_index = (NOTES.index(root_note) + interval) % len(NOTES)
        root_note = NOTES[current_index]
        chord_notes.append(root_note)
    return chord_notes

class FretboardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Guitar Fretboard Visualizer")

        style = ttk.Style()
        style.theme_use('clam')  # Use a theme for ttk widgets

        self.initial_window_size = "1300x450"  # Example size, adjust as needed
        #master.geometry(self.initial_window_size)

        self.num_strings = tk.IntVar(value=DEFAULT_NUM_STRINGS)
        self.num_frets = tk.IntVar(value=DEFAULT_NUM_FRETS)
        
        self.control_frame = tk.Frame(root)
        # Initialize fret_buttons
        self.fret_buttons = {}

        # Tuning setup
        self.tuning = DEFAULT_TUNING.copy()
        self.tuning_vars = [tk.StringVar(master, value=note) for note in self.tuning]
        self.tuning_selection_var = tk.StringVar(master)  # Add this line


        # Create StringVar for root note, scale, and chord selections
        self.note_var = tk.StringVar(master)
        self.scale_var = tk.StringVar(master)
        self.chord_var = tk.StringVar(master)

        # Set default values
        self.note_var.set("C")  # Default root note
        self.scale_var.set("Major")  # Default scale
        self.chord_var.set("Major")  # Default chord
        
        # Buttons and their state for scale and chord visualization
        self.visualize_scale_button = None
        self.visualize_scale_active = False
        self.visualize_chord_button = None
        self.visualize_chord_active = False
        self.show_progression_active = False
        self.show_progression_button = None
        self.find_scaleschords_active = False
        self.active_scale_result_button = None
        self.active_chord_result_button = None
        self.active_progression_result_button = None


        self.selected_notes = set()
        self.scale_results_var = tk.StringVar(master)
        self.chords_results_var = tk.StringVar(master)
        self.use_chord_for_progression = tk.BooleanVar(value=False)

        self.setup_controls()
        self.visualize_fretboard()

    def reset_button_styles(self):
        # Reset styles for both buttons
        if self.visualize_scale_button:
            self.visualize_scale_button.config(bg='SystemButtonFace')
        if self.visualize_chord_button:
            self.visualize_chord_button.config(bg='SystemButtonFace')

    def setup_controls(self):
        default_font = tkFont.Font(family="Helvetica", size=10)
        # Top Frame for Strings and Frets
        top_frame = tk.Frame(self.master)
        top_frame.pack(pady=5)
        tk.Label(top_frame, text="Strings:").pack(side=tk.LEFT)
        tk.Spinbox(top_frame, from_=4, to=8, textvariable=self.num_strings, command=self.update_fretboard).pack(side=tk.LEFT)
        tk.Label(top_frame, text="Frets:").pack(side=tk.LEFT)
        tk.Spinbox(top_frame, from_=5, to=24, textvariable=self.num_frets, command=self.update_fretboard).pack(side=tk.LEFT)
    
        # Middle Frame for Tuning
        tuning_frame = tk.Frame(self.master)
        tuning_frame.pack(pady=5)
        tk.Label(tuning_frame, text="Tuning:").pack(side=tk.LEFT)
    
        self.tuning_vars.clear()
        for i in range(self.num_strings.get()):
            var = tk.StringVar(self.master, value=self.tuning[i])
            self.tuning_vars.append(var)
        for var in reversed(self.tuning_vars):
            tk.OptionMenu(tuning_frame, var, *NOTES).pack(side=tk.LEFT)
        tk.Button(tuning_frame, text="Update Tuning", command=self.update_tuning, font=default_font).pack(side=tk.LEFT)
        
        # Label and Dropdown for Common Tunings
        tk.Label(tuning_frame, text="Common Tunings:").pack(side=tk.LEFT)
        self.tuning_menu = tk.OptionMenu(tuning_frame, self.tuning_selection_var, *COMMON_TUNINGS.get(self.num_strings.get(), []))
        self.tuning_menu.pack(side=tk.LEFT)

    
        # Bottom Frame for Root Note, Scale, and Chords
        bottom_frame = tk.Frame(self.master)
        bottom_frame.pack(pady=5)
    
        # Root Note Selection
        root_note_frame = tk.Frame(bottom_frame)
        root_note_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(root_note_frame, text="Root Note:").pack(side=tk.LEFT)
        tk.OptionMenu(root_note_frame, self.note_var, *NOTES, command=self.on_root_note_change).pack(side=tk.LEFT)
    
        # Scale Controls
        scale_frame = tk.Frame(bottom_frame)
        scale_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(scale_frame, text="Scale:").pack(side=tk.LEFT)
        scale_menu = tk.OptionMenu(scale_frame, self.scale_var, *SCALES.keys(), command=self.on_scale_change)
        scale_menu.pack(side=tk.LEFT)
        self.visualize_scale_button = tk.Button(scale_frame, text="Visualize Scale", command=self.visualize_scale, font=default_font)
        self.visualize_scale_button.pack(side=tk.LEFT)
    
        # Chord Controls
        chord_frame = tk.Frame(bottom_frame)
        chord_frame.pack(side=tk.LEFT, padx=10)
        tk.Label(chord_frame, text="Chord:").pack(side=tk.LEFT)
        chord_menu = tk.OptionMenu(chord_frame, self.chord_var, *CHORDS.keys(), command=self.on_chord_change)
        chord_menu.pack(side=tk.LEFT)
        self.visualize_chord_button = tk.Button(chord_frame, text="Visualize Chord", command=self.visualize_chord, font=default_font)
        self.visualize_chord_button.pack(side=tk.LEFT)

        self.find_scaleschords_button = tk.Button(chord_frame, text="Find Scales/Chords", command=self.update_scales_and_chords_display, font=default_font)
        self.find_scaleschords_button.pack(side=tk.LEFT, padx=20)
    
        # Chord Progression Frame
        progression_frame = tk.Frame(self.master)
        progression_frame.pack(pady=5)
    
        self.progression_var = tk.StringVar(self.master)
        tk.Label(progression_frame, text="Chord Progressions:").pack(side=tk.LEFT)
        self.progression_menu = tk.OptionMenu(progression_frame, self.progression_var, *CHORD_PROGRESSIONS.keys(), command=self.on_progression_selected)
        self.progression_menu.pack(side=tk.LEFT)
        self.show_progression_button = tk.Button(progression_frame, text="Show Progression", command=self.show_progression, font=default_font)
        self.show_progression_button.pack(side=tk.LEFT)

        self.use_chord_checkbox = tk.Checkbutton(
            progression_frame, text="Use Chord", 
            var=self.use_chord_for_progression, 
            command=self.on_use_chord_checkbox_changed
        )
        self.use_chord_checkbox.pack(side=tk.LEFT)

        # tk.Button(progression_frame, text="Clear Fretboard", command=self.clear_highlights, font=default_font).pack(side=tk.LEFT, padx=20)

        # Results grid area
        self.results_frame = tk.Frame(self.master)
        self.results_frame.pack(pady=5, fill=tk.BOTH, expand=True)

        # Frames for each section with border
        scales_frame = tk.Frame(self.results_frame, borderwidth=1, relief="solid")
        chords_frame = tk.Frame(self.results_frame, borderwidth=1, relief="solid")
        progressions_frame = tk.Frame(self.results_frame, borderwidth=1, relief="solid")

        # Place section frames in grid
        scales_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=2)
        chords_frame.grid(row=1, column=0, sticky="ew", padx=5, pady=2)
        progressions_frame.grid(row=2, column=0, sticky="ew", padx=5, pady=2)

        # Labels and result areas within each section frame
        tk.Label(scales_frame, text="Scales:", font=("Helvetica", 10, 'bold')).pack(side=tk.LEFT, padx=5)
        self.scales_result_area = tk.Frame(scales_frame)
        self.scales_result_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)

        tk.Label(chords_frame, text="Chords:", font=("Helvetica", 10, 'bold')).pack(side=tk.LEFT, padx=5)
        self.chords_result_area = tk.Frame(chords_frame)
        self.chords_result_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)

        tk.Label(progressions_frame, text="Chord Progression:", font=("Helvetica", 10, 'bold')).pack(side=tk.LEFT, padx=5)
        self.progressions_result_area = tk.Frame(progressions_frame)
        self.progressions_result_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=2)

        # Configure column weights to allocate space proportionally
        self.results_frame.grid_columnconfigure(1, weight=1)

    def update_fretboard(self):
        new_tuning_length = self.num_strings.get()
    
        # Adjust the tuning list based on the number of strings
        while len(self.tuning) < new_tuning_length:
            # Add a string tuned 5 half steps below the last one, or default to 'E'
            if len(self.tuning) > 0:
                prev_note_index = NOTES.index(self.tuning[-1])
                new_note = NOTES[(prev_note_index - 5) % len(NOTES)]
            else:
                new_note = 'E'
            self.tuning.append(new_note)
    
        # Trim the tuning list if the number of strings is reduced
        self.tuning = self.tuning[:new_tuning_length]
    
        # Rebuild the fretboard with the new tuning
        self.setup_controls()
        self.visualize_fretboard()

    def on_scale_change(self, _):
        if self.visualize_scale_active:
            self.visualize_scale()

    def on_chord_change(self, _):
        if self.visualize_chord_active:
            self.visualize_chord()

    def on_root_note_change(self, _):
        self.clear_highlights()
        # If "Visualize Scale" is active, update scale visualization
        if self.visualize_scale_active:
            self.update_scale_visualization()

        # If "Visualize Chord" is active, update chord visualization
        if self.visualize_chord_active:
            self.update_chord_visualization()

        # Update chord progression display
        self.update_chord_progression_display()



    def visualize_fretboard(self):
        def create_note_button(note, row, column):
            note_button = tk.Button(fretboard_frame, text=note, width=5, 
                                    command=lambda: self.toggle_note_selection(note, note_button), **button_style)
            note_button.grid(row=row + 1, column=column)  # Offset by 1 row for upper fret markers
            self.fret_buttons[row][column] = note_button

        for widget in self.master.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.control_frame:
                widget.destroy()
        self.setup_controls()

        fretboard_frame = tk.Frame(self.master)
        fretboard_frame.pack()

        # Style for open string notes
        open_string_style = {'font': ('Helvetica', 12, 'bold')}
        # Styling for buttons and labels
        button_style = {'font': ('Helvetica', 10), 'bg': 'white', 'activebackground': 'gray'}
        label_style = {'font': ('Helvetica', 10, 'bold'), 'bg': 'lightgray'}

        # Create buttons for frets and store references
        for string in range(self.num_strings.get()):
            self.fret_buttons[string] = {}

            # Open string/nut visualization with increased font size and bold
            open_string_label = tk.Label(fretboard_frame, text=self.tuning[string], width=5, bg='darkgrey', **open_string_style)
            open_string_label.grid(row=string + 1, column=0)  # Offset by 1 row for upper fret markers
            self.fret_buttons[string][0] = open_string_label

            for fret in range(1, self.num_frets.get() + 1):
                note = find_note_on_fretboard(self.tuning[string], fret)
                create_note_button(note, string, fret)

        # Fret labels aligned with fret buttons
        marker_frets = [3, 5, 7, 9, 12, 15, 17, 19, 21, 24]
        marker_color = "#ADD8E6"
        for fret in range(1, self.num_frets.get() + 1):
            # Upper fret markers
            upper_label = tk.Label(fretboard_frame, text=str(fret), width=5, **label_style)
            upper_label.grid(row=0, column=fret)
            if fret in marker_frets:
                upper_label.config(bg=marker_color)

            # Lower fret markers
            lower_label = tk.Label(fretboard_frame, text=str(fret), width=5, **label_style)
            lower_label.grid(row=self.num_strings.get() + 1, column=fret)  # Offset by 1 row for upper fret markers
            if fret in marker_frets:
                lower_label.config(bg=marker_color)



        

    def highlight_notes(self, notes):
        default_font = tkFont.Font(family="Helvetica", size=10)
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        for string in range(self.num_strings.get()):
            for fret in range(0, self.num_frets.get() + 1):  # Include open string (fret 0)
                note = find_note_on_fretboard(self.tuning[string], fret)
                
                # Access the button or label using stored references
                note_widget = self.fret_buttons[string][fret]
                if note in notes:
                    if fret == 0:
                        # Highlight text for open notes
                        note_widget.config(fg=NOTE_COLORS.get(note, 'yellow'), font=bold_font)
                    else:
                        # Highlight background for fretted notes
                        note_widget.config(bg=NOTE_COLORS.get(note, 'yellow'), font=bold_font)
                else:
                    if fret == 0:
                        # Reset open note text color
                        note_widget.config(fg='black')
                    else:
                        # Reset fretted note background color
                        note_widget.config(bg='white')

    def visualize_scale(self):
        # Reset active buttons of other types
        if self.active_chord_result_button and self.active_chord_result_button.winfo_exists():
            self.active_chord_result_button.config(bg='SystemButtonFace')
        if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
            self.active_progression_result_button.config(bg='SystemButtonFace')

        # Default and bold fonts
        default_font = tkFont.Font(family="Helvetica", size=10)
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.clear_selected_notes()
        self.scale_results_var.set('')

        if self.find_scaleschords_active:
            # Deactivate Find Scales/Chords
            self.find_scaleschords_active = False
            self.find_scaleschords_button.config(bg='SystemButtonFace')
            self.clear_results_area(self.scales_result_area)
            self.clear_results_area(self.chords_result_area)

        if self.visualize_scale_active:
            # Deactivate Visualize Scale
            self.clear_highlights()
            self.clear_results_area(self.scales_result_area)
            self.visualize_scale_button.config(bg='SystemButtonFace', font=default_font)
            self.visualize_scale_active = False
            if self.active_scale_result_button and self.active_scale_result_button.winfo_exists():
                self.active_scale_result_button.config(bg='SystemButtonFace')
            self.active_scale_result_button = None  # Reset the active scale button reference
        else:
            # Activate Visualize Scale
            self.clear_results_area(self.chords_result_area)
            self.visualize_scale_button.config(bg='lightblue')
            self.visualize_scale_active = True
            if self.visualize_chord_button:
                self.visualize_chord_button.config(bg='SystemButtonFace', font=default_font)
            self.visualize_chord_active = False
            root_note = self.note_var.get()
            scale_type = self.scale_var.get()
            scale_notes = get_scale(root_note, scale_type)
            self.highlight_notes(scale_notes)
            scale_label = f"{self.note_var.get()} {self.scale_var.get()}"
            self.update_scale_result_area(scale_label, True)  # Update the scale result area

    
    def visualize_chord(self):
        if self.active_scale_result_button and self.active_scale_result_button.winfo_exists():
            self.active_scale_result_button.config(bg='SystemButtonFace')
            self.active_scale_result_button = None
        if self.active_chord_result_button and self.active_chord_result_button.winfo_exists():
            self.active_chord_result_button.config(bg='SystemButtonFace')
            self.active_chord_result_button = None
        if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
            self.active_progression_result_button.config(bg='SystemButtonFace')
            self.active_progression_result_button = None
        default_font = tkFont.Font(family="Helvetica", size=10)
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")
        self.clear_selected_notes()
        self.scale_results_var.set('')
        if self.find_scaleschords_active:
            self.find_scaleschords_active = False
            self.find_scaleschords_button.config(bg='SystemButtonFace')
            self.clear_results_area(self.scales_result_area)
            self.clear_results_area(self.chords_result_area)
        if self.visualize_chord_active:
            # Button is already active, so deactivate it and clear highlights
            self.clear_highlights()
            self.clear_results_area(self.chords_result_area)
            self.visualize_chord_button.config(bg='SystemButtonFace', font=default_font)
            self.visualize_chord_active = False
        else:
            # Activate this button, deactivate the other, and highlight notes
            self.clear_results_area(self.scales_result_area)
            self.visualize_chord_button.config(bg='lightblue')
            self.visualize_chord_active = True
            if self.visualize_scale_button:
                self.visualize_scale_button.config(bg='SystemButtonFace', font=default_font)
            self.visualize_scale_active = False
            root_note = self.note_var.get()
            chord_type = self.chord_var.get()
            chord_notes = get_chord_notes(root_note, chord_type)
            self.highlight_notes(chord_notes)
            chord_label = f"{self.note_var.get()} {self.chord_var.get()}"
            self.update_chord_result_area(chord_label, True)

    def update_scale_visualization(self):
        root_note = self.note_var.get()
        scale_type = self.scale_var.get()
        scale_notes = get_scale(root_note, scale_type)
        if self.active_scale_result_button:
            self.highlight_notes(scale_notes)
        scale_label = f"{root_note} {scale_type}"
        #if self.active_scale_result_button and self.active_scale_result_button.winfo_exists():
        self.update_scale_result_area(scale_label)


    def update_chord_visualization(self):
        # Do not deactivate, only update the chord visualization
        root_note = self.note_var.get()
        chord_type = self.chord_var.get()
        chord_notes = get_chord_notes(root_note, chord_type)
        if self.active_chord_result_button:
            self.highlight_notes(chord_notes)
        chord_label = f"{root_note} {chord_type}"
        #if self.active_chord_result_button and self.active_chord_result_button.winfo_exists():
        self.update_chord_result_area(chord_label)

    
    def visualize_on_fretboard(self, entity, entity_type, button):
        # Deactivate the previously active button of the same type if it's different
        if entity_type == 'scale':
            if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
                self.active_progression_result_button.config(bg='SystemButtonFace')
                self.active_progression_result_button = None
            if self.active_scale_result_button and self.active_scale_result_button != button and self.active_scale_result_button.winfo_exists():
                self.active_scale_result_button.config(bg='SystemButtonFace')
            self.active_scale_result_button = button
        elif entity_type == 'chord':
            if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
                self.active_progression_result_button.config(bg='SystemButtonFace')
                self.active_progression_result_button = None
            if self.active_chord_result_button and self.active_chord_result_button != button and self.active_chord_result_button.winfo_exists():
                self.active_chord_result_button.config(bg='SystemButtonFace')
            self.active_chord_result_button = button
        elif entity_type == 'progression':
            if self.active_scale_result_button and self.active_scale_result_button.winfo_exists():
                self.active_scale_result_button.config(bg='SystemButtonFace')
                self.active_scale_result_button = None
            if self.active_chord_result_button and self.active_chord_result_button.winfo_exists():
                self.active_chord_result_button.config(bg='SystemButtonFace')
                self.active_chord_result_button = None
            if self.active_progression_result_button and self.active_progression_result_button != button and self.active_progression_result_button.winfo_exists():
                self.active_progression_result_button.config(bg='SystemButtonFace')
            self.active_progression_result_button = button

        # Toggle the active state of the current button
        if button['bg'] == 'lightblue':
            button.config(bg='SystemButtonFace')
            self.clear_highlights()
        else:
            button.config(bg='lightblue')
            #print(entity, entity_type, self.visualize_scale_active)
            notes_to_highlight = self.get_notes_to_highlight(entity, entity_type)
            if notes_to_highlight:
                self.highlight_notes(notes_to_highlight)


    def get_notes_to_highlight(self, entity, entity_type):
        notes_to_highlight = []
        if entity_type == 'scale':
            root_note, scale_type = entity.split(' ', 1)
            notes_to_highlight = get_scale(root_note, scale_type)
        elif entity_type == 'chord':
            root_note, chord_type = entity.split(' ', 1)
            notes_to_highlight = get_chord_notes(root_note, chord_type)
        elif entity_type == 'progression':
            root_note, chord_type = entity.split(' ', 1)
            notes_to_highlight = get_chord_notes(root_note, chord_type)
        return notes_to_highlight


    
    def clear_highlights(self):
        default_font = tkFont.Font(family="Helvetica", size=10)
        for string in range(self.num_strings.get()):
            for fret in range(0, self.num_frets.get() + 1):
                note_widget = self.fret_buttons[string][fret]
                if fret == 0:
                    # Reset open note text color
                    note_widget.config(fg='black')
                else:
                    # Reset fretted note background color
                    note_widget.config(bg='white', font=default_font)


    def update_tuning(self):
        # Check if a common tuning is selected
        selected_common_tuning = self.tuning_selection_var.get()
        if selected_common_tuning in COMMON_TUNINGS.get(self.num_strings.get(), []):
            # Update tuning based on the selected common tuning
            new_tuning = self.get_tuning_notes(self.num_strings.get(), selected_common_tuning)
            for i, note in enumerate(new_tuning):
                self.tuning_vars[i].set(note)
        else:
            # Update tuning based on the individual dropdowns
            new_tuning = [var.get() for var in self.tuning_vars]
    
        self.tuning = new_tuning
        self.visualize_fretboard()
    
        # Reset the common tunings dropdown
        self.tuning_selection_var.set('')



        
    def update_tuning_dropdown(self):
        # Clear the existing menu entries
        menu = self.tuning_menu["menu"]
        menu.delete(0, "end")
    
        # Add new entries to the menu
        for tuning in COMMON_TUNINGS.get(self.num_strings.get(), []):
            menu.add_command(label=tuning, command=lambda value=tuning: self.tuning_selection_var.set(value))
    
        # Set the default value for the dropdown
        if COMMON_TUNINGS.get(self.num_strings.get()):
            self.tuning_selection_var.set(COMMON_TUNINGS[self.num_strings.get()][0])

        
    # Function to get notes for a given tuning and number of strings
    def get_tuning_notes(self, num_strings, tuning_name):
        return TUNINGS_NOTES[num_strings].get(tuning_name, ['E'] * num_strings)


    def get_scale_degree_chord(self, root_note, scale_degree):
        # First, build the major scale for the root note
        major_scale = get_scale(root_note, "Major")
        
        # Translate scale degree to index and type (I -> (0, Major), ii -> (1, Minor), etc.)
        degree_info = {
            "I": (0, "Major"),
            "ii": (1, "Minor"),
            "iii": (2, "Minor"),
            "IV": (3, "Major"),
            "V": (4, "Major"),
            "vi": (5, "Minor"),
            "vii": (6, "Diminished"),
            "II": (1, "Major"),
            "III": (2, "Major"),
            "VI": (5, "Major"),
            "VII": (6, "Major")
        }
        degree_index, chord_type = degree_info.get(scale_degree, (None, None))
    
        # Check if degree_index is None to avoid KeyError
        if degree_index is not None:
            chord_root = major_scale[degree_index]
            return chord_root, chord_type
        else:
            # Handle invalid scale degree
            return None, None


    
    def on_progression_selected(self, event=None):
        # Deactivate the active result button if it's valid
        if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
            self.active_progression_result_button.config(bg='SystemButtonFace')
            self.active_progression_result_button = None

            # Clear the highlights from the fretboard
            self.clear_highlights()

        # Continue with displaying the new chord progression
        if self.show_progression_active:
            progression_name = self.progression_var.get()
            if progression_name in CHORD_PROGRESSIONS:
                self.clear_results_area(self.progressions_result_area)
                scale_degrees = CHORD_PROGRESSIONS[progression_name]
                root_note = self.note_var.get()
                for scale_degree in scale_degrees:
                    chord_root, chord_type = self.get_scale_degree_chord(root_note, scale_degree)
                    if chord_root and chord_type:
                        chord_name = f"{chord_root} {chord_type}"
                        button = tk.Button(self.progressions_result_area, text=chord_name)
                        button.config(command=lambda c=chord_name, b=button: self.visualize_on_fretboard(c, 'progression', b))
                        button.pack(side=tk.LEFT)

    def show_progression(self):
        progression_name = self.progression_var.get()

        if not progression_name:
            self.clear_results_area(self.progressions_result_area)
            label = tk.Label(self.progressions_result_area, text="Please select a chord progression first.")
            label.pack(side=tk.LEFT)
            return

        if self.show_progression_active:
            # Deactivate the button, clear results, reset the dropdown
            self.show_progression_button.config(bg='SystemButtonFace')
            self.clear_results_area(self.progressions_result_area)
            self.progression_var.set('')  # Reset the dropdown selection
            self.show_progression_active = False

            # Deactivate any active result buttons created by Show Progression
            if self.active_progression_result_button and self.active_progression_result_button.winfo_exists():
                self.active_progression_result_button.config(bg='SystemButtonFace')
                self.active_progression_result_button = None

            # Clear the highlights from the fretboard
            self.clear_highlights()
        else:
            # Activate the button and determine which progression to display
            self.show_progression_button.config(bg='lightblue')
            self.show_progression_active = True

            if self.use_chord_for_progression.get():
                # Show progression based on the selected chord
                self.show_chord_based_progression()
            else:
                # Show standard progression based on root note
                self.on_progression_selected()

    def on_use_chord_checkbox_changed(self):
        # Logic to update the display when the checkbox state changes
        if self.show_progression_active:
            self.show_progression()

    def show_chord_based_progression(self):
        # Implement logic to generate and display chord progressions based on the selected chord
        pass

    def update_chord_progression_display(self):
        # Clear previous progression results
        self.clear_results_area(self.progressions_result_area)

        # Re-display the selected chord progression
        progression_name = self.progression_var.get()
        if progression_name in CHORD_PROGRESSIONS:
            scale_degrees = CHORD_PROGRESSIONS[progression_name]
            root_note = self.note_var.get()
            for i, scale_degree in enumerate(scale_degrees):
                chord_root, chord_type = self.get_scale_degree_chord(root_note, scale_degree)
                chord_name = f"{chord_root} {chord_type}"
                button = tk.Button(self.progressions_result_area, text=chord_name)
                button.config(command=lambda c=chord_name, b=button: self.visualize_on_fretboard(c, 'progression', b))
                button.grid(row=0, column=i, sticky="w")
                
    
    def get_chord_name(self, root_note, chord_type):
        # Returns the name of the chord based on root note and chord type
        # This can be a simple implementation or more complex based on your chord naming rules
        return f"{root_note} {chord_type}"

    def toggle_note_selection(self, note, note_widget):
        # Define the default and bold fonts
        default_font = tkFont.Font(family="Helvetica", size=10)
        bold_font = tkFont.Font(family="Helvetica", size=10, weight="bold")

        # If scale or chord visualization is active, do not allow toggle
        if self.visualize_scale_active or self.visualize_chord_active:
            return

        if note in self.selected_notes:
            self.selected_notes.remove(note)
            note_widget.config(bg='white', font=default_font)
        else:
            self.selected_notes.add(note)
            note_widget.config(bg=NOTE_COLORS.get(note, 'yellow'), font=bold_font)

    
    def find_matching_scales(self):
        matching_scales = []
        for root_note in NOTES:
            for scale_name, intervals in SCALES.items():
                scale_notes = set(get_scale(root_note, scale_name))
                if self.selected_notes.issubset(scale_notes):
                    matching_scales.append(f"{root_note} {scale_name}")
        return matching_scales


    def find_matching_chords(self):
        if not self.selected_notes:
            return []

        matching_chords = []
        for chord_name, intervals in CHORDS.items():
            # Generate all chords for comparison (all rotations of the chord)
            for note in NOTES:
                chord_notes = set(get_chord_notes(note, chord_name))
                if self.selected_notes.issubset(chord_notes):
                    matching_chords.append(f"{note} {chord_name}")
                    break  # Break if a matching chord is found
        return matching_chords


    def update_scale_results_display(self):
        self.clear_results_area(self.scales_result_area)
        if not self.selected_notes:
            label = tk.Label(self.scales_result_area, text="Please select notes first.")
            label.pack(side=tk.LEFT)
            if self.find_scaleschords_active:
                self.find_scaleschords_active = False
                self.find_scaleschords_button.config(bg='SystemButtonFace')
            return

        matching_scales = self.find_matching_scales()

        max_buttons_per_row = 10  # Adjust this number based on your UI design
        current_row = None
        button_count = 0

        for scale in matching_scales:
            if button_count % max_buttons_per_row == 0:
                current_row = tk.Frame(self.scales_result_area)
                current_row.pack(fill=tk.X, expand=True)

            button = tk.Button(current_row, text=scale)
            button.config(command=lambda s=scale, b=button: self.visualize_on_fretboard(s, 'scale', b))
            button.pack(side=tk.LEFT, padx=2, pady=2)
            button_count += 1

    def update_chord_results_display(self):
        self.clear_results_area(self.chords_result_area)  # Clear previous results
        if not self.selected_notes:
            label = tk.Label(self.chords_result_area, text="Please select notes first.")
            label.pack(side=tk.LEFT)
            if self.find_scaleschords_active:
                self.find_scaleschords_active = False
                self.find_scaleschords_button.config(bg='SystemButtonFace')
            return

        matching_chords = self.find_matching_chords()

        max_buttons_per_row = 10  # Adjust this number based on your UI design
        current_row = None
        button_count = 0

        for chord in matching_chords:
            if button_count % max_buttons_per_row == 0:
                current_row = tk.Frame(self.chords_result_area)
                current_row.pack(fill=tk.X, expand=True)

            button = tk.Button(current_row, text=chord)
            button.config(command=lambda c=chord, b=button: self.visualize_on_fretboard(c, 'chord', b))
            button.pack(side=tk.LEFT, padx=2, pady=2)
            button_count += 1

        if not matching_chords:
            label = tk.Label(self.chords_result_area, text="No fit with any chords here.")
            label.pack(side=tk.LEFT)



    def update_scales_and_chords_display(self):
        if self.find_scaleschords_active:
            # Deactivate and clear results, reset window size
            self.clear_results_area(self.scales_result_area)
            self.clear_results_area(self.chords_result_area)
            self.find_scaleschords_button.config(bg='SystemButtonFace')
            self.find_scaleschords_active = False
            #self.master.geometry(self.initial_window_size)
        else:
            # Activate and find scales/chords
            self.find_scaleschords_button.config(bg='lightblue')
            self.find_scaleschords_active = True

            # Deactivate other buttons
            if self.visualize_scale_button:
                self.visualize_scale_button.config(bg='SystemButtonFace')
                self.visualize_scale_active = False
            if self.visualize_chord_button:
                self.visualize_chord_button.config(bg='SystemButtonFace')
                self.visualize_chord_active = False
            
            #self.clear_highlights()
            self.clear_results_area(self.chords_result_area)

            # Update results for scales and chords
            self.update_scale_results_display()
            self.update_chord_results_display()
    
    def update_scale_result_area(self, scale_label, forceactive = False):
        self.clear_results_area(self.scales_result_area)
        # if self.active_scale_result_button and self.active_scale_result_button.winfo_exists():
        #     self.active_scale_result_button.config(bg='SystemButtonFace')
        if self.active_scale_result_button or forceactive:
            # Create new active scale button
            button = tk.Button(self.scales_result_area, text=scale_label, bg='lightblue')
            button.config(command=lambda s=scale_label, b=button: self.visualize_on_fretboard(s, 'scale', b))
            button.pack(side=tk.LEFT)
            self.active_scale_result_button = button  # Set the new active button
        else:
            button = tk.Button(self.scales_result_area, text=scale_label)
            button.config(command=lambda s=scale_label, b=button: self.visualize_on_fretboard(s, 'scale', b))
            button.pack(side=tk.LEFT)


    def update_chord_result_area(self, chord_label, forceactive = False):
        self.clear_results_area(self.chords_result_area)
        if self.active_chord_result_button and self.active_chord_result_button.winfo_exists():
            self.active_chord_result_button.config(bg='SystemButtonFace')

        if self.active_chord_result_button or forceactive:
            button = tk.Button(self.chords_result_area, text=chord_label, bg='lightblue')
            button.config(command=lambda c=chord_label, b=button: self.visualize_on_fretboard(c, 'chord', b))
            button.pack(side=tk.LEFT)
            self.active_chord_result_button = button  # Set the new active button
        else:
            button = tk.Button(self.chords_result_area, text=chord_label)
            button.config(command=lambda c=chord_label, b=button: self.visualize_on_fretboard(c, 'chord', b))
            button.pack(side=tk.LEFT)


    def clear_selected_notes(self):
        self.selected_notes.clear()
        for string in range(self.num_strings.get()):
            for fret in range(0, self.num_frets.get() + 1):
                note_widget = self.fret_buttons[string][fret]
                # Reset button color to default and font to non-bold
                if fret == 0:
                    note_widget.config(fg='black')
                else:
                    note_widget.config(bg='white', font=tkFont.Font(family="Helvetica", size=10))

    def reset_results_frame_layout(self):
        # Reset the row and column configuration of the results_frame
        for i in range(self.results_frame.grid_size()[0]):  # Reset all rows
            self.results_frame.grid_rowconfigure(i, minsize=0, weight=0)
        for i in range(self.results_frame.grid_size()[1]):  # Reset all columns
            self.results_frame.grid_columnconfigure(i, minsize=0, weight=0)

    def clear_results_area(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        # Manually set the frame size to minimum
        frame.config(width=1, height=1)




    def update_selected_notes_display(self):
        # This method should update the display to show the currently selected notes
        # For simplicity, you can just show the notes as a comma-separated string
        selected_notes_str = ', '.join(sorted(self.selected_notes))
        self.scale_results_var.set(selected_notes_str)


 
if __name__ == "__main__":
    root = tk.Tk()
    app = FretboardApp(root)
    root.mainloop()

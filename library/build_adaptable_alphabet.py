#!/usr/bin/env python3
import csv
import sqlite3
from pathlib import Path

BASE = Path.home() / "neuroforge_core"
LIB = BASE / "library"
EXP = BASE / "exports"
DB_PATH = LIB / "adaptable_alphabet.db"

LIB.mkdir(parents=True, exist_ok=True)
EXP.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(str(DB_PATH))
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS glyphs;
DROP TABLE IF EXISTS join_sets;
DROP TABLE IF EXISTS join_members;
DROP VIEW IF EXISTS resolved_sequences;

CREATE TABLE glyphs (
    glyph_id TEXT PRIMARY KEY,
    family TEXT NOT NULL,
    code TEXT NOT NULL,
    display_text TEXT NOT NULL,
    display_emoji TEXT,
    normalized TEXT NOT NULL,
    can_run_alone INTEGER NOT NULL,
    notes TEXT DEFAULT ''
);

CREATE TABLE join_sets (
    join_id TEXT PRIMARY KEY,
    purpose TEXT NOT NULL,
    label TEXT NOT NULL,
    description TEXT DEFAULT '',
    allow_standalone_members INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE join_members (
    join_id TEXT NOT NULL,
    position INTEGER NOT NULL,
    glyph_id TEXT NOT NULL,
    role TEXT NOT NULL,
    separator TEXT DEFAULT '',
    PRIMARY KEY (join_id, position),
    FOREIGN KEY (join_id) REFERENCES join_sets(join_id),
    FOREIGN KEY (glyph_id) REFERENCES glyphs(glyph_id)
);
""")

glyphs = []

# Letters A-Z
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    glyphs.append((
        f"letter_{ch}",
        "letter",
        ch,
        ch,
        ch,
        ch.lower(),
        1,
        "Latin uppercase letter"
    ))

# Numbers 0-9
for ch in "0123456789":
    glyphs.append((
        f"number_{ch}",
        "number",
        ch,
        ch,
        ch,
        ch,
        1,
        "Arabic numeral"
    ))

# Symbols
symbol_rows = [
    ("symbol_atom_text", "symbol", "atom_text", "⚛︎", "⚛️", "atom", 1, "Atomic text form"),
    ("symbol_atom_emoji", "symbol", "atom_emoji", "⚛️", "⚛️", "atom_emoji", 1, "Atomic emoji form"),

    ("symbol_twin_text", "symbol", "twin_text", "♊︎", "♊️", "twin", 1, "Twin text form"),
    ("symbol_twin_emoji", "symbol", "twin_emoji", "♊️", "♊️", "twin_emoji", 1, "Twin emoji form"),

    ("symbol_infinity_text", "symbol", "infinity_text", "∞", "♾️", "infinity", 1, "Infinity text form"),
    ("symbol_infinity_emoji", "symbol", "infinity_emoji", "♾️", "♾️", "infinity_emoji", 1, "Infinity emoji form"),

    ("symbol_engine", "symbol", "engine", "⚙︎", "⚙️", "engine", 1, "Engine mark"),
    ("symbol_library", "symbol", "library", "📚", "📚", "library", 1, "Library mark"),

    ("symbol_workbench", "symbol", "workbench", "🪑", "🪑", "workbench", 1, "Workbench mark"),
    ("symbol_workbench_wheel", "symbol", "workbench_wheel", "☸︎", "☸️", "workbench_wheel", 1, "Wheel for the Workbench"),

    ("symbol_canvas", "symbol", "canvas", "🎨", "🎨", "canvas", 1, "Canvas mark"),
    ("symbol_dashboard", "symbol", "dashboard", "🪬", "🪬", "dashboard", 1, "Dashboard mark"),
    ("symbol_cloud", "symbol", "cloud", "☁", "☁", "cloud", 1, "Cloud bridge mark"),
    ("symbol_lab", "symbol", "lab", "🔬", "🔬", "lab", 1, "Lab mark"),
    ("symbol_orchard", "symbol", "orchard", "🏝️", "🏝️", "orchard", 1, "Orchard mark"),
    ("symbol_core", "symbol", "core", "❇️", "❇️", "core", 1, "Core declaration mark")
]
glyphs.extend(symbol_rows)

cur.executemany("""
INSERT INTO glyphs (
    glyph_id, family, code, display_text, display_emoji, normalized, can_run_alone, notes
) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", glyphs)

join_sets = [
    ("JOIN_ENGINE_CORE", "brand", "Engine Core", "Core engine signature", 1),
    ("JOIN_LIBRARY_CORE", "archive", "Library Core", "Archive signature", 1),
    ("JOIN_WORKBENCH_CORE", "work", "Workbench Core", "Workbench signature", 1),
    ("JOIN_SYMBOL_CONTINUITY", "symbolic", "Symbol Continuity", "Atom to Twin to Infinity", 1),
    ("JOIN_MMS_768", "runtime", "MMS-768", "Runtime marker", 1)
]
cur.executemany("""
INSERT INTO join_sets (join_id, purpose, label, description, allow_standalone_members)
VALUES (?, ?, ?, ?, ?)
""", join_sets)

join_members = [
    ("JOIN_ENGINE_CORE", 1, "symbol_engine", "prefix", " "),
    ("JOIN_ENGINE_CORE", 2, "letter_N", "sequence", ""),
    ("JOIN_ENGINE_CORE", 3, "letter_F", "sequence", ""),
    ("JOIN_ENGINE_CORE", 4, "letter_E", "sequence", ""),

    ("JOIN_LIBRARY_CORE", 1, "symbol_library", "prefix", " "),
    ("JOIN_LIBRARY_CORE", 2, "letter_L", "sequence", ""),
    ("JOIN_LIBRARY_CORE", 3, "letter_I", "sequence", ""),
    ("JOIN_LIBRARY_CORE", 4, "letter_B", "sequence", "_"),
    ("JOIN_LIBRARY_CORE", 5, "number_2", "sequence", ""),
    ("JOIN_LIBRARY_CORE", 6, "letter_T", "sequence", ""),
    ("JOIN_LIBRARY_CORE", 7, "letter_B", "sequence", ""),

    ("JOIN_WORKBENCH_CORE", 1, "symbol_workbench_wheel", "prefix", " "),
    ("JOIN_WORKBENCH_CORE", 2, "symbol_workbench", "prefix", " "),
    ("JOIN_WORKBENCH_CORE", 3, "letter_W", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 4, "letter_O", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 5, "letter_R", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 6, "letter_K", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 7, "letter_B", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 8, "letter_E", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 9, "letter_N", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 10, "letter_C", "sequence", ""),
    ("JOIN_WORKBENCH_CORE", 11, "letter_H", "sequence", ""),

    ("JOIN_SYMBOL_CONTINUITY", 1, "symbol_atom_text", "sequence", " "),
    ("JOIN_SYMBOL_CONTINUITY", 2, "symbol_twin_text", "sequence", " "),
    ("JOIN_SYMBOL_CONTINUITY", 3, "symbol_infinity_text", "sequence", ""),

    ("JOIN_MMS_768", 1, "letter_M", "sequence", ""),
    ("JOIN_MMS_768", 2, "letter_M", "sequence", ""),
    ("JOIN_MMS_768", 3, "letter_S", "sequence", "-"),
    ("JOIN_MMS_768", 4, "number_7", "sequence", ""),
    ("JOIN_MMS_768", 5, "number_6", "sequence", ""),
    ("JOIN_MMS_768", 6, "number_8", "sequence", "")
]
cur.executemany("""
INSERT INTO join_members (join_id, position, glyph_id, role, separator)
VALUES (?, ?, ?, ?, ?)
""", join_members)

cur.executescript("""
CREATE VIEW resolved_sequences AS
SELECT
    jm.join_id,
    js.purpose,
    js.label,
    GROUP_CONCAT(g.display_text || jm.separator, '') AS resolved_text
FROM join_members jm
JOIN glyphs g ON g.glyph_id = jm.glyph_id
JOIN join_sets js ON js.join_id = jm.join_id
GROUP BY jm.join_id, js.purpose, js.label
ORDER BY jm.join_id;
""")

conn.commit()

with open(EXP / "glyphs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["glyph_id", "family", "code", "display_text", "display_emoji", "normalized", "can_run_alone", "notes"])
    for row in cur.execute("""
        SELECT glyph_id, family, code, display_text, display_emoji, normalized, can_run_alone, notes
        FROM glyphs
        ORDER BY family, code
    """):
        writer.writerow(row)

with open(EXP / "join_sets.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["join_id", "purpose", "label", "description", "allow_standalone_members"])
    for row in cur.execute("""
        SELECT join_id, purpose, label, description, allow_standalone_members
        FROM join_sets
        ORDER BY join_id
    """):
        writer.writerow(row)

with open(EXP / "join_members.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["join_id", "position", "glyph_id", "role", "separator"])
    for row in cur.execute("""
        SELECT join_id, position, glyph_id, role, separator
        FROM join_members
        ORDER BY join_id, position
    """):
        writer.writerow(row)

with open(EXP / "resolved_sequences.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["join_id", "purpose", "label", "resolved_text"])
    for row in cur.execute("""
        SELECT join_id, purpose, label, resolved_text
        FROM resolved_sequences
        ORDER BY join_id
    """):
        writer.writerow(row)

print(f"Database written to: {DB_PATH}")
print(f"Exports written to: {EXP}")

conn.close()

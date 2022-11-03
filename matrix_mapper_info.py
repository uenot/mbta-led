import json
import pathlib

stop_coordinates = {
    "Wonderland": (62, 7),
    "Revere Beach": (60, 9),
    "Beachmont": (58, 11),
    "Suffolk Downs": (56, 13),
    "Orient Heights": (54, 15),
    "Wood Island": (52, 17),
    "Airport": (50, 19),
    "Maverick": (48, 21),
    "Aquarium": (45, 24),
    "State": (43, 26),
    "Government Center": (41, 24),
    "Bowdoin": (39, 22),

    "Oak Grove": (43, 3),
    "Malden Center": (43, 5),
    "Wellington": (43, 7),
    "Assembly": (43, 9),
    "Sullivan": (43, 11),
    "Community College": (43, 13),
    "North Station": (43, 19),
    "Haymarket": (43, 21),
    "State": (43, 26),
    "Downtown Crossing": (41, 28),
    "Chinatown": (39, 30),
    "Tufts Medical Center": (37, 32),
    "Back Bay": (35, 34),
    "Massachusetts Avenue": (33, 36),
    "Ruggles": (31, 38),
    "Roxbury Crossing": (29, 40),
    "Jackson Square": (27, 42),
    "Stony Brook": (25, 44),
    "Green Street": (23, 46),
    "Forest Hills": (21, 48),

    "Alewife": (23, 10),
    "Davis": (25, 12),
    "Porter": (27, 14),
    "Harvard": (29, 16),
    "Central": (31, 18),
    "Kendall/MIT": (33, 20),
    "Charles/MGH": (37, 24),
    "Park Street": (39, 26),
    "Downtown Crossing": (41, 28),
    "South Station": (44, 31),
    "Broadway": (46, 35),
    "Andrew": (46, 37),
    "JFK/UMass": (46, 39),
    "Savin Hill": (44, 42),
    "Fields Corner": (44, 44),
    "Shawmut": (44, 46),
    "Ashmont": (44, 48),
    "North Quincy": (50, 43),
    "Wollaston": (53, 46),
    "Quincy Center": (56, 49),
    "Quincy Adams": (59, 52),
    "Braintree": (59, 56),

    "Medford/Tufts": (27, 3),
    "Ball Square": (29, 5),
    "Magoun Square": (31, 7),
    "Gilman Square": (33, 9),
    "East Somerville": (35, 11),
    "Union Square": (35, 15),
    "Lechmere": (39, 15),
    "Science Park/West End": (41, 17),
    "North Station": (43, 19),
    "Haymarket": (43, 21),
    "Government Center": (41, 24),
    "Park Street": (39, 26),
    "Boylston": (37, 28),
    "Arlington": (34, 28),
    "Copley": (31, 28),
    "Hynes Convention Center": (28, 28),
    "Kenmore": (25, 28),

    "Prudential": (30, 30),
    "Symphony": (30, 33),
    "Northeastern": (29, 34),
    "Museum of Fine Arts": (28, 35),
    "Longwood Medical Area": (27, 36),
    "Brigham Circle": (26, 37),
    "Fenwood Road": (25, 38),
    "Mission Park": (24, 39),
    "Riverway": (23, 40),
    "Back of the Hill": (22, 41),
    "Heath Street": (21, 42),

    "Blandford Street": (24, 26),
    "BU East": (23, 25),
    "BU Central": (22, 24),
    "Amory Street": (21, 23),
    "Babcock Street": (20, 22),
    "Packard's Corner": (19, 21),
    "Harvard Avenue": (17, 20),
    "Griggs Street": (15, 21),
    "Allston Street": (14, 22),
    "Warren Street": (13, 23),
    "Washington Street": (12, 24),
    "Sutherland Road": (11, 25),
    "Chiswick Road": (10, 26),
    "Chestnut Hill Avenue": (9, 27),
    "South Street": (8, 28),
    "Boston College": (6, 29),

    "Saint Mary's Street": (21, 27),
    "Hawes Street": (20, 26),
    "Kent Street": (18, 25),
    "Saint Paul Street": (16, 26),
    "Coolidge Corner": (15, 27),
    "Summit Avenue": (14, 28),
    "Brandon Hall": (13, 29),
    "Fairbanks Street": (12, 30),
    "Washington Square": (11, 31),
    "Tappan Street": (10, 32),
    "Dean Road": (9, 33),
    "Englewood Avenue": (8, 34),
    "Cleveland Circle": (6, 35),

    "Fenway": (23, 30),
    "Longwood": (22, 31),
    "Brookline Village": (21, 32),
    "Brookline Hills": (20, 33),
    "Beaconsfield": (19, 34),
    "Reservoir": (18, 35),
    "Chestnut Hill": (17, 36),
    "Newton Centre": (16, 37),
    "Newton Highlands": (15, 38),
    "Eliot": (14, 39),
    "Waban": (13, 40),
    "Woodland": (12, 41),
    "Riverside": (10, 42)
}

colors = {
    "Red": (218, 41, 28),
    "Mattapan": (218, 41, 28),
    "Orange": (237, 139, 0),
    "Blue": (0, 61, 165),
    "Green": (0, 132, 61)
}

text = [
    (2, 56), (2, 57), (2, 58), (2, 59), (2, 60), (2, 61), (2, 62), (2, 63),
    (3, 57), (3, 58), (4, 59), (4, 60), (5, 57), (5, 58),
    (6, 56), (6, 57), (6, 58), (6, 59), (6, 60), (6, 61), (6, 62), (6, 63),

    (8, 56), (8, 57), (8, 58), (8, 59), (8, 60), (8, 61), (8, 62), (8, 63),
    (9, 56), (10, 56), (11, 57), (11, 58), (9, 59), (10, 59),
    (11, 60), (11, 61), (11, 62), (9, 63), (10, 63),

    (13, 56), (14, 56), (15, 56), (16, 56), (17, 56),
    (15, 57), (15, 58), (15, 59), (15, 60), (15, 61), (15, 62), (15, 63),

    (19, 63), (19, 62), (19, 61), (20, 60), (20, 59), (20, 58), (21, 57), (21, 56),
    (22, 58), (22, 59), (22, 60), (23, 61), (23, 62), (23, 63), (21, 60),

    (25, 56), (25, 57), (25, 58), (25, 59), (25, 60), (25, 61), (25, 62), (25, 63),
    (26, 63), (27, 63), (28, 63), (29, 63),

    (31, 56), (31, 57), (31, 58), (31, 59), (31, 60), (31, 61), (31, 62), (31, 63),
    (32, 56), (33, 56), (34, 56), (35, 56),
    (32, 59), (33, 59), (34, 59), (35, 59),
    (32, 63), (33, 63), (34, 63), (35, 63),

    (37, 56), (37, 57), (37, 58), (37, 59), (37, 60), (37, 61), (37, 62), (37, 63),
    (38, 56), (39, 56), (40, 56), (38, 63), (39, 63), (40, 63),
    (41, 57), (41, 58), (41, 59), (41, 60), (41, 61), (41, 62),

    (45, 56), (45, 57), (45, 58), (45, 59), (46, 57), (47, 57), (47, 58), (47, 59), (46, 59),
    
    (49, 57), (51, 57), (50, 58), (49, 59),

    (45, 61), (45, 62), (45, 63), (46, 63), (47, 63), (47, 62), (47, 61),

    (51, 61), (50, 61), (49, 61), (49, 62), (49, 63), (50, 63), (51, 63),

    (53, 63), (53, 62), (53, 61), (54, 61), (55, 61), (55, 62), (55, 63),

    (57, 61), (57, 62), (57, 63), (58, 63), (59, 63), (59, 62), (59, 61), (58, 61),

    (62, 60), (62, 61), (62, 62), (62, 63), (61, 61), (63, 61)
]

if __name__ == "__main__":
    shifted_stops = {k: (x-1, y-1) for k, (x, y) in stop_coordinates.items()}
    shifted_text = [(x-1, y-1) for (x, y) in text]

    data_path = pathlib.Path('data')
    data_path.mkdir(parents=True, exist_ok=True)

    with (data_path / 'stops.json').open('w') as f:
        json.dump(shifted_stops, f, indent=2)

    with (data_path / 'colors.json').open('w') as f:
        json.dump(colors, f, indent=2)
    
    with (data_path / 'text.json').open('w') as f:
        json.dump(shifted_text, f, indent=2)
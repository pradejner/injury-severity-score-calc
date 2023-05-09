# Calculate ISS for the occupants in the example input
def calculate_injury_severity_scores(occupants_ais_scores):
    iss_list = []

    for ais_scores in occupants_ais_scores:
        if len(ais_scores) != 6:
            raise ValueError("Input dict should contain AIS scores for 6 body regions")

        # Extract the top 3 highest AIS scores from different body regions
        top_3_ais_scores = sorted(ais_scores.values(), reverse=True)[:3]
        
        iss = sum(score ** 2 for score in top_3_ais_scores)
        iss_list.append(iss)

    return iss_list

# Interpret ISS scores and classify injury severity for each occupant
def interpret_iss_scores(iss_list):
    interpreted_scores = []

    for iss in iss_list:
        severity = 'Severely Injured' if iss > 15 else 'Not Severely Injured'
        interpreted_scores.append({'ISS': iss, 'Severity': severity})

    return interpreted_scores

occupants_ais_scores_example = [
    {'Head': 4, 'Face': 1, 'Chest': 2, 'Abdomen': 2, 'Extremities': 3, 'External': 1},
    {'Head': 0, 'Face': 0, 'Chest': 0, 'Abdomen': 0, 'Extremities': 0, 'External': 1}
]

iss_list_example = calculate_injury_severity_scores(occupants_ais_scores_example)
interpreted_iss_list_example = interpret_iss_scores(iss_list_example)

print(f"Injury Severity Scores (ISS) and classifications for the given occupants: {interpreted_iss_list_example}")



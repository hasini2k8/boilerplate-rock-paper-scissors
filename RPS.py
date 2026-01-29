def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) == 0:
        return "R"

    def beat(move):
        return {"R": "P", "P": "S", "S": "R"}[move]

    quincy_cycle = ["R", "P", "P", "S", "R", "S"]
    if len(opponent_history) >= 6:
        last6 = opponent_history[-6:]
        if last6 == quincy_cycle:
            # Predict next in cycle
            next_index = (len(opponent_history)) % 6
            return beat(quincy_cycle[next_index])

    if len(opponent_history) >= 3:
        if opponent_history[-1] == opponent_history[-2] == opponent_history[-3]:
            return beat(opponent_history[-1])

    if len(opponent_history) >= 3:
        last_two = tuple(opponent_history[-2:])
        transitions = {}

        for i in range(len(opponent_history) - 2):
            key = (opponent_history[i], opponent_history[i+1])
            next_move = opponent_history[i+2]
            if key not in transitions:
                transitions[key] = {"R": 0, "P": 0, "S": 0}
            transitions[key][next_move] += 1

        if last_two in transitions:
            predicted = max(transitions[last_two], key=transitions[last_two].get)
            return beat(predicted)

    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1

    predicted = max(freq, key=freq.get)
    return beat(predicted)

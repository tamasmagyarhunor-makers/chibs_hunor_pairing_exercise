def names(participants):
    if len(participants) == 1:
        return participants[0]
    elif len(participants) == 2:
        return participants[0] + " & " + participants[1]
    elif len(participants) > 2:
        return participants[0] + ", " + " & ".join(participants[-2:])
    return ""
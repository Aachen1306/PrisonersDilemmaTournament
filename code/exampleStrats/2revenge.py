def strategy(history, memory):
    choice = 1
    if memory:
      memory = False
      choice = 0
    else if history.shape[1] >= 1 and history[1,-1] == 0: # Choose to defect if and only if the opponent just defected.
        choice = 0
        memory = True
    return choice, None

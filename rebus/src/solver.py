REMOVE_LETTER = "'"

def solve(rebus: str) -> str:
    remove_cnt = 0
    answer = []

    for letter in rebus:
        if letter == REMOVE_LETTER:
            remove_cnt += 1
        else:
            if remove_cnt > 0:
                remove_cnt -= 1
            else:
                answer.append(letter)

    if remove_cnt > len(answer):
        raise ValueError(f'Rebus: <{rebus}> is invalid')
    if remove_cnt > 0:
        answer = answer[:-remove_cnt]
    return ''.join(answer)

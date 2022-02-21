from typing import List

from src.solver import solve


# print(solve("'''новосёл"))
# print(solve("макияж'''"))


def run():
    rebuses = read_rebuses()
    answers = solve_rebuses(rebuses)
    write_answers(answers)


def read_rebuses() -> List[str]:
    with open('data/input.txt', 'r') as f:
        rebuses = f.readlines()
    return rebuses


def solve_rebuses(rebuses: List[str]) -> List[str]:
    answers = []
    for rebus in rebuses:
        answers.append(
            solve(rebus.strip())
        )
    return answers

    return [
        solve(rebus.strip()) for rebus in rebuses
    ]


def write_answers(answers: List[str]) -> None:
    # lines = map(
    #     lambda line: f'{line}\n',
    #     answers
    # )
    # with open('data/output.txt', 'w') as f:
    #     f.writelines(lines)

    lines = '\n'.join(answers)
    with open('data/output.txt', 'w') as f:
        f.write(lines)


if __name__ == '__main__':
    run()

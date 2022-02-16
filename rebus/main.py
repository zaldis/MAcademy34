from typing import List

from src.solver import solve as solve_rebus


def run():
    examples = read_examples()
    answers = solve(examples)
    write_answers(answers)


def read_examples():
    with open('data/input.txt', 'r') as f:
        examples = f.readlines()
    return examples


def solve(examples: List[str]) -> List[str]:
    answers = []
    for example in examples:
        answers.append(solve_rebus(example.strip()))
    return answers


def write_answers(answers: List[str]) -> None:
    lines = '\n'.join(answers)
    with open('data/output.txt', 'w') as f:
        f.write(lines)


if __name__ == '__main__':
    run()

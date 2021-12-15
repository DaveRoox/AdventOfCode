import sys
from pathlib import Path


def template():
    return """def part1(v):
    pass


def part2(v):
    pass


with open("input/day{}.txt") as f:
    v = list(map(lambda l: l.replace('\\n', ''), f.readlines()))
    part1(v)
    part2(v)
"""


flags = dict(map(lambda l: tuple(l.split('=')), sys.argv[1:]))
year = int(flags['-year'])
start_day = int(flags['-day']) if '-day' in flags else int(flags['-from'])
end_day = int(flags['-day']) if '-day' in flags else int(flags['-to'])
Path('./{}/input'.format(year)).mkdir(parents=True, exist_ok=True)
for day in range(start_day, end_day + 1):
    filepath = Path('./{}/day{}.py'.format(year, day))
    filepath.touch(exist_ok=True)
    filepath.write_text(template().format(day))
    Path('./{}/input/day{}.txt'.format(year, day)).touch(exist_ok=True)
print('Completed.')

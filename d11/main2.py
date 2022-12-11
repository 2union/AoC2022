import heapq
import math
from dataclasses import dataclass, field


@dataclass
class Monkey:
    fn: str = ''
    divisible: int = 0
    true_position: int = 0
    false_position: int = 0
    items: list[int] = field(default_factory=list)
    inspected: int = 0

monkeys = []

with open('input') as f:
    monkey_buffer = None
    for line in f:
        if line[:6] == 'Monkey':
            if monkey_buffer:
                monkeys.append(monkey_buffer)
            monkey_buffer = Monkey()
        line_elements = line.strip().split()
        match line_elements:
            case 'Starting', 'items:', *items:
                monkey_buffer.items = list(map(int, [i.replace(',', '') for i in items]))
            case 'Operation:', 'new', '=', *formula:
                monkey_buffer.fn = 'lambda old: ' + ' '.join(formula)
            case 'Test:', 'divisible', 'by', divisible:
                monkey_buffer.divisible = int(divisible)
            case 'If', 'true:', 'throw', 'to', 'monkey', monkey:
                monkey_buffer.true_position = int(monkey)
            case 'If', 'false:', 'throw', 'to', 'monkey', monkey:
                monkey_buffer.false_position = int(monkey)
    monkeys.append(monkey_buffer)

monkeys_mod = math.prod([i.divisible for i in monkeys])

for i in range(10000):
    for monkey in monkeys:
        fn = eval(monkey.fn)
        for item in monkey.items:
            wory_level = fn(item) % monkeys_mod
            if wory_level % monkey.divisible:
                monkeys[monkey.false_position].items.append(wory_level)
            else:
                monkeys[monkey.true_position].items.append(wory_level)
            monkey.inspected += 1
        monkey.items = []

print(math.prod(heapq.nlargest(2, [i.inspected for i in monkeys])))

# Part 1
lines = [line.strip() for line in open("inputday11.txt")]

monkeys = [[]]
for i in lines:
    if not i:
        monkeys.append([])
    else:
        monkeys[-1].append(i)

monkey_dict = {}
for monkey in monkeys:
    number = monkey[0].split()[1].split(":")[0]
    monkey_dict[str(number)] = {}
    monkey_dict[str(number)]["worrylevel"] = monkey[1].split(": ")[1].split(", ")
    monkey_dict[str(number)]["operand"] = monkey[2].split("= ")[1].split("old ")[1].split(" ")[0]
    monkey_dict[str(number)]["nr_operand"] = monkey[2].split("= ")[1].split("old ")[1].split(" ")[1]
    monkey_dict[str(number)]["test"] = monkey[3].split("by ")[1]
    monkey_dict[str(number)]["throw"] = monkey[4].split("monkey ")[1], monkey[5].split("monkey ")[1]
    monkey_dict[str(number)]["nr_inspected"] = 0

for i in range(20):
    for monkey in monkey_dict:        
        for _ in range(len(monkey_dict[monkey]["worrylevel"])):
            monkey_dict[monkey]["nr_inspected"] += 1
            item = monkey_dict[monkey]["worrylevel"].pop()
            # Performing operation
            if monkey_dict[monkey]["operand"] == "*":
                if monkey_dict[monkey]["nr_operand"] == "old":
                    new_item = int(item) * int(item)

                else:
                    new_item = int(item) * int(monkey_dict[monkey]["nr_operand"])
            elif monkey_dict[monkey]["operand"] == "+":
                if monkey_dict[monkey]["nr_operand"] == "old":
                    new_item = int(item) + int(item)
                else:
                    new_item = int(item) + int(monkey_dict[monkey]["nr_operand"])
            # Monkey gets bored
            new_worry = new_item // 3
            if new_worry % int(monkey_dict[monkey]["test"]) == 0:
                monkey_dict[str(monkey_dict[monkey]["throw"][0])]["worrylevel"].append(new_worry)
            else:
                monkey_dict[str(monkey_dict[monkey]["throw"][1])]["worrylevel"].append(new_worry)

monkey_business = []
for monkey in monkey_dict:
    monkey_business.append(monkey_dict[monkey]["nr_inspected"])
print("Part 1: ", sorted(monkey_business, reverse=True)[0] * sorted(monkey_business, reverse=True)[1])
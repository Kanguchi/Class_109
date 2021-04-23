import random
import statistics
import plotly.figure_factory as ff

dice_result = []
count = []

for i in range(0, 1001):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceTotal = dice1 + dice2
    count.append(i)
    dice_result.append(diceTotal)

mean = sum(dice_result) / len(dice_result)
std_deviation = statistics.stdev(dice_result)

# middle number in data set
median = statistics.median(dice_result)
# number that occurs most often
mode = statistics.mode(dice_result)

val1 = mean + (3*std_deviation)
val2 = mean - (3*std_deviation)
num_between = 0
for i in dice_result:
    if val1 > i > val2:
        num_between += 1
percentage = 100 * (num_between/1000)
print(f"The percentage of values if: {percentage:.2f}%")


# fig = ff.create_distplot([dice_result], ["Dice Total"], show_hist=False)
# fig.show()

print(f"The mean of the data set is: {mean:.2f}")
print(f"The median of the data set is: {median:.2f}")
print(f"The mode of the data set is: {mode:.2f}")


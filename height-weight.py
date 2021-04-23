import csv
import pandas as pd
import statistics

df = pd.read_csv("height-weight.csv")

height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

mean_height = statistics.mean(height_list)
std_dev_height = statistics.stdev(height_list)

mean_weight = statistics.mean(weight_list)
std_dev_weight = statistics.stdev(weight_list)

height_dev_strt, height_dev_end = mean_height - std_dev_height, mean_height + std_dev_height
height_dev_strt2, height_dev_end2 = mean_height - 2*std_dev_height, mean_height + 2*std_dev_height
height_dev_strt3, height_dev_end3 = mean_height - 3*std_dev_height, mean_height + 3*std_dev_height
height_count1 = [result for result in height_list if result > height_dev_strt and result < height_dev_end]
height_count2 = [result for result in height_list if result > height_dev_strt2 and result < height_dev_end2]
height_count3 = [result for result in height_list if result > height_dev_strt3 and result < height_dev_end3]

weight_dev_strt, weight_dev_end = mean_weight + std_dev_weight, mean_weight - std_dev_weight


print(f"{len(height_count1)/len(height_list) * 100}% of data for height lies in 1 statdard deviation")
print("{}% of data for height lies in 2 statdard deviations".format(len(height_count2)/len(height_list) * 100))
print(f"{len(height_count3)/len(height_list) * 100}% of data for height lies in 3 statdard deviations")
print()


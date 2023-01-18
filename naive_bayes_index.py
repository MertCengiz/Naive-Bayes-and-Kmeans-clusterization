import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
height_input = input('Please enter an height in centimetres: ')
weight_input = input('Please enter an weight in kilograms: ')
while True:
    gender_input = input('Please choose "female" or "male": ')
    if gender_input.lower() == 'female' or gender_input.lower() == 'male':
        break
    else:
        print('Wrong input; try again.', end=' ')
zero_count = 0
one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
female_zero_count = 0
male_zero_count = 0
female_one_count = 0
male_one_count = 0
female_two_count = 0
male_two_count = 0
female_three_count = 0
male_three_count = 0
female_four_count = 0
male_four_count = 0
female_five_count = 0
male_five_count = 0
zero_height_list = []
zero_weight_list = []
one_height_list = []
one_weight_list = []
two_height_list = []
two_weight_list = []
three_height_list = []
three_weight_list = []
four_height_list = []
four_weight_list = []
five_height_list = []
five_weight_list = []
index_list = []
for l in range(len(dataframe['Index'])):
    if dataframe['Index'][l] == 0:
        zero_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_zero_count += 1
        if str(dataframe['Height'][l]) == height_input:
            zero_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            zero_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_zero_count += 1
    if dataframe['Index'][l] == 1:
        one_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_one_count += 1
        if str(dataframe['Height'][l]) == height_input:
            one_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            one_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_one_count += 1
    if dataframe['Index'][l] == 2:
        two_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_two_count += 1
        if str(dataframe['Height'][l]) == height_input:
            two_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            two_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_two_count += 1
    if dataframe['Index'][l] == 3:
        three_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_three_count += 1
        if str(dataframe['Height'][l]) == height_input:
            three_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            three_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_three_count += 1
    if dataframe['Index'][l] == 4:
        four_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_four_count += 1
        if str(dataframe['Height'][l]) == height_input:
            four_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            four_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_four_count += 1
    if dataframe['Index'][l] == 5:
        five_count += 1
        if dataframe['Gender'][l].lower() == 'female':
            female_five_count += 1
        if str(dataframe['Height'][l]) == height_input:
            five_height_list.append(dataframe['Height'][l])
        if str(dataframe['Weight'][l]) == weight_input:
            five_weight_list.append(dataframe['Weight'][l])
        if dataframe['Gender'][l].lower() == 'male':
            male_five_count += 1
zero_num_probability = zero_count / len(dataframe['Index'])
one_num_probability = one_count / len(dataframe['Index'])
two_num_probability = two_count / len(dataframe['Index'])
three_num_probability = three_count / len(dataframe['Index'])
four_num_probability = four_count / len(dataframe['Index'])
five_num_probability = five_count / len(dataframe['Index'])
female_probability_zero = female_zero_count / (female_zero_count+male_zero_count)
male_probability_zero = male_zero_count / (female_zero_count+male_zero_count)
female_probability_one = female_one_count / (female_one_count+male_one_count)
male_probability_one = male_one_count / (female_one_count+male_one_count)
female_probability_two = female_two_count / (female_two_count+male_two_count)
male_probability_two = male_two_count / (female_two_count+male_two_count)
female_probability_three = female_three_count / (female_three_count+male_three_count)
male_probability_three = male_three_count / (female_three_count+male_three_count)
female_probability_four = female_four_count / (female_four_count+male_four_count)
male_probability_four = male_four_count / (female_four_count+male_four_count)
female_probability_five = female_five_count / (female_five_count+male_five_count)
male_probability_five = male_five_count / (female_five_count+male_five_count)
if dataframe['Gender'][l].lower() == 'female':
    zero_height_probability = len(zero_height_list) / zero_count
    zero_weight_probability = len(zero_weight_list) / zero_count
    one_height_probability = len(one_height_list) / one_count
    one_weight_probability = len(one_weight_list) / one_count
    two_height_probability = len(two_height_list) / two_count
    two_weight_probability = len(two_weight_list) / two_count
    three_height_probability = len(three_height_list) / three_count
    three_weight_probability = len(three_weight_list) / three_count
    four_height_probability = len(four_height_list) / four_count
    four_weight_probability = len(four_weight_list) / four_count
    five_height_probability = len(five_height_list) / five_count
    five_weight_probability = len(five_weight_list) / five_count
    zero_naive_bayes = zero_num_probability*zero_height_probability*zero_weight_probability*female_probability_zero
    one_naive_bayes = one_num_probability*one_height_probability*one_weight_probability*female_probability_one
    two_naive_bayes = two_num_probability*two_height_probability*two_weight_probability*female_probability_two
    three_naive_bayes = three_num_probability*three_height_probability*three_weight_probability*female_probability_three
    four_naive_bayes = four_num_probability*four_height_probability*four_weight_probability*female_probability_four
    five_naive_bayes = five_num_probability*five_height_probability*five_weight_probability*female_probability_five
if dataframe['Gender'][l].lower() == 'male':
    zero_height_probability = len(zero_height_list) / zero_count
    zero_weight_probability = len(zero_weight_list) / zero_count
    one_height_probability = len(one_height_list) / one_count
    one_weight_probability = len(one_weight_list) / one_count
    two_height_probability = len(two_height_list) / two_count
    two_weight_probability = len(two_weight_list) / two_count
    three_height_probability = len(three_height_list) / three_count
    three_weight_probability = len(three_weight_list) / three_count
    four_height_probability = len(four_height_list) / four_count
    four_weight_probability = len(four_weight_list) / four_count
    five_height_probability = len(five_height_list) / five_count
    five_weight_probability = len(five_weight_list) / five_count
    zero_naive_bayes = zero_num_probability*zero_height_probability*zero_weight_probability*male_probability_zero
    one_naive_bayes = one_num_probability*one_height_probability*one_weight_probability*male_probability_one
    two_naive_bayes = two_num_probability*two_height_probability*two_weight_probability*male_probability_two
    three_naive_bayes = three_num_probability*three_height_probability*three_weight_probability*male_probability_three
    four_naive_bayes = four_num_probability*four_height_probability*four_weight_probability*male_probability_four
    five_naive_bayes = five_num_probability*five_height_probability*five_weight_probability*male_probability_five
naive_bayes_list=[zero_naive_bayes,one_naive_bayes,two_naive_bayes,three_naive_bayes,four_naive_bayes,five_naive_bayes]
# print(naive_bayes_list)
print(f'Index {naive_bayes_list.index(max(naive_bayes_list))} has the greatest probability percentage.')
print('Graph in progress; please wait...')
ax = plt.axes(projection='3d')
for dot in range(len(dataframe['Gender'])):
    x = dataframe['Height'][dot]
    y = dataframe['Weight'][dot]
    if dataframe['Gender'][dot] == 'Female':
        z = 0
    if dataframe['Gender'][dot] == 'Male':
        z = 1
    if dataframe['Index'][dot] == 0:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])
            # ax.scatter3D(x, y, z, color='red', label='Index 0')
            index_zero = ax.scatter3D(x, y, z, color='red', label='Index 0')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='red')
    if dataframe['Index'][dot] == 1:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])
            # ax.scatter3D(x, y, z, color='blue', label='Index 1')
            index_one = ax.scatter3D(x, y, z, color='blue', label='Index 1')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='blue')
    if dataframe['Index'][dot] == 2:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])
            # ax.scatter3D(x, y, z, color='green', label='Index 2')
            index_two = ax.scatter3D(x, y, z, color='green', label='Index 2')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='green')
    if dataframe['Index'][dot] == 3:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])
            # ax.scatter3D(x, y, z, color='orange', label='Index 3')
            index_three = ax.scatter3D(x, y, z, color='orange', label='Index 3')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='orange')
    if dataframe['Index'][dot] == 4:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])

            index_four = ax.scatter3D(x, y, z, color='cyan', label='Index 4')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='cyan')
    if dataframe['Index'][dot] == 5:
        if dataframe['Index'][dot] not in index_list:
            index_list.append(dataframe['Index'][dot])
            index_five = ax.scatter3D(x, y, z, color='chocolate', label='Index 5')
        if dataframe['Index'][dot] in index_list:
            ax.scatter3D(x, y, z, color='chocolate')
g = 1 if gender_input.lower() == 'male' else 0
# if naive_bayes_list.index(max(naive_bayes_list)) == 0:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='red', marker='*', s=300)
# if naive_bayes_list.index(max(naive_bayes_list)) == 1:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='blue', marker='*', s=300)
# if naive_bayes_list.index(max(naive_bayes_list)) == 2:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='green', marker='*', s=300)
# if naive_bayes_list.index(max(naive_bayes_list)) == 3:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='orange', marker='*', s=300)
# if naive_bayes_list.index(max(naive_bayes_list)) == 4:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='olive', marker='*', s=300)
# if naive_bayes_list.index(max(naive_bayes_list)) == 5:
#     ax.scatter3D(float(height_input), float(weight_input), g, color='chocolate', marker='*', s=300)
the_point = ax.scatter3D(float(height_input), float(weight_input), g, color='black', marker='*', s=30, label='The Input Point')
ax.legend(loc='upper right', bbox_to_anchor=(1.0, 0.5, 0.5, 0.5), handles=[index_zero, index_one, index_two, index_three, index_four, index_five, the_point])
ax.set_xlabel('Height (in centimetres)')
ax.set_ylabel('Weight (in kilograms)')
ax.set_zlabel('Gender')
plt.title('500 Person Gender-Height-Weight-Body Mass Index Graph', fontweight='bold')
print('The graph is being printed.')
plt.show()

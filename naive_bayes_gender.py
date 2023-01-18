import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
datatable_with_index = pd.read_csv('500_Person_Gender_Height_Weight_Index.csv')
datatable = datatable_with_index[['Gender', 'Height', 'Weight']]
print(datatable)
print(datatable.isnull().sum())
height_input = input('Please enter an height in centimetres: ')
weight_input = input('Please enter an weight in kilograms: ')
male_height_list = []
male_weight_list = []
female_height_list = []
female_weight_list = []
female_num_count = 0
female_height_count = 0
female_weight_count = 0
male_num_count = 0
male_height_count = 0
male_weight_count = 0
for g in range(len(datatable['Gender'])):
    if datatable['Gender'][g] == 'Male':
        male_num_count += 1
        male_height_list.append(datatable['Height'][g])
        male_weight_list.append(datatable['Weight'][g])
        if str(datatable['Height'][g]) == height_input:
            male_height_count += 1
        if str(datatable['Weight'][g]) == weight_input:
            male_weight_count += 1
    if datatable['Gender'][g] == 'Female':
        female_num_count += 1
        female_height_list.append(datatable['Height'][g])
        female_weight_list.append(datatable['Weight'][g])
        if str(datatable['Height'][g]) == height_input:
            female_height_count += 1
        if str(datatable['Weight'][g]) == weight_input:
            female_weight_count += 1
# print('Male height number is {} and weight number is {},'.format(male_height_count, male_weight_count), end=' ')
# print('whereas female height number is {} and weight number is {}.'.format(female_height_count, female_weight_count))
female_frequency = female_num_count/(female_num_count+male_num_count)
female_height_frequency = female_height_count/female_num_count
female_weight_frequency = female_weight_count/female_num_count
male_frequency = male_num_count/(female_num_count+male_num_count)
male_height_frequency = male_height_count/male_num_count
male_weight_frequency = male_weight_count/male_num_count
female_probability = female_frequency*female_height_frequency*female_weight_frequency
male_probability = male_frequency*male_height_frequency*male_weight_frequency
female_naive_bayes = female_probability/(female_probability+male_probability+(1e-14))
male_naive_bayes = male_probability/(female_probability+male_probability+(1e-14))
female_likeliness = female_height_frequency + female_weight_frequency
male_likeliness = male_height_frequency + male_weight_frequency
if male_naive_bayes == 0 and female_naive_bayes == 0:
    # print('Male likeliness: %{}, Female likeliness: %{}'.format(male_likeliness * 100, female_likeliness * 100))
    if male_height_count + male_weight_count == 0 and female_weight_count + female_height_count == 0:
        print('Unable to detect the gender.')
    else:
        if male_height_count + male_weight_count >= female_weight_count + female_height_count:
            print('This person is likely to be a male.')
        if male_height_count + male_weight_count < female_weight_count + female_height_count:
            print('This person is likely to be a female.')
else:
    # print('Male likeliness: %{}, Female likeliness: %{}'.format(male_naive_bayes * 100, female_naive_bayes * 100))
    if female_naive_bayes > male_naive_bayes:
        print('This person is likely to be a female.')
    if male_naive_bayes >= female_naive_bayes:
        print('This person is likely to be a male.')
print()
male_height_list.sort()
male_weight_list.sort()
female_height_list.sort()
female_weight_list.sort()
plt.hist(datatable['Height'], edgecolor='white')
plt.xlabel('Height (in centimetres)')
plt.ylabel('Number of occurrences')
plt.title('Graph 1: Number of Occurrences Per Height Value', fontweight='bold')
plt.show()
plt.hist(datatable['Weight'], edgecolor='white')
plt.xlabel('Weight (in kilograms)')
plt.ylabel('Number of occurrences')
plt.title('Graph 2: Number of Occurrences Per Weight Value', fontweight='bold')
plt.show()
plt.pie([male_num_count, female_num_count], labels=[f'Male: {male_num_count}', f'Female: {female_num_count}'])
plt.title('Graph 3: Gender Distribution', fontweight='bold')
plt.show()
plt.boxplot([male_height_list, female_height_list], notch=True, patch_artist=True, labels=['Males', 'Females'])
plt.title('Graph 4: Distribution of Height Among Genders', fontweight='bold')
plt.show()
plt.boxplot([male_weight_list, female_weight_list], notch=True, patch_artist=True, labels=['Males', 'Females'])
plt.title('Graph 5: Distribution of Weight Among Genders', fontweight='bold')
plt.show()
height_labels = []
h_num = min(male_height_list[0], female_height_list[0])
while True:
    if h_num + 9 < max(male_height_list[-1], female_height_list[-1]):
        height_labels.append('{}-{}'.format(h_num, h_num+9))
        h_num += 10
        continue
    if h_num + 9 >= max(male_height_list[-1], female_height_list[-1]):
        height_labels.append('{}-{}'.format(h_num, max(male_height_list[-1], female_height_list[-1])))
        break
x = np.arange(len(height_labels))
width = 0.40
fig, ax = plt.subplots()
male_height_ranges = []
female_height_ranges = []
for label in height_labels:
    male_range_list = []
    female_range_list = []
    if label[3] == '-' and label[-4] == '-':
        for val in male_height_list:
            if int(label[0]+label[1]+label[2]) <= val <= int(label[-3]+label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_height_list:
            if int(label[0]+label[1]+label[2]) <= val <= int(label[-3]+label[-2]+label[-1]):
                female_range_list.append(val)
    if label[2] == '-' and label[-3] == '-':
        for val in male_height_list:
            if int(label[0]+label[1]) <= val <= int(label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_height_list:
            if int(label[0]+label[1]) <= val <= int(label[-3]+label[-2]):
                female_range_list.append(val)
    if label[2] == '-' and label[-4] == '-':
        for val in male_height_list:
            if int(label[0]+label[1]) <= val <= int(label[-3]+label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_height_list:
            if int(label[0]+label[1]) <= val <= int(label[-3]+label[-2]+label[-1]):
                female_range_list.append(val)
    male_height_ranges.append(len(male_range_list))
    female_height_ranges.append(len(female_range_list))
rects1 = ax.bar(x-(width/2), male_height_ranges, width, label='Males')
rects2 = ax.bar(x+(width/2), female_height_ranges, width, label='Females')
ax.set_ylabel('Number of occurrences')
ax.set_title('Graph 6: Number of Occurrences Per Height Value Among Genders', fontweight='bold')
# ax.set_xticks(x, height_labels)  # In Matplolib 3.5.1 version, uncomment this.
ax.set_xticks(x)     # In Matplotlib 3.5.1 version, comment this.
ax.set_xticklabels(height_labels)    # In Matplotlib 3.5.1 version, comment this.
ax.legend()
# ax.bar_label(rects1)  # In Matplolib 3.5.1 version, uncomment this.
# ax.bar_label(rects2)  # In Matplolib 3.5.1 version, uncomment this.
fig.tight_layout()
plt.show()
weight_labels = []
w_num = min(male_weight_list[0], female_weight_list[0])
while True:
    if w_num + 19 < max(male_weight_list[-1], female_weight_list[-1]):
        weight_labels.append('{}-{}'.format(w_num, w_num+19))
        w_num += 20
        continue
    if w_num + 19 >= max(male_weight_list[-1], female_weight_list[-1]):
        weight_labels.append('{}-{}'.format(w_num, max(male_weight_list[-1], female_weight_list[-1])))
        break
x = np.arange(len(weight_labels))
width = 0.40
fig, ax = plt.subplots()
male_weight_ranges = []
female_weight_ranges = []
for label in weight_labels:
    male_range_list = []
    female_range_list = []
    if label[3] == '-' and label[-4] == '-':
        for val in male_weight_list:
            if int(label[0]+label[1]+label[2]) <= val <= int(label[-3]+label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_weight_list:
            if int(label[0]+label[1]+label[2]) <= val <= int(label[-3]+label[-2]+label[-1]):
                female_range_list.append(val)
    if label[2] == '-' and label[-3] == '-':
        for val in male_weight_list:
            if int(label[0]+label[1]) <= val <= int(label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_weight_list:
            if int(label[0]+label[1]) <= val <= int(label[-2]+label[-1]):
                female_range_list.append(val)
    if label[2] == '-' and label[-4] == '-':
        for val in male_weight_list:
            if int(label[0]+label[1]) <= val <= int(label[-3]+label[-2]+label[-1]):
                male_range_list.append(val)
        for val in female_weight_list:
            if int(label[0]+label[1]) <= val <= int(label[-3]+label[-2]+label[-1]):
                female_range_list.append(val)
    male_weight_ranges.append(len(male_range_list))
    female_weight_ranges.append(len(female_range_list))
rects1 = ax.bar(x-(width/2), male_weight_ranges, width, label='Males')
rects2 = ax.bar(x+(width/2), female_weight_ranges, width, label='Females')
ax.set_ylabel('Number of occurrences')
ax.set_title('Graph 7: Number of Occurrences Per Weight Value Among Genders', fontweight='bold')
# ax.set_xticks(x, weight_labels)  # In Matplolib 3.5.1 version, uncomment this.
ax.set_xticks(x)       # In Matplotlib 3.5.1 version, comment this.
ax.set_xticklabels(weight_labels)    # In Matplotlib 3.5.1 version, comment this.
ax.legend()
# ax.bar_label(rects1)    # In Matplolib 3.5.1 version, uncomment this.
# ax.bar_label(rects2)    # In Matplolib 3.5.1 version, uncomment this.
fig.tight_layout()
plt.show()
for c in range(len(datatable['Gender'])):
    if datatable['Gender'][c] == 'Male':
        plt.scatter(datatable['Height'][c], datatable['Weight'][c], c='blue', alpha=0.40)
    if datatable['Gender'][c] == 'Female':
        plt.scatter(datatable['Height'][c], datatable['Weight'][c], c='red', alpha=0.40)
plt.xlabel('Height in centimetres')
plt.ylabel('Weight in kilograms')
plt.title('Graph 8: Height-Weight Comparison (Blue: Males, Red: Females)', fontweight='bold')
plt.show()
ax = plt.axes(projection='3d')
for dot in range(len(datatable_with_index['Gender'])):
    x = datatable_with_index['Height'][dot]
    y = datatable_with_index['Weight'][dot]
    z = datatable_with_index['Index'][dot]
    if datatable_with_index['Gender'][dot] == 'Female':
        ax.scatter3D(x, y, z, color='red')
    if datatable_with_index['Gender'][dot] == 'Male':
        ax.scatter3D(x, y, z, color='blue')
ax.set_xlabel('Height (in centimetres)')
ax.set_ylabel('Weight (in kilograms)')
ax.set_zlabel('Index Value')
plt.title('Graph 9: Height-Weight-Index Comparison (Blue: Males, Red: Females)', fontweight='bold')
plt.show()
ax = plt.axes(projection='3d')
for dot in range(len(datatable_with_index['Gender'])):
    x = datatable_with_index['Height'][dot]
    y = datatable_with_index['Weight'][dot]
    if datatable_with_index['Gender'][dot] == 'Female':
        z = 0
    if datatable_with_index['Gender'][dot] == 'Male':
        z = 1
    # z = datatable_with_index['Gender'][dot]
    if datatable_with_index['Index'][dot] == 0:
        ax.scatter3D(x, y, z, color='red')
    if datatable_with_index['Index'][dot] == 1:
        ax.scatter3D(x, y, z, color='blue')
    if datatable_with_index['Index'][dot] == 2:
        ax.scatter3D(x, y, z, color='green')
    if datatable_with_index['Index'][dot] == 3:
        ax.scatter3D(x, y, z, color='yellow')
    if datatable_with_index['Index'][dot] == 4:
        ax.scatter3D(x, y, z, color='olive')
    if datatable_with_index['Index'][dot] == 5:
        ax.scatter3D(x, y, z, color='silver')
ax.set_xlabel('Height (in centimetres)')
ax.set_ylabel('Weight (in kilograms)')
ax.set_zlabel('Gender')
plt.title('Graph 10: Height-Weight-Gender Comparison ', fontweight='bold')
plt.show()

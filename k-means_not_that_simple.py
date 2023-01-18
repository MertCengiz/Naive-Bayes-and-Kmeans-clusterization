import random
import copy
import matplotlib.pyplot as plt

'''K-means clustering is an unsupervised clustering method which means it attempts to group similar data together, without knowing which group the data belongs to.
It works in an iterative manner:
    First, you choose some k random data points, which needs to have the same dimensionality as your data. Meaning: our dataset has the x and y coordinates, so our k points, which we will call cluster centers, centers or centroids needs to have x and y coordinates as well.
    Then you check for all your data for the Euclidean distance between each point and each center.
    Then you record somewhere which center is closest to each data point, lists can be useful here.
    Then you update the location of each center. You do this by looking at your records, and summing up all the data points belonging to a center, and dividing that sum with the number of data points belonging to that center. This is basically taking average, you are determining where the center should be moved to based on the points closest to it.
That's it, you can repeat it for a number of times; or you can repeat until there is no change for any points between two iterations.
Note that since you start from random points, which you can also modify, the algorithm does not always work out the same, and may even find results which are not very good.'''

# This video visualizing what is happening when we do this can help you understand better. https://youtu.be/nXY6PxAaOk0

# Please try to implement this yourselves or at least take a look at it when you have some free time, I implemented this using only the things you have learned in this course.


def get_l2_distance(p1, p2):
    squared_dist = 0
    for i in range(len(p1)):
        squared_dist += (p1[i] - p2[i])**2
    return squared_dist**0.5

def read_data(filepath):
    f = open(filepath, "r")
    data = []
    for line in f:
        s = line.strip()
        features = s.split(',')
        converted = [float(fv) for fv in features]
        data.append(converted)
    f.close()
    return data

def centre_find(data_length):
    center = []
    for j in range(len(data_length)):
        c = random.uniform(0, 1)
        center.append(c)
    return center

def cluster_colourization(k):
    rgb_list = []
    while True:
        choice = input('Press "r" for random selection and "w" for writing one by one: ')
        if choice.lower() == "w":
            counts = 0
            while True:
                inp = input(f'Please enter a colour except black and white ({k - counts} remaining): ')
                if inp.lower() == 'black' or inp.lower() == 'white':
                    print(f'"{inp}" is not a valid colour; try again.', end=' ')
                    continue
                if inp.lower() in rgb_list:
                    print(f'"{inp}" is already written. Please enter some other colour; try again.', end=' ')
                    continue
                rgb_list.append(inp.lower())
                counts += 1
                if counts == k:
                    break
            return rgb_list
        if choice.lower() == 'r':
            many_colours_list = ['red', 'green', 'blue', 'brown', 'purple', 'pink', 'yellow', 'cyan', 'magenta', 'gray','orange', 'navy', 'olive', 'turquoise', 'chocolate', 'palegreen', 'gold']
            for i in range(k):
                chosen = random.choice(many_colours_list)
                rgb_list.append(chosen)
                many_colours_list.remove(chosen)
            return rgb_list
        else:
            print('Incorrect input; try again.', end=' ')

def operation(filepath, iter_count, centers, colour_centres_dict, colour_points_dict):
    flag = True
    data = read_data(filepath)
    print('Operation has started.')
    while True:
        question = input('Would you like to see the progress? Please type "yes" or "no": ')
        if question.lower() == 'yes':
            break
        if question.lower() == 'no':
            flag = False
            break
        if question.lower() != 'no' or question.lower() != 'yes':
            print('Incorrect format; try again.', end=' ')
    for i in range(iter_count):
        for f in range(len(centers)):
            if flag == True:
                print("Iteration {}: center {} coordinates: {}".format(i + 1, f + 1, centers[f]))
        ownerships = []
        center_sums = [[0 for g in range(len(data[0]))] for t in range(len(centers))]
        n = 0
        for each in data:
            distances = []
            for c in centers:
                distances.append(get_l2_distance(c, each))
            min_val = min(distances)
            min_ind = distances.index(min_val)
            for key, val in colour_centres_dict.items():
                if min_ind == int(list(key)[-1]):
                    point_colour = val[1]
                    colour_points_dict[f'point{n}'] = min_ind, point_colour
                    n += 1
            ownerships.append(min_ind)
        old_centre = [copy.deepcopy(centers)]
        for j in range(len(ownerships)):
            center_sums[ownerships[j]] = [center_sums[ownerships[j]][dim] + data[j][dim] for dim in range(len(data[j]))]
        for j in range(len(center_sums)):
            if ownerships.count(j) != 0:
                centers[j] = [center_sums[j][m] / ownerships.count(j) for m in range(len(center_sums[j]))]
        if old_centre == [centers]:
            print('Optimum point found in Iteration {}'.format(i+1))
            break
    print('Operation has ended.')

def visualization(data, colour_points_dict, centers, filepath, k, iter_count):
    try:
        print('The graph is being prepared. Please wait...')
        for m in range(len(data)):
            plt.scatter(data[m][0], data[m][1], c=colour_points_dict[f'point{m}'][1], alpha=0.20)
        for l in range(len(centers)):
            plt.scatter(centers[l][0], centers[l][1], c='black', alpha=1)
        plt.show()
    except:
        print('Something wrong occurred; try again.', end=' ')
        k_means(filepath, k, iter_count)

def k_means(filepath, k, iter_count):
    data = read_data(filepath)
    centers = []
    colour_centres_dict = {}
    colour_points_dict = {}
    for i in range(k):
        center = centre_find(data[0])
        centers.append(center)
    choose = cluster_colourization(k)
    for i in range(len(centers)):
        colour_centres_dict[f'centre{i}'] = centers[i], choose[i]
    operation(filepath, iter_count, centers, colour_centres_dict, colour_points_dict)
    visualization(data, colour_points_dict, centers, filepath, k, iter_count)

def main():
    while True:
        try:
            k_value = int(input('Please enter the number of centres: '))
            break
        except:
            print('Please write a number; try again.', end=' ')
    while True:
        try:
            number_of_iteration = int(input('Please enter the number of iterations: '))
            break
        except:
            print('Please write a number; try again.', end=' ')
    # k_value = random.randint(1, 10)
    k_means("xclara.csv", k_value, number_of_iteration)
    # k_means("500_Person_Height_Weight.csv", k_value, number_of_iteration)

main()

# You can change the number of clusters (k) to use, or the number of iterations.
# If you wish, you can find your own dataset (or maybe create your own dataset using the random module),
# and after handling the input part use this algorithm.
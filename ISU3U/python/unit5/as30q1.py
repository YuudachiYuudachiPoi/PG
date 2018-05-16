def count_total(numbers):

    total_down_1 = numbers[1] * numbers[2]
    total_down_2 = numbers[0] / numbers[4] + numbers[8]
    total_down_3 = numbers[2] - numbers[7]

    total_across_1 = numbers[1] / numbers[2]
    total_across_2 = numbers[3] * numbers[4] - numbers[5]
    total_across_3 = numbers[6] + numbers[7]

    total = total_down_1 + total_down_2 + total_down_3 + total_across_1 + total_across_2 + total_across_3
    
    all_total =[total,
        total_down_1,total_down_2,total_down_3,
        total_across_1,total_across_2,total_across_3]

    return total,all_total


def next_list(number,last_possible_number):
    next_possible_number = []
    for k in last_possible_number:
        if k != number:
            next_possible_number.append(k)

    return next_possible_number


possible_number_0 = []
for n in range(1,10):
    possible_number_0.append(n)

total_list = []
everythings_list = []

for n0 in possible_number_0:
    possible_number_1 = next_list(n0,possible_number_0)

    for n1 in possible_number_1:
        possible_number_2 = next_list(n1,possible_number_1)

        for n2 in possible_number_2:
            possible_number_3 = next_list(n2,possible_number_2)

            for n3 in possible_number_3:
                possible_number_4 = next_list(n3,possible_number_3)

                for n4 in possible_number_4:
                    possible_number_5 = next_list(n4,possible_number_4)

                    for n5 in possible_number_5:
                        possible_number_6 = next_list(n5,possible_number_5)

                        for n6 in possible_number_6:
                            possible_number_7 = next_list(n6,possible_number_6)

                            for n7 in possible_number_7:
                                possible_number_8 = next_list(n7,possible_number_7)

                                n8 = possible_number_8[0]

                                numbers = [n0,n1,n2,n3,n4,n5,n6,n7,n8]

                                total,all_total = count_total(numbers)
                                total_list.append(total)
                                all_total.append(numbers)
                                everythings_list.append(all_total)

biggest_total = max(total_list)
print(biggest_total)

for n in everythings_list:
    if n[0] == biggest_total:
        print(n)

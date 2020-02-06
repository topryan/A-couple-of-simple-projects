def main():
    y_or_n = input('Do you want to continue?(y or n)')
    while y_or_n == 'y':
        print('Please enter the following information(without unit) with the blank split.')
        input_str = input('gender weight(kg) height(cm) age:')
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = float(str_list[3])

        if gender == 'male':
            bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
        elif gender == 'female':
            bmr = 9.6 * weight + 4.8 * height - 1.7 * age + 655
        else:
            bmr = -1

        if bmr != -1:
            print('Your gender:{}, weight:{}kg, height:{}cm. age:{}'.format(gender, weight, height,age))
            print('Your basal metabolic rate:{} calories'.format(bmr))
        else:
            print('This gender is not supported yet.')
        print()
        y_or_n = input('Do you want to continue?(y or n)')

if __name__ == '__main__':
    main()
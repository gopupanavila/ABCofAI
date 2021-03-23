import csv
import random

items = {
    'office': ['SECURITY LOCK', 'CAMERA', 'COMPUTER', 'COFFEE MACHINE', 'WAITING LOUNGE'],
    'home': ['KITCHEN SET', 'TELIVISION', 'SHOW CASE', 'DRESSING TABLE', 'DOUBLE COT']
}
applicance_type = ['home', 'office']


def gen(name, volume=10000):
    with open(name, mode='w') as test_file:
        test_data_writer = csv.writer(test_file, delimiter=',',
                                      quotechar='"', quoting=csv.QUOTE_MINIMAL)

        test_data_writer.writerow(['index', 'user', 'appliance_type', 'items', 'rating'])
        for i in range(volume):
            appl_type = random.choice(applicance_type)
            count = random.randint(1, 4)
            _items = ','.join(random.sample(items.get(appl_type), count))
            rating = random.randint(1, 10)
            user = f'user{random.randint(1,500)}'
            test_data_writer.writerow([str(i+1), user, appl_type, str(_items), str(rating)])


if __name__ == '__main__':
    gen('appliances_rating.csv')





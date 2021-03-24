import csv
import random

items = {
    'office': ['SECURITY LOCK', 'CAMERA', 'COMPUTER', 'COFFEE MACHINE', 'WAITING LOUNGE',
               'SHREDDER', 'LAZER PRINTER', 'PAPER CLIP', 'MARKER', 'CALCULATOR'],
    'home': ['KITCHEN SET', 'TELEVISION', 'SHOW CASE', 'DRESSING TABLE',
             'DOUBLE COT', 'DISH WASHER', 'OVEN', 'TOASTER', 'REFRIGERATOR',
             'WASHING MACHINE', 'BLENDER', 'VACCUM CLEANER']
}
applicance_type = ['home', 'office']


def gen(name, volume=20000):
    with open(name, mode='w') as test_file:
        test_data_writer = csv.writer(test_file, delimiter=',',
                                      quotechar='"', quoting=csv.QUOTE_MINIMAL)

        test_data_writer.writerow(['no', 'user', 'appliance_type', 'items', 'quantities', 'rating'])
        for i in range(volume):
            appl_type = random.choice(applicance_type)
            count = random.randint(1, 4)
            _items = ','.join(random.sample(items.get(appl_type), count))
            quantities = ','.join([str(random.randint(1, 4)) for i in range(count)])
            rating = random.randint(1, 10)
            user = f'user{random.randint(1,500)}'
            test_data_writer.writerow([str(i+1), user, appl_type,
                                       str(_items), str(quantities), str(rating)])


if __name__ == '__main__':
    gen('appliances_rating.csv')





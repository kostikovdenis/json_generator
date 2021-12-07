import random
import uuid
from random import randint
from json import dumps
from datetime_generator import RandomDateTime as rdt

length = 20
filename = 'test_2'
start_datetime = '1900:01:01'
end_datetime = '2021:01:01'
pattern_datetime = '%Y:%m:%d'

for i in range(length):
    data_dict = {
        'userId': randint(1, 10000),
        'user': {
            'firstName': str(uuid.uuid4())[:-29],
            'lastName': str(uuid.uuid4())[:-20],
            'sex': random.choice(['M', 'F']),
            'birthDate': rdt(start_datetime, end_datetime, pattern_datetime).random_dt(),
            'driverLicense': bool(random.getrandbits(1))
        },
        'message': {
            'messageId': random.randrange(10000),
            'text': str(uuid.uuid4()),
        }
    }

    with open('%s.json' % filename, 'a') as output:
        output.write(dumps(data_dict, indent=None, separators=(',', ':')))
        output.write('\n')

print("Done.")

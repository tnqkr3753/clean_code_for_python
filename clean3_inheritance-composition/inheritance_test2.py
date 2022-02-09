import collections
from datetime import datetime

class TransactionalPolicy(collections.UserDict):
    '''잘못된 상속'''

    def change_in_policy(self, customer_id, **new_policy_data):
        self[customer_id].update(**new_policy_data)

def main():
    policy = TransactionalPolicy({
        "client1":{
            "fee": 1000.0,
            "expiration_date": datetime(2022,2,9),
        }
    })
    print(policy['client1'])
    policy.change_in_policy("client1",expiration_date=datetime(2022,2,15))
    print(policy['client1'])
    print()
    print(dir(policy))

if __name__=='__main__':
    main()
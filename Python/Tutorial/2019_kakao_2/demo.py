import requests
from elevator import Elevator


class Demo:
    server_addr = "http://localhost:8000"

    def __init__(self):
        self.user_key = 'user'
        self.problem_id = 0
        self.number_of_elevators = 1
        self.token = None
        self.elevators = []

    def start(self):
        url = '{}/start/{}/{}/{}'.format(self.server_addr, self.user_key, self.problem_id, self.number_of_elevators)
        r = requests.post(url=url)
        data = r.json()
        self.token = data['token']
        elevators = data['elevators']
        for e in elevators:
            elevator = Elevator(elevator_id=e['id'], floor=e['floor'], passengers=e['passengers'], status=e['status'])
            self.elevators.append(elevator)
        # print(self.token)
        # print(self.elevators)

    def on_call(self):
        headers = {'X-Auth-Token': self.token}
        url = '{}/oncalls'.format(self.server_addr)
        r = requests.get(url=url, headers=headers)
        data = r.json()
        print(data)
        print(data['calls'])

    def action(self, commands):
        headers = {'X-Auth-Token': self.token, 'Content-Type': 'application/json'}
        url = '{}/action'.format(self.server_addr)
        r = requests.post(url=url, headers=headers, json={'commands': commands})
        data = r.json()
        print(data)


if __name__ == '__main__':
    demo = Demo()
    demo.start()
    demo.on_call()
    print(demo.elevators)

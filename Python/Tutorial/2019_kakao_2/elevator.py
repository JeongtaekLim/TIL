class Elevator:
    state_to_action = {
        'STOPPED': {
            'STOP': 'STOPPED',
            'OPEN': 'OPENED',
            'UP': 'UPWARD',
            'DOWN': 'DOWNWARD'
        },
        'OPENED': {
            'OPEN': 'OPENED',
            'ENTER': 'OPENED',
            'EXIT': 'OPENED',
            'CLOSE': 'STOPPED'
        },
        'UPWARD': {
            'STOP': 'STOPPED',
            'UP': 'UPWARD',
        },
        'DOWNWARD': {
            'STOP': 'STOPPED',
            'DOWN': 'DOWNWARD'
        }
    }

    def __init__(self, elevator_id, floor, passengers, status):
        self.elevator_id = elevator_id
        self.floor = floor
        self.passengers = passengers
        self.status = status
        self.max = 8

    def __repr__(self):
        return "<{}, {}, {}, {}>".format(self.elevator_id, self.floor, self.passengers, self.status)

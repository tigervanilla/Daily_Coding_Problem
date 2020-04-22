# This problem was asked by Twitter.

# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

# You should be as efficient with time and space as possible.


class Log:
    def __init__(self, max_log_size):
        self.max_log_size = max_log_size
        self.buffer = [None] * max_log_size
        self.cur_index = 0

    def record(self, order_id):
        self.buffer[self.cur_index] = order_id
        self.cur_index = (self.cur_index + 1) % self.max_log_size

    def get_last(self, i):
        index = (self.cur_index + self.max_log_size - i) % self.max_log_size
        return self.buffer[index]


n = 5
logs = Log(n)
for i in range(8):
    logs.record('log #' + str(i + 1))
for i in range(1, n + 1):
    print(logs.get_last(i))

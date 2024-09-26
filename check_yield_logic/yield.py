

# def _yield_def():
#     i = 1
#     yield i
#     while True:
#         print ("Print #1:", i)
#         if i == 1:
#             print("keep work 1:", i)
#             i += 2
#
#
#         print("keep work 2:", i)
#         i += 1
#
# # def _retun_def():
# #     i = 1
# #     print ("Print #2:", i)
# #     return i + 1
#
#
# for index in _yield_def():
#     if index > 10:
#         break
#     print ("Result _yield_def:", index)
#     # print ("Result _retun_def:", _retun_def())

safer_output = {
    0: "qw1",
    1: "qw2",
    2: "qw3",
    3: "qw4",
    4: "qw5",
    5: "qw6",
    6: "qw7",
    7: "qw8",
    8: "qw9",
    9: "qw10",
    10: "qw11",
    11: "qw12",
    12: "qw13",
    13: "qw14",
    14: "qw15",
    15: "qw16",
    16: "qw17",
    17: "qw18",
    18: "qw19",
    19: "qw20",
    20: "qw21",
}
rows_size = 0
num_rows = 2

class yieldTest():

    def _get_batch_row(self, first_block):
        batch_row_idx = 1
        while batch_row_idx < num_rows:
            filename = 'filename.xml'
            batch_rows = [safer_output[0]]
            rows_size = 0
            batch_row_idx += 1
            print('first_block:', first_block)
            for index in range(1, 20):
                row = safer_output[index]
                batch_rows.append(row)
                rows_size += len(row) + 1

                if first_block:
                    print('first_block:index = ', first_block, index)

                if rows_size >= 11:
                    yield batch_rows, filename

                    batch_rows = [safer_output[0]]
                    rows_size = 0

            if len(batch_rows) > 1:
                yield batch_rows, filename

            first_block = False


    def _exec_some_code(self):
        first_block = True
        # while True:
        for batch_rows, filename in self._get_batch_row(first_block):
            print('_get_batch_row', batch_rows, filename, first_block)
            yield batch_rows, filename
            first_block = False


    # print(_exec_some_code())

yield_test = yieldTest()

for batch_rows, filename in yield_test._exec_some_code():
    print('_exec_some_code', batch_rows, filename)
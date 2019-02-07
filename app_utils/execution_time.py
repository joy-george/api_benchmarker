import time


def calculate(func):
    def timeit():
        execution_start_time = time.time()
        response = func()
        # x 1000 to convert the output into milliseconds
        response["executionTimeMs"] = "{:.4f}".format((time.time()-execution_start_time)*1000)
        return response

    return timeit
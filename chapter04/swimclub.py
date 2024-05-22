import statistics

FOLDER = "../chapter03/swimdata/"


def read_swim_data(filename):
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(",")

    converts = []
    for time in times:
        if ":" in time:
            minutes, rest = time.split(":")
            seconds, hundreths = rest.split(".")
        else:
            minutes = 0
            seconds, hundreths = time.split(".")

        converts.append(
            (int(minutes) * 60 * 100) + (int(seconds) * 100) + (int(hundreths))
        )

    average = statistics.mean(converts)
    mins_secs, hundreths = str(round(average / 100, 2)).split(".")
    mins_secs = int(mins_secs)
    minutes = mins_secs // 60
    seconds = mins_secs - minutes * 60
    average = str(minutes) + ":" + str(seconds) + ":" + hundreths

    return swimmer, age, distance, stroke, times, average

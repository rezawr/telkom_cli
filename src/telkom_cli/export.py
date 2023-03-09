import json


def read_files(err_file):
    with open(err_file) as f:
        f = f.readlines()

    return f

def export_json(file, err_file):
    if file is None:
        file = open('error.json', 'w')

    f = read_files(err_file)

    res = []
    for line in f:
        arr = line.split(": ")

        if len(arr) < 3:
            time = arr[0]
            user = None
            msg = arr[1]
        else:
            time = arr[0]
            user = arr[1]
            msg = arr[2]

        res.append({
            "time": time,
            "agent": user,
            "err_log" : msg,
        })

    json.dump(res, file, indent=4)
    file.close()


def export_plain(file, err_file):
    if file is None:
        file = open('error.txt', 'w+')

    f = read_files(err_file)

    for line in f:
        file.write(line)

    file.close()

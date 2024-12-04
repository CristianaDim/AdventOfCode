import numpy as np

def safe(report):
    differences = np.diff(report)
    if np.max(np.abs(differences)) > 3 or np.min(np.abs(differences)) < 1:
        return 0

    if int(np.abs(np.sum(np.sign(differences)))) != len(differences):
        return 0

    return 1

reports = []
with open('input.csv', 'r+') as f:
    for line in f.readlines():
        strippedLine = line.rstrip()
        report = []
        for val in strippedLine.split(' '):
            report.append(float(val))
        reports.append(report)

safeCount = 0
for report in reports:
    if safe(report):
        safeCount += 1
    else:
        good = False
        for i in range(len(report)):
            if safe(report[:i] + report[i+1:]):
                good = True
        if good:
            safeCount += 1

print(f"{int(safeCount)} reports are safe.")
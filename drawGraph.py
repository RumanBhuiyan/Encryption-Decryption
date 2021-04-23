import numpy as np
import matplotlib.pyplot as plt


def plotGraph(data,title):
    courses = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(courses, values, color='orange', width=0.4)
    plt.xlabel("Key lengths in bits")
    plt.ylabel("execution time in seconds")
    plt.title(title)
    plt.show()

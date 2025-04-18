"""
This is a script to help fatma with graph for thesis. It creates a antimated graph of fatma's data
requirements: scipy, pandas, matplotlib

author: Abdul
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scienceplots
import matplotlib as mpl
import pandas as pd
from scipy.signal import savgol_filter

# yhat = savgol_filter(y, 51, 3) # window size 51, polynomial order 3


fig_object = []

axes = []
Peak_list = [14]
Peak_label = ["peak1"]
font_size = 20

window_size = 70
smoothing_factor = 4


def draw_line(x, y, label):
    line = plt.plot([x, x], [y, 0], '--')
    plt.text(x, y + 5, label)


def create_fig(fig_data: np.ndarray):
    """
    This creates the static figure needed for animation
    :return: fig,ax
    """
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((size := len(data[1]) / 2, 0), 300, 400, ls="--", ec="c",color="lightgrey"))
    line = plt.plot(np.arange(len(data[1])), data[1])  # raw data
    line2 = plt.plot(np.arange(len(data[1])), savgol_filter(data[1], window_size, smoothing_factor), "--")  # smooth

    plt.xlabel("X-axis")  # X-axis here
    plt.ylabel("Y-axis")  # Y-axis here
    plt.title("Fatma_graph")  # title here
    plt.xlim([0, size])  # x-limits
    plt.ylim([-3, 400])  # y-limits

    x_index = [100, 200, 300, 400]
    label = [data[0][100], data[0][200], data[0][300], data[0][400]]
    for j, i in enumerate(Peak_list):
        i = i - 2
        x_index.append(i)
        label.append(data[0][i])
        draw_line(i, data[1][i], Peak_label[j])

    plt.xticks(x_index, label)
    fig_object.append(*line)
    return fig, ax


def main(data):
    # Use a breakpoint in the code line below to debug your script.
    # plt.style.use("science")
    # print(mpl.rcParams.keys())
    mpl.rcParams["font.size"] = font_size

    fig, ax = create_fig(data)
    # ani = animation.FuncAnimation(fig=fig, func=update, frames=100, interval=30)
    # ani.save("ani.gif")
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fatma_data = pd.read_csv("fatma_data.csv")
    x = fatma_data["Day"].tolist()
    y = fatma_data["Total"].tolist()
    # m = 3
    # data = 3 * np.arange(100) + np.random.normal(0, 2, 100)  # creating random data
    data = [x, y]
    main(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import matplotlib.pyplot as plt
import pandas as pd

CSV = "https://raw.githubusercontent.com/gzavo/CS_Assignment/master/istherecorrelation.csv"


def main():
    """
    Reads in a csv file and
    makes two subplots (line) of the data.
    """

    df = pd.read_csv(CSV, sep=';', decimal=',')
    cols = list(df.columns)
    df[cols[1]] = pd.to_numeric(df[cols[1]])

    for i in range(1, 3):
        df[cols[i]] = df[cols[i]] * 1000

    lineplot(df, cols)

def lineplot(df, cols):
    """
    Makes two subplots (line) of the data.
    """

    # Create two subplots
    plt.style.use("seaborn-darkgrid")
    fig, axes = plt.subplots(1, 2, figsize=(10, 5), tight_layout=True)
    axes[0].plot(df[cols[0]], df[cols[1]], marker='.', mfc='k')
    axes[1].plot(df[cols[0]], df[cols[2]], marker='.', mfc='k')
    axes[0].set_title("Amount of Dutch WO Students Per Year",
                      fontsize=14, fontweight="bold", pad=20)
    axes[1].set_title("Total Beer Consumption of Dutch Students \n in hectoliters",
                      fontsize=14, fontweight="bold", pad=20)
    axes[0].set_ylabel("Students", fontsize=12, fontweight='bold')
    axes[1].set_ylabel("Beer Consumption (hL)", fontsize=12, fontweight='bold')

    for index in range(2):
        axes[index].set_xticks(df[cols[0]])
        axes[index].ticklabel_format(style='sci', axis='y', scilimits=(3, 3))
        axes[index].set_xlabel("Year", fontsize=12, fontweight='bold')

    for ax in axes:
        for tick in ax.get_xticklabels():
            tick.set_rotation(-60)

    plt.savefig("correlation.png", dpi=300)

if __name__ == "__main__":
    main()

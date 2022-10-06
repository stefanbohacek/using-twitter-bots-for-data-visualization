import matplotlib.pyplot as plt
import seaborn as sns

def handler(pd: "pipedream"):
    dataset = pd.steps["get_data"]["$return_value"]
    data = dataset["data"]
    filename = "/tmp/chart.png"

    sns.set_style("darkgrid")
    sns.barplot(x = list(data.values()), y = [f"{x}: {list(data.values())[ind]}" for ind, x in enumerate(list(data.keys()))], orient = "h")
    plt.tight_layout()
    plt.savefig(filename)

    return {
        "filename": filename,
        "dataset": dataset
    }


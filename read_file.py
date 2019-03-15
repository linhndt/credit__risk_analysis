import pandas as pd




def read_csv_file(dataset_name):

    assert dataset_name in [
        "hmeq",         # Home loan
        "lgd",          # Loss rate given default
        "mortgage",     # Mortgage
        "rating"        # Credit ranking
    ]

    if dataset_name == 'hmeq':
        dataset = pd.read_csv('data/hmeq.csv')

    elif dataset_name == 'lgd':
        dataset = pd.read_csv('data/lgd.csv')

    elif dataset_name == 'mortgage':
        dataset = pd.read_csv('data/mortgage.csv')

    else:
        dataset = pd.read_csv('data/ratings.csv')

    return dataset



if __name__ == "__main__":

    dataset_name = 'mortgage'
    data = read_csv_file(dataset_name)
    print(data)

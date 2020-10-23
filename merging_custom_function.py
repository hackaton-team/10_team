import json
import pandas as pd


def merging_custom(json_paths: list,
                   csv_paths: list,
                   output_path: str,
                   additional_keys=None,
                   columns_to_include=None):
    """
    Merges twits from json files and prices from csv files into one common csv file.
    :param json_paths: paths to json files with twits
    :param csv_paths: paths to csv files with prices
    :param output_path: path to output csv file
    :param additional_keys: (optional) additional keys from json to be included in output file
    :param columns_to_include: (optional) selection of columns from csv to be included in output file
    :return: csv file
    """
    people = []
    assets = []
    for i in json_paths:
        with open(i) as f:
            person = json.load(f)
        person_lst = []
        for j in person:

            person_lst.append([person[j]['created_at'],
                               person[j]['user']['name'],
                               person[j]['text']])

            if additional_keys != None:
                for k in additional_keys:
                    person_lst[-1].append(person[j].get(k, None))

        cols = ['Date', 'Name', 'Tweets']
        if additional_keys != None:
            for k in additional_keys:
                cols.append(k)

        person = pd.DataFrame(person_lst, columns=cols)

        person['Date'] = pd.to_datetime(person['Date'])
        person['Date'] = person['Date'].dt.strftime('%Y-%m-%d')
        person['Date'] = pd.to_datetime(person['Date'])
        people.append(person)

    for p in csv_paths:
        asset = pd.read_csv(p)
        if columns_to_include != None:
            if 'Date' not in columns_to_include:
                columns_to_include.append('Date')
            asset = asset[[x for x in columns_to_include if x in asset.columns]]
        asset['Date'] = pd.to_datetime(asset['Date'])
        assets.append(asset)

    a = people[0]
    b = assets[0]
    for i in range(1, len(people)):
        a = a.append(people[i])
    for i in range(1, len(assets)):
        b = b.merge(assets[i], how='outer')

    start_date = max(min(a['Date']), min(b['Date']))
    tweet_dates = a[a['Date'] >= start_date]['Date']
    asset_dates = b[(b['Date'] >= min(tweet_dates)) & (b['Date'] <= max(tweet_dates))]['Date']
    missing_dates = pd.concat([asset_dates, tweet_dates]).drop_duplicates(keep=False)
    missing_assets = b[b['Date'].isin(missing_dates)]

    for clm in a.columns[1:]:
        missing_assets[clm] = None

    total = a.merge(b)

    if max(a['Date']) != max(total['Date']):
        add_clm = []
        for _ in a.iloc[0, :]:
            add_clm.append(_)
        for _ in range(len(total.columns) - len(a.columns)):
            add_clm.append(None)
        add_clm = pd.DataFrame([add_clm])
        add_clm.columns = total.columns
        total = total.append(add_clm)

    total = total.append(missing_assets)
    total.sort_values('Date', ascending=False, inplace=True)
    total.to_csv(output_path, index=False)
    return total.reset_index(drop=True)
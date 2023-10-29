import pandas as pd


def create_html(apartments):
    df = pd.DataFrame(data=apartments)
    df = df.fillna(' ')
    html = df.to_html(escape=False)
    return html

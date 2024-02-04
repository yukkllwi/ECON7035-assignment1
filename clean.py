import pandas as pd


def clean(input1,input2):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df_merged = pd.merge(df1,df2,left_on='respondent_id',right_on='id').drop('respondent_id', axis=1).dropna()
    df_merged = df_merged[~df_merged['job'].str.contains('insurance|Insurance')]
    return df_merged


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file (CSV)')
    parser.add_argument('input2', help='Data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)

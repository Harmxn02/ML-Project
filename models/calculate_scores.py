def calculate_scores(df):
    pos_columns = [col for col in df.columns if "pos" in col]
    neg_columns = [col for col in df.columns if "neg" in col]

    # Calculating net score
    for i in range(1, 6):
        hotel_pos_cols = [f"score{i}_pos"]
        hotel_neg_cols = [f"score{i}_neg"]

        df[f"net_score{i}"] = df[hotel_pos_cols].values - df[hotel_neg_cols].values
    
    # combined_net_score = df[pos_columns].sum(axis=1) - df[neg_columns].sum(axis=1)

    # Adding new columns to the DataFrame
    df["combined_pos_score"] = df[pos_columns].sum(axis=1)
    df["combined_neg_score"] = df[neg_columns].sum(axis=1)
    # df["combined_net_score"] = combined_net_score

    # Dropping original score columns and net score columns
    df.drop(columns=pos_columns + neg_columns + [f'net_score{i}' for i in range(1, 6)], inplace=True)

    return df
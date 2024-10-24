def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).

    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.

    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],
            'discrete': []
        },
        'categorical': {
            'nominal': [],
            'ordinal': []
        }
    }

    # Classify numerical features
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if df[col].nunique() < 20:  # Assuming discrete if unique values are less than 20
            feature_types['numerical']['discrete'].append(col)
        else:
            feature_types['numerical']['continuous'].append(col)

    # Classify categorical features
    for col in df.select_dtypes(include=['object']).columns:
        feature_types['categorical']['nominal'].append(col)

    # You may manually add any known ordinal features
    # feature_types['categorical']['ordinal'].append('known_ordinal_feature')

    return feature_types


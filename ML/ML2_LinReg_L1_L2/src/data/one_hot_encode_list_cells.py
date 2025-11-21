def maxu(df):
    mlb = MultiLabelBinarizer()
    d = pd.DataFrame(
        mlb.fit_transform(df.Col3.values)
        , df.index, mlb.classes_
    )
    return df.drop('Col3', 1).join(d)


def bos(df):
    return df.drop('Col3', 1).assign(**pd.get_dummies(df.Col3.apply(lambda x:pd.Series(x)).stack().reset_index(level=1,drop=True)).sum(level=0))

def psi(df):
    return pd.concat([
        df.drop("Col3", 1),
        df.Col3.apply(lambda x: pd.Series(1, x)).fillna(0)
    ], axis=1)

def alex(df):
    return df[['Col1', 'Col2']].assign(**{fruit: [1 if fruit in cell else 0 for cell in df.Col3] 
                                       for fruit in set(fruit for fruits in df.Col3 
                                                        for fruit in fruits)})

def pir_slow(df):
    return df.drop('Col3', 1).join(df.Col3.str.join('|').str.get_dummies())

def pir_alt1(df):
    return df.drop('Col3', 1).join(pd.get_dummies(pd.DataFrame(df.Col3.tolist()).stack()).astype(int).sum(level=0))

def pir_fast(df):
    v = df.Col3.values
    l = [len(x) for x in v.tolist()]
    f, u = pd.factorize(np.concatenate(v))
    n, m = len(v), u.size
    i = np.arange(n).repeat(l)

    dummies = pd.DataFrame(
        np.bincount(i * m + f, minlength=n * m).reshape(n, m),
        df.index, u
    )

    return df.drop('Col3', 1).join(dummies)

results = pd.DataFrame(
    index=(1, 3, 10, 30, 100, 300, 1000, 3000),
    columns='maxu bos psi alex pir_slow pir_fast pir_alt1'.split()
)

for i in results.index:
    d = pd.concat([df] * i, ignore_index=True)
    for j in results.columns:
        stmt = '{}(d)'.format(j)
        setp = 'from __main__ import d, {}'.format(j)
        results.set_value(i, j, timeit(stmt, setp, number=10))

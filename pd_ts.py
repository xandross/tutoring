import pandas as pd


def getPeriodSalesData(sdf: pd.DataFrame, pandas_period: str, period_column_name: str):
    prev_period_column_name = 'prev_' + period_column_name

    sdf[period_column_name] = sdf['date'].dt.to_period(pandas_period)
    sdf[prev_period_column_name] = sdf[period_column_name] - 1

    grouped = sdf.groupby(period_column_name)['sales'].max().reset_index()
    grouped = grouped.rename(
        columns={
            period_column_name: prev_period_column_name,
            'sales': prev_period_column_name + 'ly_sales_max'
        })

    sdf = sdf.merge(grouped, how='left', on=prev_period_column_name)

    return sdf

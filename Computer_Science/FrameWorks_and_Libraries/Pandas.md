# Pandas

## Iterate over rows

```python
for index, row in df.iterrows():
    print(row['c1'], row['c2'])
```

## Multi Index

Multi index is use for dealing with data that has mutiple colums/rows. See 'pandasMultiIndexSample' for an example of what this data might look like.

Good reference link:
<br>https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

### Get level colums

The normal .columns will give you a tuple of all the levels combinded. To get colums for at specific level first get levels by `mi.names` then get the columns in a level with get_level_values `mi.get_level_values('level_name')`. Or integers can be used `mi.get_level_values(0)` where it the int is the level with 0 being the highest.<br>
Ref link: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.get_level_values.html

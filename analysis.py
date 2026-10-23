import pandas as pd
from scipy import stats

def analyse_release_years(data):
    d = data[["type", "release_year"]].copy()
    d["release_year"] = pd.to_numeric(d["release_year"], errors="coerce")
    d = d[d["type"].isin(["Movie", "TV Show"]) &
          d["release_year"].between(1900, 2100)].dropna()
    movies = d.loc[d["type"] == "Movie", "release_year"].to_numpy()
    tv = d.loc[d["type"] == "TV Show", "release_year"].to_numpy()
    if len(movies) == 0 or len(tv) == 0:
        raise ValueError("Both groups must contain valid records")
    return stats.mannwhitneyu(movies, tv, alternative="greater")

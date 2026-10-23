import pandas as pd
from scipy import stats

def analyse_release_years(data):
    required = {"type", "release_year"}
    if not required.issubset(data.columns):
        raise ValueError("Required columns are missing")

    d = data[["type", "release_year"]].copy()
    d["release_year"] = pd.to_numeric(d["release_year"], errors="coerce")
    d = d[
        d["type"].isin(["Movie", "TV Show"])
        & d["release_year"].between(1900, 2100)
    ].dropna(subset=["release_year"])

    movies = d.loc[d["type"] == "Movie", "release_year"].to_numpy()
    tv = d.loc[d["type"] == "TV Show", "release_year"].to_numpy()

    if len(movies) == 0 or len(tv) == 0:
        raise ValueError("Both groups must contain valid records")

    result = stats.mannwhitneyu(movies, tv, alternative="greater")
    return len(d), len(movies), len(tv), result.pvalue

def test_synthetic_pipeline():
    data = pd.DataFrame({
        "type": ["Movie", "Movie", "Movie", "TV Show", "TV Show", "TV Show"],
        "release_year": [2018, 2019, 2020, 2000, 2005, 2010]
    })
    total, movie_count, tv_count, p_value = analyse_release_years(data)
    assert total == 6
    assert movie_count == 3
    assert tv_count == 3
    assert 0 <= p_value <= 1

if __name__ == "__main__":
    test_synthetic_pipeline()
    print("PASS: Synthetic pipeline test")

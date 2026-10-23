# Netflix Movies and TV Shows — Reproducible Research Analysis

## Project Overview

This project analyses the release years of Movies and TV Shows in the Netflix dataset using Python and statistical methods. It follows a reproducible research workflow, including data cleaning, hypothesis testing, documentation, and synthetic-data pipeline testing.

## Research Question

**Do movies tend to have later release years than TV shows in the Netflix dataset?**

##  Technologies Used

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Google Colab

## Project Structure

```text
netflix-data-research/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/
├── src/
│   └── analysis.py
├── reports/
│   ├── preregistration.md
│   └── research_report.md
├── tests/
│   └── synthetic_pipeline_test.py
├── environment.txt
└── requirements-lock.txt
```

## 📊 Methodology

1. Load the Netflix dataset.
2. Select the `type` and `release_year` columns.
3. Remove invalid title types and invalid release years.
4. Compare Movies and TV Shows using median release years.
5. Apply a one-sided Mann–Whitney U test.
6. Perform a robustness check using the 1st and 99th percentiles.
7. Document the findings and test the pipeline using synthetic data.

## Results

The analysis of the supplied dataset produced the following results:

- Valid records: 8,807
- Movies: 6,131
- TV Shows: 2,676
- Median release year for Movies: 2016
- Median release year for TV Shows: 2018
- Mann–Whitney U test p-value: 1.0

The test did not provide sufficient statistical evidence that movie release years tend to be later than TV Show release years.

## Reproducibility

The project includes an analysis plan, research report, Python analysis code, environment information, package lockfile, and synthetic-data pipeline test.

## Limitations

- The Netflix catalogue may not represent all movies and TV shows.
- Release year is different from the date a title was added to Netflix.
- The analysis is observational and cannot establish causation.

## How to Run

1. Download or clone this repository.
2. Install the packages listed in `requirements-lock.txt` in a compatible Python environment.
3. Open the analysis notebook in Google Colab or Jupyter.
4. Provide the Netflix dataset in the expected location.
5. Run the notebook cells in order.

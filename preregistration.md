# Analysis Plan: Netflix Release Year Comparison

## Research Question
Do movies tend to have later release years than TV shows?

## Population
Valid Movie and TV Show records in the supplied Netflix dataset.

## Exposure and Comparator
Group of interest: Movie.
Comparator: TV Show.
This is an observational comparison.

## Outcome
Release year, measured in calendar years.

## Observation Window
All valid release years available in the supplied dataset.

## Hypotheses
H0: Movie release years do not tend to be greater than TV Show release years.
H1: Movie release years tend to be greater than TV Show release years.

## Exclusion Rules
Exclude invalid title types, missing or non-numeric years,
and release years outside 1900–2100.

## Transformations
Select type and release_year, convert release_year to numeric,
apply exclusions, and convert valid years to integers.

## Statistical Test
Use a one-sided Mann–Whitney U test with Movie as the first group.
Significance level: 0.05.
Report group sizes, medians, median difference, p-value, and effect size.

## Robustness Check
Repeat the test after removing years below the pooled 1st percentile
or above the pooled 99th percentile.

## Limitations
The catalogue may not represent all entertainment titles.
Release year is not the date a title was added to Netflix.
This observational analysis cannot establish causation.

## Registration Status
This document records the analysis plan transparently.
If the data or results have already been examined, this is not a
prospective preregistration made before seeing the data.
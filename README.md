# Data-Analysis

A collection of pandas practice exercises — five Jupyter notebooks, two standalone scripts and three
exported PDFs — working through weather, cars, police-stop, COVID-19, London housing and Udemy
course datasets.

This is coursework, not a library or an application. Each file answers a numbered list of questions
about one dataset; there is no shared code, no package structure and nothing to install or run as a
whole.

## Contents

### Notebooks

| File | Dataset | Contents |
| --- | --- | --- |
| `Weather data.ipynb` | Weather Data Analysis | ~138 lines: unique wind speeds, value counts, null handling, renaming columns, `.mean()`, filtering by weather condition |
| `Cars Data.ipynb` | Cars Data Analysis | ~40 lines: shape, nulls, value counts, grouping by make |
| `Police Data.ipynb` | Police Data Analysis | ~63 lines: dropping sparse columns, stop-outcome rates by gender, search-conducted rates, `datetime` conversion |
| `Covid Data Analysis as of 29Apr2020 (1).ipynb` | COVID-19 (snapshot to 29 Apr 2020) | Confirmed/deaths/recovered by region, filtering, seaborn null heatmap |
| `Udemy Courses.ipynb` | Udemy course catalogue | The largest of the set (42 cells): paid vs free splits, top/bottom courses by subscriber count, cleaning a `price` column that mixes numbers with the string `"Free"`, keyword filters for Python/Java courses, `published_timestamp` → year, and matplotlib/seaborn charts of subscribers by subject, level distribution, price distribution and a price/subscribers/reviews correlation |

### Scripts

| File | Notes |
| --- | --- |
| `COVID Data.py` | The COVID notebook's analysis as a plain script, printing answers to Q1–Qn |
| `London Housing Data Analysis.py` | Null handling, `to_datetime` conversion, deriving a `year` column, grouping by area |
| `sum_of_array.py` | A four-line beginner exercise, unrelated to the rest |

### PDFs

`Census Data Analysis.pdf`, `Netflix.ipynb - JupyterLab.pdf` and `Udemy Course… (2) - JupyterLab.pdf`
are JupyterLab print-outs. **The Census and Netflix notebooks themselves are not in this repository** —
only these PDF exports survive.

## The datasets are not included — nothing here runs as-is

Every notebook and script loads its data from a **hardcoded absolute Windows path** on the original
author's machine, for example:

```python
covid = pd.read_csv(r"C:\Users\Harold\Desktop\python\projects\Dataset  Project 4  Covid Data Analysis.csv")
df    = pd.read_csv(r"D:\Documents\python\projects\Udemy.csv", index_col=0)
```

None of those CSVs are committed. To re-run anything you must source the dataset yourself and edit
the path at the top of the file. The saved cell outputs in the notebooks are the only record of the
results.

The `Dataset  Project N  …` filenames indicate these came from a structured pandas course.
**TODO: verify** which course, so the datasets can be linked and properly credited.

## Tech stack

Python 3, pandas, NumPy, matplotlib, seaborn, scikit-learn (in the Udemy notebook only), Jupyter.

```bash
python3 -m venv venv && source venv/bin/activate
pip install pandas numpy matplotlib seaborn scikit-learn jupyterlab
jupyter lab
```

There is no `requirements.txt`; the list above is inferred from the imports.

## A note on the notebook structure

Four of the five notebooks consist of a **single code cell** holding the entire analysis (up to 138
lines) rather than one cell per step, which makes them awkward to read and to re-execute
incrementally. `Udemy Courses.ipynb` is properly split into 42 cells and is the best example of the
set.

## Status

**Complete as a coursework archive; not maintained.** Last commit May 2024. Useful as evidence of
pandas familiarity; not reproducible without the source datasets.

## Licence

None. **TODO: add a LICENSE file** — without one, the default is "all rights reserved". Note that the
underlying datasets carry their own licence terms.

# 🎬 IMDb Movie Rating Analysis

> An exploratory data analysis (EDA) project investigating IMDb movie ratings —
> uncovering trends across genres, decades, and release years using Python.

---

## 📌 Project Overview

This project performs a full end-to-end analysis of IMDb movie data, from raw data
cleaning through to visual storytelling. It answers key questions like:

- Which genres consistently receive the highest ratings?
- How have movie ratings changed over time?
- What does the overall distribution of IMDb ratings look like?

Completed as part of the NSQ Level 3 — Data Analysis with Python certification
with the Computer Professionals Registration Council of Nigeria (CPN).

---

## 🔍 What the Analysis Covers

| Step | Description |
|---|---|
| Data Cleaning | Parsed messy columns — stripped symbols from gross_total, votes, year_of_release |
| Validation | Asserted ratings are within 1–10 and years within 1900–2023 |
| Feature Engineering | Created decade column and roi (Return on Investment) metric |
| Genre Expansion | Exploded multi-genre entries for accurate per-genre analysis |
| Visualisation | 5 charts covering distribution, genre comparison, and time trends |

---

## 📊 Visualisations Produced

### 1. 📈 Distribution of IMDb Ratings
Histogram showing how ratings are spread across all movies —
reveals whether most movies cluster around average or skew high/low.

### 2. 🎭 Top Genres by Average Rating
Horizontal bar chart comparing average IMDb rating per genre,
filtered to genres with at least 5 movies to avoid misleading small samples.

### 3. 📅 Ratings Over Time
Line plot of yearly average ratings with a polynomial trendline —
shows whether movie quality (as perceived by audiences) has shifted across decades.

### 4. 🫧 All Genres with Movie Count Bubbles
Enhanced genre chart with bubble indicators showing sample size per genre —
combines rating quality with data reliability at a glance.

### 5. 📊 Simple Genre Ranking
Clean horizontal bar chart for a quick genre-by-genre comparison.

---

## ⚙️ How to Run

### Requirementspip install pandas numpy matplotlib

### Steps
1. Place your movies.csv file in the same folder as the script
2. Run the script:python movie_rating_analysis.py

### Expected CSV columnsmovie_name, year_of_release, imdb_rating, gross_total, votes, genre

> Note: The script handles messy formatting automatically —
> year_of_release like (2019), gross_total like $45.3M,
> and votes like 1,234,567 are all cleaned on load.

---

## 📁 Project Structure
imdb-movie-rating-analysis/
│
├── movie_rating_analysis.py   # Full analysis and visualisation code
├── movies.csv                 # Dataset (add your own copy)
├── README.md                  # Project documentation

---

## 💡 Key Techniques Used

- `pd.read_csv` with custom converters — clean messy data on import without post-processing
- `.explode()` — handle multi-value genre lists properly
- `np.polyfit` — fit a trendline to time-series rating data
- Layered matplotlib charts — combine bars, scatter bubbles, and text annotations
- Data assertions — validate data integrity before analysis begins

---

## 📌 Sample Insight

> *"After filtering genres with fewer than 5 movies, the analysis reveals that
> certain niche genres consistently outperform mainstream categories in average
> IMDb rating — though their smaller sample sizes warrant cautious interpretation."*

---

## 👤 Author

Aliyu Abdullahi
B.Sc. Mathematics — Second Class Honours
Kaduna State University, Nigeria
📧 aleeyuabdullahi09@gmail.com

---

## 📜 Certifications
- NSQ Level 3 — Data Analysis with Python (CPN, Nov 2025)
- AI Workplace Proficiency Certification

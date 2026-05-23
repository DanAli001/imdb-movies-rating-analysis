import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(
    'movies.csv', 
    converters={
        'year_of_release': lambda x: int(x.strip('()')) if x and pd.notna(x) else np.nan,
        'gross_total': lambda x: float(x.strip('$').rstrip('M')) if x and pd.notna(x) else np.nan,
        'votes': lambda x: int(x.replace(',', '')) if x and pd.notna(x) else np.nan
    }
)

print(f"Data shape: {df.shape}")
print("\nSample cleaned data:")
print(df[['movie_name', 'year_of_release', 'imdb_rating', 'gross_total']].head(3))


assert df['imdb_rating'].between(1, 10).all()
assert df['year_of_release'].between(1900, 2023).all()

df['decade'] = (df['year_of_release'] // 10 * 10).astype(int)


genre_expanded = df.explode('genre')


df['roi'] = df['gross_total'] / df['gross_total'].median()


plt.figure(figsize=(10, 6))
plt.hist(df['imdb_rating'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of IMDb Ratings', fontsize=14)
plt.xlabel('Rating (1-10)')
plt.ylabel('Number of Movies')
plt.grid(axis='y', alpha=0.3)
plt.show()


genre_stats = (df.explode('genre')
                .groupby('genre')
                .agg({'imdb_rating': ['mean', 'count']})
                .droplevel(0, axis=1))
genre_stats = genre_stats[genre_stats['count'] > 5]  

plt.figure(figsize=(12, 6))
genre_stats['mean'].sort_values().plot(kind='barh', color='teal')
plt.title('Average IMDb Rating by Genre (Min 5 Movies)', fontsize=14)
plt.xlabel('Average Rating')
plt.xlim(7, 9)  
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
yearly_avg = df.groupby('year_of_release')['imdb_rating'].mean()


plt.plot(yearly_avg.index, yearly_avg.values, 
         'o-', color='navy', label='Yearly Average')


z = np.polyfit(yearly_avg.index, yearly_avg.values, 1)
p = np.poly1d(z)
plt.plot(yearly_avg.index, p(yearly_avg.index), 
         'r--', label='Trendline')

plt.title('IMDb Ratings Over Time', fontsize=14)
plt.xlabel('Release Year')
plt.ylabel('Average Rating')
plt.legend()
plt.grid(alpha=0.3)
plt.show()


genre_stats = (df.explode('genre')
               .groupby('genre')
               .agg(avg_rating=('imdb_rating', 'mean'),
                    movie_count=('imdb_rating', 'count'))
               .query('movie_count >= 5')  
               .sort_values('avg_rating', ascending=False))


plt.figure(figsize=(10, 6))
bars = plt.barh(genre_stats.index, genre_stats['avg_rating'], 
                color='#3498db', edgecolor='black', alpha=0.8)


plt.title('Top Genres by Average IMDb Rating (Min 5 Movies)', 
          fontsize=14, pad=20)
plt.xlabel('Average Rating', fontsize=12)
plt.xlim(7.5, 9.0) 
plt.grid(axis='x', linestyle='--', alpha=0.4)


for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.05, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}',
             va='center', ha='left', fontsize=10)


for i, (genre, row) in enumerate(genre_stats.iterrows()):
    plt.text(7.48, i, f'n={row["movie_count"]}', 
             va='center', ha='right', fontsize=9, color='gray')

plt.tight_layout


genre_stats = (df.explode('genre')
               .groupby('genre')
               .agg(avg_rating=('imdb_rating', 'mean'),
                    movie_count=('imdb_rating', 'count'))
               .sort_values('avg_rating', ascending=True))  


plt.figure(figsize=(12, 8))
bars = plt.barh(genre_stats.index, genre_stats['avg_rating'],
color='#1f77b4', edgecolor='black', alpha=0.7)


plt.title('All Genres by Average IMDb Rating\n(Bubble size = number of movies)',
          fontsize=14, pad=20, fontweight='bold')
plt.xlabel('Average Rating', fontsize=12)
plt.xlim(6, 9.5)  
plt.grid(axis='x', linestyle='--', alpha=0.3)


for i, (genre, row) in enumerate(genre_stats.iterrows()):
 
    plt.text(row['avg_rating'] + 0.05, i,
             f"{row['avg_rating']:.1f}",
             va='center', ha='left', fontsize=10)
    
    bubble_size = min(100 + row['movie_count'] * 5, 500)  
    plt.scatter([6.2], [i], s=bubble_size, color='#ff7f0e', alpha=0.5)
    plt.text(6.25, i, f"n={row['movie_count']}",
             va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()


(df.explode('genre')
   .groupby('genre')['imdb_rating']
   .mean()
   .sort_values()
   .plot(kind='barh', title='Average Rating by Genre'))
plt.show()

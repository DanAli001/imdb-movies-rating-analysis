color='#1f77b4', edgecolor='black', alpha=0.7)

# Customize appearance
plt.title('All Genres by Average IMDb Rating\n(Bubble size = number of movies)',
          fontsize=14, pad=20, fontweight='bold')
plt.xlabel('Average Rating', fontsize=12)
plt.xlim(6, 9.5)  # Adjusted range to include all genres
plt.grid(axis='x', linestyle='--', alpha=0.3)

# Add value labels and bubble indicators
for i, (genre, row) in enumerate(genre_stats.iterrows()):
    # Rating value
    plt.text(row['avg_rating'] + 0.05, i,
             f"{row['avg_rating']:.1f}",
             va='center', ha='left', fontsize=10)
    
    # Bubble indicator for movie count
    bubble_size = min(100 + row['movie_count'] * 5, 500)  # Scale bubble size
    plt.scatter([6.2], [i], s=bubble_size, color='#ff7f0e', alpha=0.5)
    plt.text(6.25, i, f"n={row['movie_count']}",
             va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()

# Top genres by average rating
(df.explode('genre')
   .groupby('genre')['imdb_rating']
   .mean()
   .sort_values()
   .plot(kind='barh', title='Average Rating by Genre'))
plt.show()

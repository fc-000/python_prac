liked_songs = {
  'Mr. Sun': 'Ichiko Aoba',
  'Potion For Love': 'AURORA'
}

def write_liked_songs_to_file(song, file_name):
  with open('liked_songs', 'w') as file:
    file.write('Liked songs:\n')
    for title, artist in song.items():
      file.write(f'{title} by {artist}\n')
  print(f"Successfully added liked songs to {file_name}")

write_liked_songs_to_file(liked_songs, "liked_songs.txt")
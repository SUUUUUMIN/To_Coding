def solution(genres, plays):
    album = []
    songs = {}
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        
        if genre in songs:
            songs[genre]['total'] += play
            songs[genre]['info'].append([i, play])
        
        else:
            songs[genre] = {
                'total' : play,
                'info' : [[i, play]]
            }
    songs = sorted(songs.items(), key=lambda item: item[1]['total'], reverse=True)
    
    for gen, song in songs:
        sort_info = sorted(song['info'], key=lambda x:x[1], reverse=True)
        album.extend(i[0] for i in sort_info[:2])
        

    return album
import random
import os


class MP3Playlist:
    def __init__(self, playlist):
        self.tracks = []
        self.playlist = playlist

    def load_playlist(self):
        playlist_path = f"C:/Users/USER/Documents/DataholicHQ/OOP/{self.playlist}.txt"
        if os.path.exists(playlist_path):
            with open(self.playlist + '.txt', 'r') as file:
                self.tracks = [line.strip() for line in file.readlines()]
        else:
            with open(playlist_path, 'w'):
                pass
            print(f"Playlist does not exist but we have created a new one with the "
                  f"name '{self.playlist}' for you.")
            # user_choice = input(f"The playlist '{self.playlist}' does not exist."
            #              "\nWould you like to create it and add a track to it? (y/n): ")
            #
            # while user_choice != 'y' or user_choice != 'n':
            #     user_choice = input(f"You entered the wrong choice. Enter (y/n): ")
            #
            # if user_choice == 'y':
            #     self.playlist = input("What playlist name do you want: ")
            #     track_name = input(f'What track do you want to add to the playlist {self.playlist}: ')
            #     self.add_track(track_name)
            #     print(f"The track '{track_name}' has been added to the playlist {self.playlist}")

    def display_tracks(self):
        if len(self.tracks) == 0:
            print(f"The playlist {self.playlist} is empty. Add track to the playlist")
        else:
            for index, track in enumerate(self.tracks, start=1):
                print(f"{index}. {track}")

    def add_track(self, track):
        if track not in self.tracks:
            self.tracks.append(track)
            self.save_playlist()
            print(f"Track '{track}' has been added to '{self.playlist}' playlist")
        else:
            print(f"Track '{track}' already in playlist.")

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            self.save_playlist()
            print(f"Track '{track}' has been removed from playlist")
        else:
            print(f"The track {track} does not exist.")

    def shuffle_tracks(self):
        random.shuffle(self.tracks)
        self.save_playlist()

    def save_playlist(self):
        with open(self.playlist+'.txt', 'w') as file:
            file.write('\n'.join(self.tracks))

    def count_tracks(self):
        return len(self.tracks)

    def total_duration(self):
        return f"{len(self.tracks) * 5} mins"

    def clear_playlist(self):
        self.tracks = []
        self.save_playlist()

    def is_empty(self):
        print(len(self.tracks) == 0)


# Creating an instance of MP3Playlist
playlist1 = MP3Playlist('love')

# Loading tracks from a file
playlist1.load_playlist()

# # Displaying tracks
playlist1.display_tracks()

# # add new track
playlist1.add_track("New Song")

# # Removing a track
playlist1.remove_track("New Song")

# # Shuffling tracks
playlist1.shuffle_tracks()

# # Displaying tracks
playlist1.display_tracks()

# Counting tracks and calculating total duration
num_tracks = playlist1.count_tracks()
total_duration = playlist1.total_duration()
print(f"Number of tracks: {num_tracks}")
print(f"Total duration: {total_duration} minutes")

# Clearing the playlist
playlist1.clear_playlist()

# check if playlist is empty
playlist1.is_empty()

# # Saving playlist to a file
# playlist1.save_playlist('new_playlist.txt')
#
# # Clearing the playlist
# playlist1.clear_playlist()


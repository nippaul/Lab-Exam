
# Song class
class Song:
    def __init__(self, song_id, song_title, artist, duration):
        self.song_id = song_id
        self.song_title = song_title
        self.artist = artist
        self.duration = duration


# Node class
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # Check if list is empty
    def is_empty(self):
        return self.head is None

    # Add song at beginning
    def insert_first(self, song):
        new_node = Node(song)

        new_node.next = self.head
        self.head = new_node

        self.count += 1

    # Add song at end
    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.count += 1

    # Insert song at specific position
    def insert_at(self, position, song):

        # Position 1 means beginning
        if position == 1:
            self.insert_first(song)
            return True

        if position < 1 or position > self.count + 1:
            return False

        new_node = Node(song)

        current = self.head

        # Move to the node before the desired position
        for i in range(position - 2):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1

        return True

    # Display playlist
    def display(self):
        if self.is_empty():
            print("\nPlaylist is empty.")
            return

        print("\n========== PLAYLIST ==========")

        current = self.head
        position = 1

        while current is not None:
            song = current.song

            print("Position:", position)
            print("Song ID:", song.song_id)
            print("Song Title:", song.song_title)
            print("Artist:", song.artist)
            print("Duration:", song.duration)
            print("------------------------------")

            current = current.next
            position += 1

        print("Total Songs:", self.count)

    # Search song
    def search(self, song_id):
        current = self.head

        while current is not None:
            if current.song.song_id == song_id:
                return current.song

            current = current.next

        return None

    # Remove song
    def delete(self, song_id):

        if self.head is None:
            return False

        # If first node is the song
        if self.head.song.song_id == song_id:
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head

        while current.next is not None:

            if current.next.song.song_id == song_id:
                current.next = current.next.next
                self.count -= 1
                return True

            current = current.next

        return False

    # Display playlist size
    def size(self):
        return self.count

def music_playlist_manager():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print("      MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Add at beginning
        if choice == "1":
            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            playlist.insert_first(song)

            print("Song added at the beginning.")

        # Add at end
        elif choice == "2":
            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            playlist.insert_last(song)

            print("Song added at the end.")

        # Insert at position
        elif choice == "3":
            song_id = input("Enter Song ID: ")
            song_title = input("Enter Song Title: ")
            artist = input("Enter Artist: ")
            duration = input("Enter Duration: ")

            position = int(input("Enter Position: "))

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            if playlist.insert_at(position, song):
                print("Song inserted successfully.")
            else:
                print("Invalid position.")

        # Display
        elif choice == "4":
            playlist.display()

        # Search
        elif choice == "5":
            song_id = input("Enter Song ID to search: ")

            song = playlist.search(song_id)

            if song is not None:
                print("\nSong Found!")
                print("Song ID:", song.song_id)
                print("Song Title:", song.song_title)
                print("Artist:", song.artist)
                print("Duration:", song.duration)
            else:
                print("Song not found.")

        # Remove
        elif choice == "6":
            song_id = input("Enter Song ID to remove: ")

            if playlist.delete(song_id):
                print("Song removed successfully.")
            else:
                print("Song not found.")

        # Size
        elif choice == "7":
            print("\nTotal Songs:", playlist.size())

        # Exit
        elif choice == "8":
            print("Exiting Music Playlist Manager...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run Part II
music_playlist_manager()
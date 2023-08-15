def main():
    song_list = []

    while True:
        print("\nMy Song List\n")
        print("1. Add Song")
        print("2. Show List of Songs")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            song = input("Enter a song: ")
            song_list.append(song)
        elif choice == "2":
            print("\nSongs:")
            for index, song in enumerate(song_list, start=1):
                print(f"{index}. {song}")
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

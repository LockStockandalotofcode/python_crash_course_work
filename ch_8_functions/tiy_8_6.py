# ### 8-6
# def city_country(city, country):
#     required = f"{city}, {country}"
#     return required.title()

# pair_1 = city_country('istanbul', 'turkey')
# pair_2 = city_country('delhi', 'india')
# pair_3 = city_country('las vegas', 'america')

# print(pair_1)
# print(pair_2)
# print(pair_3)

# ### 8-7
# def make_album(artist, title, songs=None):
#     """Return a dictionary of info about music album"""
#     album = {
#         'artist_name': artist.title(),
#         'album_title': title.title(),
#     }

#     if songs:
#         album['number of songs'] = songs
#     return album

# print(make_album('A R rahman', 'rehna tu'))
# print(make_album('hari haran', 'tu hi re'))
# print(make_album('punjabi M C', 'dhol jageero da'))
# print(make_album('punjabi M C', 'dhol jageero da', 5))

# ### 8-8

# while True:
#     print("\nEnter information about music album.")
#     print("(Enter quit to end this program.)")

#     artist__name = input("Enter artist name: ")
#     if artist__name == 'q':
#         break

#     album__title = input("Enter album name: ")
#     if album__title == 'q':
#         break

#     album_info = make_album(artist__name, album__title)
#     print(album_info)
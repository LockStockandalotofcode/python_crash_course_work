from pathlib import Path

# contents for cat file
contents_1 = "persian cat\n"
contents_1 += "scottish fold\n"
contents_1 += "turkish angolia\n"

# contents for dog file
contents_2 = "siberian husky\n"
contents_2 += "german shepher\n"
contents_2 += "shih tzu\n"

# make cats.txt file
path_1 = Path('cats.txt')
# write respective contents to this file
path_1.write_text(contents_1)

# make dogs.txt file
path_2 = Path('dogs.txt')
# write respective contents to this file
path_2.write_text(contents_2)
''' This program takes in a file of tv show names and the amount of seasons they have in the format below
20
Gunsmoke
30
The Simpsons

Then the information will be sorted and one document will be created to sort the shows, starting from the most amount of seasons to the least.
A second document will be created to list the shows in reverse alphabetical order.
'''

input_file = input('Type in the absolute or relative path to your file (or just file name if it\'s in the same folder as this program).\n')
output_key_value_file = input('Type the name of the document you want created to sort the shows by season amount.\n')
output_movie_titles_file = input('Type the name of the document you want created to list TV show names in reverse alphabetical order.\n')

movie_keys = []
movie_names = []
movies_dict = {}

with open(input_file, 'r') as movies_file:
    lines = movies_file.readlines()

    for line in lines:
        if line[-1:] == '\n':
            lines[lines.index(line)] = line[:-1]

    for index, element in enumerate(lines):
        if index % 2 == 0:
            if int(element) < 10:
                movie_keys.append(f'0{element}')
            else:
                movie_keys.append(element)
            continue
        movie_names.append(element)
    
    for i, key in enumerate(movie_keys):
        if key in movies_dict.keys():
            movies_dict[key] = f'{movies_dict[key]}; {movie_names[i]}'
            continue
        movies_dict[key] = movie_names[i]

movies_dict = sorted(movies_dict.items(), reverse=True)
movie_keys = sorted(movie_keys, reverse=True)
movie_names = sorted(movie_names, reverse=True)

with open(output_key_value_file, 'w') as output_keys:
    for key,value in movies_dict:
        output_keys.write(f'{int(key)}: {value}')
        output_keys.write('\n')

with open(output_movie_titles_file, 'w') as output_titles:
    for i in movie_names:
        output_titles.write(f'{i}')
        output_titles.write('\n')
"""
READ THIS FIRST:
Description: Implement the logic in the following functions to complete a
simple program that tracks the number of views for different movies:
- get_all_movies
- get_movie_views
- get_top_n_movies
- save_movie_view
"""

movies = [
            {'title':'Toy story','views':10},
            {'title':'The mummy','views':5},
            {'title':'Hellboy','views':158},
            {'title':'Halloween','views':3},
            {'title':'The lord of the rings','views':200},
            {'title':'The simpson the movie','views':300},
            {'title':'Butterfly effect','views':26},
            {'title':'Friday 13th','views':42},
            {'title':'Django','views':58},
            {'title':'Coco','views':16},
            {'title':'Up','views':100},
            {'title':'sea world','views':250},
        ]

# Write a function that receives a movie name as argument and tracks (increments) the number
# of views in a data structure.
def save_movie_view(movie_name):
    for movie in movies: 
            if movie_name in movie['title']:
                movie.update({'title':movie['title'],'views':movie['views'] +1 })
                return 'The movie {} has been viewed {} times.'.format(movie_name, movie['views'])  
            #else:
            #    movies.append({'title':movie_name,'views':1})
            #    return 'The movie {} has been viewed {} times.'.format(movie_name, 1)  


# Write a function that returns the top N most viewed movies as a list, sorted
# in descending order
def get_top_n_movies(N):
    newlist = sorted(movies, key=lambda k: k['views'], reverse = True)[:N]
    all_movies = []
    for movie in newlist: 
        all_movies.append(movie)
    return all_movies


# Write a function that receives a movie name as argument and returns the
# number of views for that movie.
def get_movie_views(name):
    for movie in movies: 
            if name in movie['title']:
                return 'Title: ' + movie['title'] + ' views: ' + str(movie['views'])
                


# Write a function that returns all the movies seen by the user in ascending
# order.
def get_all_movies():
    newlist = sorted(movies, key=lambda k: k['title']) 
    all_movies = []
    for movie in newlist: 
        all_movies.append(movie)
    return all_movies

get_movie_views('Halloween')
get_top_n_movies(2)
get_all_movies()
save_movie_view('sjjwd')
save_movie_view('new titile')

####
name = 'movie'

def get_movie_views(name):
    for movie in movies: 
            if name in movie['title']:
                print(movie['title'] + ' ' + str(movie['views']))
                return 'Title: ' + movie['title'] + ' views: ' + str(movie['views'])

get_movie_views(name)



#####
def save_movie_view(movie_name):
    movies.append({'title':movie_name,'views':0})
    return 'The movie {} has been created.'.format(movie_name)

save_movie_view('new titile')



movies = [
            {'title':'sjjwd','views':10},
            {'title':'ktore 2','views':5},
            {'title':'aaaaa 3','views':158},
        ]
###
def get_all_movies():
    newlist = sorted(movies, key=lambda k: k['title']) 
    all_movies = []
    for movie in newlist: 
        all_movies.append(movie)
    return all_movies

get_all_movies()


###

def get_top_n_movies(N):
    newlist = sorted(movies, key=lambda k: k['views'], reverse = True)[:N]
    all_movies = []
    for movie in newlist: 
        all_movies.append(movie)
    return all_movies

get_top_n_movies(3)


movies = [
            {'title':'sjjwd','views':10},
            {'title':'ktore 2','views':5},
            {'title':'aaaaa 3','views':158},
        ]
def save_movie_view(movie_name):
    for movie in movies: 
            if movie_name in movie['title']:
                movie.update({'title':movie['title'],'views':movie['views'] +1 })
                return 'The movie {} has been viewed {} times.'.format(movie_name, movie['views'])  
            else:
                movies.append({'title':movie_name,'views':1})
                return 'The movie {} has been viewed {} times.'.format(movie_name, 1)  


save_movie_view('Batman')


import random

# class to hold ranking and count data
class movies:
    ranking_list = [] # [vid1, vid2, vid3 ... vid10]
    vids = {} # {title: count}

    def ranking(self):
        return [vid.title for vid in self.ranking_list[:11]]


# class to hold movie data and methods to plan movie.
class movie(movies):
    # create move and add movie to movies list
    def __init__(self, title=None):
        self.title = title
        movies.vids[title] = 0

    # play the move, track counts, maintain ranking order in movies.
    # time complexity O(n) n is number of movies
    def play(self):
        # incriment ranking
        movies.vids[self.title]  += 1
        rank = None

        # determine if move in ranking. if so maintain ranking sorted
        if self in [vid for vid in movies.ranking_list]:
            rank = self.ranking_list.index(self)
            while rank > 0:
                movie1 = self.ranking_list[rank-1].title
                movie2 = self.ranking_list[rank].title
                if movies.vids[movie1] < movies.vids[movie2]:
                    self.ranking_list[rank-1], self.ranking_list[rank] = \
                    self.ranking_list[rank], self.ranking_list[rank-1]
                else:
                    break
                rank -= 1
        # if not append move to ranking list
        else:
            self.ranking_list.append(self)

    def get_count(self):
        return movies.vids[self.title]




myMovies = movies()
# create movies and add to movies list
vid1 = movie('Matrix1')
vid2 = movie('Blade Runner')
vid3 = movie('Dune')
vid4 = movie('2001 Space Odyssey')
vid5 = movie('Iron Man')
vid6 = movie('Snowpiercer')
vid7 = movie('Star Trek')
vid8 = movie('Fly')
vid9 = movie('Lord Of The Rings')
vid10 = movie('Star Wars')
vid11 = movie('The Martian')
vid12 = movie('Intersteller')

# for testing, randomly play 20,000 movies
shelf = [vid1, vid2, vid3, vid4, vid5, vid6, vid7, vid8, vid9, vid10, vid11, vid12]
number_of_tests = 20000
for i in range(number_of_tests):
    choose = random.randint(0, len(shelf)-1)
    shelf[choose].play()

# ensure our ranking system is working.
print('{0:^20}'.format("title"), 'count')
for i in [x.title for x in movies.ranking_list[0:10]]:
    print('{0:<20}'.format(i), movies.vids[i])

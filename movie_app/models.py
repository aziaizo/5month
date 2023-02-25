from django.db import models


class Director(models.Model):
    name=models.CharField(max_length=100)

    @property
    def movie_count(self):
        return self.movies.all().count()


    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    duration=models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True,related_name='movies')

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name


class Review(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, null=True,
                            related_name='movie_reviews')
    stars=models.IntegerField(choices=(
        (1, '*'),
        (2, '* *'),
        (3, '* * *'),
        (4, '* * * *'),
        (5, '* * * * *')
    ), default=5)




    def __str__(self):
        return self.text
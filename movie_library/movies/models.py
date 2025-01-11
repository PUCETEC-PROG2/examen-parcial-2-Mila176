
class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, default='Unknown')
    author = models.CharField(max_length=100, default='Unknown author')  
    year = models.IntegerField()
    synopsis = models.TextField(default='No synopsis available')


    def _str_(self):
        return self.title


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def _str_(self):
        return self.name
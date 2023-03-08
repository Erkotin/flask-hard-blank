from dao.movie import MovieDAO

class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        return self.dao.get_all_movies(filters)

    def get_one(self, mid):
        return self.dao.get_by_id(mid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        return self.dao.update(data)

    def delete(self, mid):
        return self.dao.delete(mid)

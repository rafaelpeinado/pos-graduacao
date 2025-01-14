from uuid import UUID
from domain.user.user_entity import User
from domain.user.user_repository_interface import UserRepositoryInterface


class InMemoryUserRepository(UserRepositoryInterface):

    def __init__(self):
        self.users: list[User] = []


    def save(self, user: User) -> None:
        self.users.append(user)

    def get_by_id(self, user_id: UUID) -> User:
        return next(filter(lambda user: user.id == user_id, self.users), None)
        # return next((user for user in self.users if user.id == id), None)
        # for user in self.users:
        #    if (user.id == id):
        #        return user
        # return None

    def update(self, user: User) -> None:
        to_update_user = self.get_by_id(user.id)
        if to_update_user:
            self.users.remove(to_update_user)
            self.users.append(user)
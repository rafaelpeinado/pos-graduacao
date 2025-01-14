from unittest.mock import MagicMock
from uuid import UUID
from infra.user.in_memory_user_repository import InMemoryUserRepository
from application.user.create_user_use_case import CreateUserRequest, CreateUserResponse, CreateUserUseCase
from domain.user.user_repository_interface import UserRepositoryInterface


class TestCreateUser:

    # TESTE PARA CRIAR UM USUÁRIO COM DADOS VÁLIDOS
    def test_create_user_with_valid_data(self):

        # REPOSITORIO
        repository = InMemoryUserRepository()

        # CASO DE USO
        use_case = CreateUserUseCase(repository=repository)

        # INPUT (REQUEST)
        request = CreateUserRequest(name="Alexandre")

        # OUTPUT (RESPONSE)
        response = use_case.execute(request)

        assert len(repository.users) == 1
        assert isinstance(response.id, UUID)

        persisted_user = repository.users[0]

        assert persisted_user.id == response.id
        assert persisted_user.name == "Alexandre"

        




    
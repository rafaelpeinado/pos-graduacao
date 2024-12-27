from uuid import uuid4
from app.domain.task.task_entity import Task
from app.domain.user.user_entity import User


class TestUserWithTasks:

    # TESTE PARA ADICIONAR TAREFAS AO USUÁRIO
    def test_collect_tasks(self):

        user = User(id=uuid4(), name="William")
        task1 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes de integração",
            description="Description 1",
            completed=False
        )

        task2 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes unitários",
            description="Description 2",
            completed=False
        )

        user.collect_tasks([task1, task2])

        assert len(user.tasks) == 2
        assert task1 in user.tasks
        assert task2 in user.tasks
    
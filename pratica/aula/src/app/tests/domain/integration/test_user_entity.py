from uuid import uuid4
from app.domain.task.task_entity import Task
from domain.user.user_entity import User


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


    # TESTE PARA CONTABILIZAR TAREFAS PENDENTES DE UM USUÁRIO
    def test_count_pending_tasks(self):
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

        task3 = Task(
            id=uuid4(),
            user_id=user.id,
            title="Estudar sobre testes E2E",
            description="Description 3",
            completed=False
        )
        user.collect_tasks([task1, task2, task3])
        user.tasks[0].mark_as_completed()
        pending_count = user.count_pending_tasks()

        assert pending_count == 2
    

    # TESTE A QUANTIDADE DE TAREFAS PENDENTES QUANDO O USUÁRIO É CRIADO
    def test_count_pending_tasks_empty(self):
        user = User(id=uuid4(), name="Alexandre")
        pending_count = user.count_pending_tasks()
        assert pending_count == 0

    # TESTAR QUANDO TODAS AS TAREFAS DO USUÁRIO ESTÃO COMPLETADAS
    def test_all_tasks_completed(self):
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

        for task in user.tasks:
            task.mark_as_completed()
        
        pending_count = user.count_pending_tasks()
        assert pending_count == 0



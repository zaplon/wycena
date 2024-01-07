from wycena.db.models import Evaluation, Job, Transaction


def create_models():
    Evaluation.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    Transaction.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
    Job.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)

import unittest

import coverage

from flask_migrate import MigrateCommand
from flask_script import Manager

from users import create_app, db
from users.api.models import User


COV = coverage.coverage(
    branch=True,
    include='users/*',
    omit=[
        'users/tests/*'
    ]
)
COV.start()


app = create_app()
manager = Manager(app)


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(
        username='michael',
        email='michael@realpython.com',
        password='test'
    ))
    db.session.add(User(
        username='michaelherman',
        email='michael@mherman.org',
        password='test'
    ))
    db.session.commit()


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def test():
    """Runs the tests without code coverage."""
    tests = unittest.TestLoader().discover('users/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('users/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()

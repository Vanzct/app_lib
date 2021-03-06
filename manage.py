__author__ = 'Van'

import os
from flask.ext.script import Manager, Shell
# from flask.ext.migrate import Migrate, MigrateCommand
from app import create_app

app = create_app(os.getenv('APP_LIB_CONFIG') or 'default')
manager = Manager(app)


# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """aRun the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # manager.run()

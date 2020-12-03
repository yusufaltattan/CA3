import pylint.lint
pylint_opts = ['main.py', 'main_notification.py', 'main_alarm.py', 'weatherAPI.py', 'newsAPI.py']
pylint.lint.Run(pylint_opts)

import logging.config
 
LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': '%(asctime)s %(levelname)s [%(name)s: %(lineno)s] -- %(message)s',                                              
        'datefmt': '%m-%d-%Y %H:%M:%S'
    },
    'handlers': {
        'myapp.tasks.add': {
            'level': 'INFO',
            'filters:' None,
            'class': 'logging.FileHandler',
            'filename': 'addtask.log'
        },
        'myapp.tasks.subtract': {
            'level': 'INFO',
            'filters:' None,
            'class': 'logging.FileHandler',
            'filename': 'subtracttask.log'
        },
    },
    'loggers': {
         'myapp.tasks.add': {
            'handlers': ['myapp.tasks.add'],
            'level': 'INFO',
            'propagate': True,
        },
        'myapp.tasks.subtract': {
            'handlers': ['myapp.tasks.substract'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
 
logging.config.dictConfig(LOG_CONFIG)
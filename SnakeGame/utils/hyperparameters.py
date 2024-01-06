def get_hyperparameters():
    print('Hyperparameters has been set')
    params = dict()
    params['alpha'] = 0.01
    params['gamma'] = 0.9
    params['epsilon'] = 1.0
    params['epsilon_decay'] = 0.1
    params['min_epsilon'] = 0.0
    params['batch_size'] = 128
    params['mem_size'] = 10000
    
    return params

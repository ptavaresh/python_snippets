workers = [
    {
    'name': 'Pedro Tavares',
    'role': 'Dev',
    'email': 'ptavaresh@gmail.com'
    },
    {
    'name': 'Raul Hernandez',
    'role': 'Tester',
    'email': 'rhernandez@gmail.com'
    },
    {
    'name': 'Maria Gutierrez',
    'role': 'Product Owner',
    'email': 'mgutierrez@gmail.com'
    },
    {
    'name': 'Maro Bautista',
    'role': 'Dev',
    'email': 'mbautista@gmail.com'
    },
    {
    'name': 'Paulina Contreras',
    'role': 'Tester',
    'email': 'pcontreras@gmail.com'
    },
]


def look_for_worker(name):
    ''' Get an specific worker using its name'''
    for worker in workers:
        if name in worker['name']:
            return(worker)
    #return next(item for item in workers if item["name"] == name)

def read_workers():
    ''' Return all the workers '''
    return workers

def create_worker(name, role=None, email=None):
    ''' Create a new worker '''
    workers.append({'name': name, 'role': role, 'email':email})
    return 'The worker {} has been created with the email {} and the role {}.'.format(name, email, role)

def update_worker(name, role, email):
    ''' Update a existed worker. '''
    for worker in workers:
        if name in worker['name']:
            workers[workers.index(worker)] = {'name': name, 'role': role, 'email':email}
            return 'The worker {} has been updated with the email {} and the role {}.'.format(name, email, role)

def delete_worker(name):
    ''' Delete a existed worker. '''
    for worker in workers:
        if name in worker['name']:
            workers.remove(worker)
            return 'The worker {} has been deleted.'.format(name)



print(look_for_worker('Perro'))
print(create_worker('Rodrigo Meza', 'Dev'))
print(update_worker('Pedro Tavares', 'Tester', 'ptavaresh@gmail.com'))
print(delete_worker('Paulina Contreras'))
print(read_workers())
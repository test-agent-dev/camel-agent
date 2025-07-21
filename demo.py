from camel_agent import CamelAgent

if __name__ == '__main__':
    agent = CamelAgent()
    context = {
        'project_name': 'sample_project',
        'architecture': 'demo'
    }
    dest = agent.build_project('python_agent', context)
    print(f'Project generated at {dest}')

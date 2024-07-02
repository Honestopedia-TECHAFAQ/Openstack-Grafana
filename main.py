import openstack

def connect_to_openstack(config_file):
    """ Connects to OpenStack using the specified configuration file. """
    conn = openstack.connect(cloud='myopenstack', config_file=config_file)
    return conn

def list_subnets_by_tag(conn, tag_name):
    """ Retrieves subnets filtered by a specific tag. """
    subnets = conn.network.subnets()
    filtered_subnets = [subnet for subnet in subnets if tag_name in subnet.tags]
    return filtered_subnets

def list_instances_by_project(conn):
    """ Retrieves instances grouped by project. """
    instances = conn.compute.servers()
    projects = {}
    for instance in instances:
        project_name = getattr(instance, 'project_name', 'Unknown')
        if project_name not in projects:
            projects[project_name] = []
        projects[project_name].append(instance)
    return projects

if __name__ == "__main__":
    config_file = 'path_to/openstack.yaml'

    conn = connect_to_openstack(config_file)
    tag_name = 'production'
    filtered_subnets = list_subnets_by_tag(conn, tag_name)
    print(f"Subnets with tag '{tag_name}':")
    for subnet in filtered_subnets:
        print(f"Subnet ID: {subnet.id}, Name: {subnet.name}")
    projects = list_instances_by_project(conn)
    print("\nInstances grouped by project:")
    for project, instances in projects.items():
        print(f"Project: {project}")
        for instance in instances:
            print(f" - Instance ID: {instance.id}, Name: {instance.name}")

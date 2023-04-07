

import copy

# Define the physical network resources
'''physical_network = {
    'nodes': {
        'node1': {'cpu': 8, 'memory': 16},
        'node2': {'cpu': 8, 'memory': 16},
        'node3': {'cpu': 8, 'memory': 16},
    },
    'links': {
        ('node1', 'node2'): {'bandwidth': 10},
        ('node2', 'node3'): {'bandwidth': 10},
        ('node1', 'node3'): {'bandwidth': 10},
    }
}
'''
# Define the virtual network request
'''
virtual_network = {
    'nodes': {
        'vnode1': {'cpu': 4, 'memory': 8},
        'vnode2': {'cpu': 6, 'memory': 12},
        'vnode3': {'cpu': 2, 'memory': 4},
    },
    'links': {
        ('vnode1', 'vnode2'): {'bandwidth': 5},
        ('vnode2', 'vnode3'): {'bandwidth': 5},
        ('vnode1', 'vnode3'): {'bandwidth': 5},
    }
}
'''
def vne_mapping(physical_network, virtual_network):
    """
    Performs Virtual Network Embedding (VNE) by mapping virtual nodes and links to physical nodes and links.

    Args:
        physical_network (dict): A dictionary representing the physical network resources.
        virtual_network (dict): A dictionary representing the virtual network request.

    Returns:
        dict: A dictionary containing the mapping of virtual nodes and links to physical nodes and links.
            The keys are the virtual node and link names, and the values are the corresponding physical node and link names.
    """
    mapping = {}  # Dictionary to store the mapping of virtual nodes and links to physical nodes and links



    # Iterate through each virtual node in the virtual network request
    for vnode in virtual_network['nodes']:
        vnode_resources = virtual_network['nodes'][vnode]  # Resources required by the virtual node

        # Iterate through each physical node in the physical network
        for pnode in physical_network['nodes']:
            pnode_resources = physical_network['nodes'][pnode]  # Resources available in the physical node

            # Check if the physical node has enough resources to map the virtual node
            if vnode_resources['cpu'] <= pnode_resources['cpu'] and \
               vnode_resources['memory'] <= pnode_resources['memory']:
                # If yes, add the mapping of the virtual node to the physical node
                mapping[vnode] = pnode
                # Update the available resources in the physical node
                physical_network['nodes'][pnode]['cpu'] -= vnode_resources['cpu']
                physical_network['nodes'][pnode]['memory'] -= vnode_resources['memory']
                break  # Move to the next virtual node

    # Iterate through each virtual link in the virtual network request
    for vlink in virtual_network['links']:
        vlink_bandwidth = virtual_network['links'][vlink]['bandwidth']  # Bandwidth required by the virtual link

        # Iterate through each physical link in the physical network
        for plink in physical_network['links']:
            plink_bandwidth = physical_network['links'][plink]['bandwidth']  # Bandwidth available in the physical link
        # Check if the physical link has enough bandwidth to map the virtual link
            if vlink_bandwidth <= plink_bandwidth:
                # If yes, add the mapping of the virtual link to the physical link
                mapping[vlink] = plink
                # Update the available bandwidth in the physical link
                physical_network['links'][plink]['bandwidth'] -= vlink_bandwidth
                break  # Move to the next virtual link

    return mapping
#end of VNE function

# Take input for the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Initialize an empty dictionary to store the physical network information
physical_network = {'nodes': {}, 'links': {}}

# Take input for nodes' cpu and memory
for i in range(1, num_nodes + 1):
    node_name = f'node{i}'
    cpu = int(input(f"Enter CPU for {node_name}: "))
    memory = int(input(f"Enter memory for {node_name}: "))
    physical_network['nodes'][node_name] = {'cpu': cpu, 'memory': memory}

# Take input for links' bandwidth
for i in range(1, num_nodes):
    for j in range(i + 1, num_nodes + 1):
        link_name = f'link{i}_{j}'
        bandwidth = int(input(f"Enter bandwidth for {link_name}: "))
        physical_network['links'][(f'node{i}', f'node{j}')] = {'bandwidth': bandwidth}
print('\nphysical network: ')
print(physical_network)
print('\n')


#creating the virtual network request
#num_v_r=int(input("Enter the number of VNR: "))

while 1:
    print("Enter VNR Details")
    try:
        num_nodes = int(input("Enter the number of nodes: "))
    # Initialize an empty dictionary to store the virtual network information
    except:
        exit()

    virtual_network= {'nodes': {}, 'links': {}}

    # Take input for nodes' cpu and memory
    for i in range(1, num_nodes + 1):
        node_name = f'vnode{i}'
        cpu = int(input(f"Enter CPU for {node_name}: "))
        memory = int(input(f"Enter memory for {node_name}: "))
        virtual_network['nodes'][node_name] = {'cpu': cpu, 'memory': memory}

    # Take input for links' bandwidth
    for i in range(1, num_nodes):
        for j in range(i + 1, num_nodes + 1):
            link_name = f'link{i}_{j}'
            bandwidth = int(input(f"Enter bandwidth for  {link_name}: "))
            virtual_network['links'][(f'vnode{i}', f'vnode{j}')] = {'bandwidth': bandwidth}

    mapping = vne_mapping(physical_network, virtual_network)
    
    #printing the virtual nodes 
    print("\nMapping of virtual nodes and links to physical nodes and links:")
    for key, value in mapping.items():
        print(f"{key} --> {value}")
    print('\n')



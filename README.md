# Cloud Computing project

Team Members
1. Abhinav Gupta
2. Anupam Lal
3. Shubhanshu Singh
4. Vamshikrishna M



### Psudo Code
1. Initialize an empty dictionary mapping to store the mapping of virtual nodes and links to physical nodes and links.
2. Iterate through each virtual node in the virtual network request.
3. For each virtual node, iterate through each physical node in the physical network.
4. Check if the physical node has enough resources (CPU and memory) to map the virtual node.
5. If yes, add the mapping of the virtual node to the physical node in the mapping dictionary, update the available resources in the physical node, and move to the next virtual node.
6. Iterate through each virtual link in the virtual network request.
7. For each virtual link, iterate through each physical link in the physical network.
8. Check if the physical link has enough bandwidth to map the virtual link.
9. If yes, add the mapping of the virtual link to the physical link in the mapping dictionary, update the available bandwidth in the physical link, and move to the next virtual link.
10. Return the mapping dictionary containing the mapping of virtual nodes and links to physical nodes and links.

### Example:
##### physical Network 
physical_network = {
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

##### virtual network request
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
#### Output

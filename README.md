# Cloud Computing project

### Team Members
1. Abhinav Gupta
2. Anupam Lal
3. Shubhanshu Singh
4. Vamshikrishna M


#### Execute VNE-code.py for results


### Example:
#### Sample input and output

##### Sample input 
![image](https://user-images.githubusercontent.com/79687143/230666006-e9b9be29-23fa-458c-bdaa-25592e21cd44.png)


##### Output of above input and  Resource utilization:

![image](https://user-images.githubusercontent.com/79687143/230665656-aac8d7d4-565a-437e-8364-ec155bd01fe7.png)

###### The loop will go on until anything other than the integer given as output.


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

The added print statements display the updated resource utilization, including CPU, memory, and bandwidth, in the physical nodes and links, providing valuable information for monitoring and analyzing resource utilization during VNE. This allows for better understanding and management of the physical network's resource usage during virtual network embedding

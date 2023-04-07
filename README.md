# Cloud Computing project

### Team Members
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
##### Sample input and output

![image](https://user-images.githubusercontent.com/79687143/230660581-b0292072-81cb-4549-b268-86c65c139fdb.png)


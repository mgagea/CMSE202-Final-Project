#Code to define the attributes of the class Block_Group
class Block_Groups:
    def __init__(gdf, target_pop, margin=1000):
        self.target_pop = target_pop
        self.margin = margin

        

    
    def group_blocks(gdf, target_population, margin=1000):
    """
    Groups blocks into supergroups based on adjacency and population criteria.
    
    Parameters:
    - gdf: GeoDataFrame containing all blocks with their population.
    - target_population: The target population for each group.
    - margin: The margin of error for the target population.
    
    Returns:
    - A list of GeoDataFrames, each representing a grouped superblock.
    """
    grouped_blocks = []
    visited = set()
    
    for index, block in gdf.iterrows():
        if index in visited:
            continue
        
        current_group = [block]
        current_population = block['VALUE9']
        queue = [block]
        visited.add(index)
        
        while queue:
            current_block = queue.pop(0)
            if current_population >= target_population - margin and current_population <= target_population + margin:
                break
            
            adjacents = find_adjacent_blocks(current_block, gdf)
            
            for _, adj_block in adjacents.iterrows():
                adj_index = adj_block.name
                if adj_index not in visited and current_population + adj_block['VALUE9'] <= target_population + margin:
                    visited.add(adj_index)
                    current_group.append(adj_block)
                    current_population += adj_block['VALUE9']
                    queue.append(adj_block)
        
        if current_group:
            grouped_blocks.append(gpd.GeoDataFrame(current_group))
    
    return grouped_blocks
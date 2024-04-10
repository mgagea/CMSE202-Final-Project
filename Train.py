#Creates a train line or something
class Train:
    def __init__(superblocks, no_lines = 2, cen_stop):
        self.superblocks = superblocks
        self.no_lines = no_lines
        self.cent_stop = cen_stop
        self.cen = find_city_center(superblocks)
        verticies = id_verticies(self.superblocks, self.cen, self.no_lines)
        line_terms = assign_verticies(verticies)
        

    def find_city_center(self):
        x_vals = self.superblocks[:,0]
        y_vals = self.superblocks[:,1]
        x_mean = x_vals.mean()
        y_mean = y_vals.mean()
        return np.array(x_mean, y_mean)

    def id_verticies(superblocks, center, no_lines):
        # Calculate distances from central coordinate
        distances = np.linalg.norm(superblocks - center, axis=1)
        
        # Sort distances and get indices of n furthest coordinates
        furthest_indices = np.argsort(distances)[-no_lines*2:]
        
        # Extract the furthest coordinates
        furthest_coords = superblocks[furthest_indices]
        
        return furthest_coords

    def assign_verticies(verticies):
        all_pairs = list(combinations(verticies, 2))

        # Sort pairs by distance
        sorted_pairs = sorted(all_pairs, key=lambda pair: np.linalg.norm(pair[0] - pair[1]), reverse=True)
        
        # Group the coordinates into pairs
        furthest_pairs = []
        paired_indices = set()
        for pair in sorted_pairs:
            idx1 = np.where((furthest_coords == pair[0]).all(axis=1))[0][0]
            idx2 = np.where((furthest_coords == pair[1]).all(axis=1))[0][0]
            if idx1 not in paired_indices and idx2 not in paired_indices:
                furthest_pairs.append(pair)
                paired_indices.add(idx1)
                paired_indices.add(idx2)
        
        return furthest_pairs
    
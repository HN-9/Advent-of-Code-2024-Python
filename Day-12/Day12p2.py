with open("input.txt", "r") as file:
    garden_map = []
    for line in file:
        garden_map.append(list(map(str, line.strip())))

def get_area(region_cells):
    return len(region_cells)

def get_perimeter_sides(region_cells, garden_map):
    fence_coords = set()
    rows = len(garden_map)
    cols = len(garden_map[0]) if rows > 0 else 0
    for r, c in region_cells:
        if r == 0 or garden_map[r-1][c] != garden_map[r][c]:
            fence_coords.add(((r, c), "U"))
        if r == rows-1 or garden_map[r+1][c] != garden_map[r][c]:
            fence_coords.add(((r, c), "D"))
        if c == 0 or garden_map[r][c-1] != garden_map[r][c]:
            fence_coords.add(((r, c), "L"))
        if c == cols-1 or garden_map[r][c+1] != garden_map[r][c]:
            fence_coords.add(((r, c), "R"))

    return fence_coords

def fence_to_sides(fence_coords):
    edges = {}
    for (row, col), direction in fence_coords:
        if direction == "U":
            neighbor_row, neighbor_col = row - 1, col
        elif direction == "D":
            neighbor_row, neighbor_col = row + 1, col
        elif direction == "L":
            neighbor_row, neighbor_col = row, col - 1
        else:  # "R"
            neighbor_row, neighbor_col = row, col + 1

        edge_row = (row + neighbor_row) / 2
        edge_col = (col + neighbor_col) / 2
        edges[(edge_row, edge_col)] = (edge_row - row, edge_col - col)

    visited_edges = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in visited_edges:
            continue
        visited_edges.add(edge)
        side_count += 1
        edge_row, edge_col = edge
        if edge_row % 1 == 0:
            for delta_row in [-1, 1]:
                current_row = edge_row + delta_row
                next_edge = (current_row, edge_col)
                while edges.get(next_edge) == direction:
                    visited_edges.add(next_edge)
                    current_row += delta_row
                    next_edge = (current_row, edge_col)
        else:
            for delta_col in [-1, 1]:
                current_col = edge_col + delta_col
                next_edge = (edge_row, current_col)
                while edges.get(next_edge) == direction:
                    visited_edges.add(next_edge)
                    current_col += delta_col
                    next_edge = (edge_row, current_col)


    return side_count



def find_regions(garden_map):
    visited_cells = set()
    all_regions = []
    total_rows = len(garden_map)
    total_cols = len(garden_map[0]) if total_rows > 0 else 0

    def depth_first_search(start_row, start_col, crop_type):
        stack = [(start_row, start_col)]
        current_region = []
        while stack: 
            row, col = stack.pop()
            if (row, col) in visited_cells:
                continue
            visited_cells.add((row, col))
            current_region.append((row, col))
            for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor_row, neighbor_col = row + delta_row, col + delta_col
                if 0 <= neighbor_row < total_rows and 0 <= neighbor_col < total_cols:
                    if (garden_map[neighbor_row][neighbor_col] == crop_type and
                            (neighbor_row, neighbor_col) not in visited_cells):
                        stack.append((neighbor_row, neighbor_col))
        return current_region

    for row in range(total_rows):
        for col in range(total_cols):
            if (row, col) not in visited_cells:
                new_region = depth_first_search(row, col, garden_map[row][col])
                all_regions.append(new_region)

    return all_regions


regions = find_regions(garden_map)
total_price = 0
for region in regions:
    area = get_area(region)
    fence_coords = get_perimeter_sides(region, garden_map)
    sides_amount = fence_to_sides(fence_coords)
    total_price += area * sides_amount 

print(total_price)



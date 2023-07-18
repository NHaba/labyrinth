def is_valid_move(row_ini, row_fin, col_ini, col_fin, orientation, labyrinth):
    if row_ini < 0 or row_fin >= len(labyrinth) or col_ini < 0 or col_fin >= len(labyrinth[0]):
        return False

    if orientation == 'H':
        for i in range(col_ini, col_fin+1):
            if labyrinth[row_ini][i] == '#':
                return False
    else:
        for j in range(row_ini, row_fin+1):
            if labyrinth[j][col_ini] == '#':
                return False

    return True


def min_number_moves(labyrinth, rod_length):
    lab_rows = len(labyrinth)
    lab_cols = len(labyrinth[0])

    queue = []
    done_moves = set()
    distances = {}

    queue.append((0,0,0,rod_length-1,'H')) # row_ini, row_fin, col_ini, col_fin, orientation
    distances[(0,0,0,rod_length-1,'H')] = 0  # Initialize the distance for the starting position

    while queue:
        row_ini, row_fin, col_ini, col_fin, orientation = queue.pop()
        distance = distances[(row_ini, row_fin, col_ini, col_fin, orientation)]

        # Check if the current position is the destination
        if (row_fin+1) == lab_rows and (col_fin+1) == lab_cols:
            return distance

        moves = []
        '''
        if is_valid_move(row_ini + 1, row_fin + 1, col_ini, col_fin, orientation, labyrinth):
            moves.append((row_ini + 1, row_fin + 1, col_ini, col_fin, orientation))  # Move down
        if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, orientation, labyrinth):
            moves.append((row_ini - 1, row_fin - 1, col_ini, col_fin, orientation))  # Move up
        if is_valid_move(row_ini, row_fin, col_ini + 1, col_fin + 1, orientation, labyrinth):
            moves.append((row_ini, row_fin, col_ini + 1, col_fin + 1, orientation))  # Move right
        if is_valid_move(row_ini, row_fin, col_ini - 1, col_fin - 1, orientation, labyrinth):
            moves.append((row_ini, row_fin, col_ini - 1, col_fin - 1, orientation))  # Move left

        if orientation == 'H':
            # Check if rotating to vertical orientation is possible
            if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, 'H', labyrinth) & \
                    is_valid_move(row_ini + 1,row_fin + 1,col_ini, col_fin,'H', labyrinth):
                moves.append((row_ini - 1, row_fin + 1, col_ini + 1, col_fin - 1, 'V'))  # Rotate to vertical
        else:
            # Check if rotating to vertical orientation is possible
            if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, 'V', labyrinth) & \
                    is_valid_move(row_ini + 1,row_fin + 1,col_ini, col_fin,'V', labyrinth):
                moves.append((row_ini - 1, row_fin + 1, col_ini + 1, col_fin - 1, 'H'))  # Rotate to vertical

        # Process valid moves
        for move in moves:
            if move not in done_moves:
                queue.append(move)
                done_moves.add(move)
                distances[move] = distance + 1  # Update the distance for the new position
                
        '''
        if orientation == 'H':
            if is_valid_move(row_ini + 1, row_fin + 1, col_ini, col_fin, 'H', labyrinth):
                moves.append((row_ini + 1, row_fin + 1, col_ini, col_fin, 'H'))  # Move down
            if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, 'H', labyrinth):
                moves.append((row_ini - 1, row_fin - 1, col_ini, col_fin, 'H'))  # Move up
            if is_valid_move(row_ini, row_fin, col_ini + 1, col_fin + 1, 'H', labyrinth):
                moves.append((row_ini, row_fin, col_ini + 1, col_fin + 1, 'H'))  # Move right
            if is_valid_move(row_ini, row_fin, col_ini - 1, col_fin - 1, 'H', labyrinth):
                moves.append((row_ini, row_fin, col_ini - 1, col_fin - 1, 'H'))  # Move left

            # Check if rotating to vertical orientation is possible
            if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, 'H', labyrinth) & is_valid_move(row_ini + 1, row_fin + 1, col_ini, col_fin, 'H', labyrinth):
                moves.append((row_ini - 1, row_fin + 1, col_ini + 1, col_fin - 1, 'V'))  # Rotate to vertical

            # Process valid moves
            for move in moves:
                if move not in done_moves:
                    queue.append(move)
                    done_moves.add(move)
                    distances[move] = distance + 1  # Update the distance for the new position

        else:
            if is_valid_move(row_ini + 1, row_fin + 1, col_ini, col_fin, 'V', labyrinth):
                moves.append((row_ini + 1, row_fin + 1, col_ini, col_fin, 'V'))  # Move down
            if is_valid_move(row_ini - 1, row_fin - 1, col_ini, col_fin, 'V', labyrinth):
                moves.append((row_ini - 1, row_fin - 1, col_ini, col_fin, 'V'))  # Move up
            if is_valid_move(row_ini, row_fin, col_ini + 1, col_fin + 1, 'V', labyrinth):
                moves.append((row_ini, row_fin, col_ini + 1, col_fin + 1, 'V'))  # Move right
            if is_valid_move(row_ini, row_fin, col_ini - 1, col_fin - 1, 'V', labyrinth):
                moves.append((row_ini, row_fin, col_ini - 1, col_fin - 1, 'V'))  # Move left

            # Check if rotating to horizontal orientation is possible
            if is_valid_move(row_ini, row_fin, col_ini + 1, col_fin + 1, 'V', labyrinth) & is_valid_move(row_ini, row_fin, col_ini - 1, col_fin - 1, 'V', labyrinth):
                moves.append((row_ini + 1, row_fin - 1 , col_ini - 1, col_fin + 1, 'H'))  # Rotate to horizontal

            # Process valid moves
            for move in moves:
                if move not in done_moves:
                    queue.append(move)
                    done_moves.add(move)
                    distances[move] = distance + 1  # Update the distance for the new position
        


    # If the destination is not reachable
    return -1


def main():
    # Example labyrinth
    labyrinth = [
        ['.', '.', '.', '.', '.','.','.','.','.'],
        ['#', '.', '.', '.', '#','.','.','.','.'],
        ['.', '.', '.', '.', '#','.','.','.','.'],
        ['.', '#', '.', '.', '.','.','.','#','.'],
        ['.', '#', '.', '.', '.','.','.','#','.'],
    ]
    rod_length = 3

    min_moves = min_number_moves(labyrinth, rod_length)

    if min_moves != -1:
        print(f"The minimal number of moves required is: {min_moves}")
    else:
        print("The destination is not reachable.")

if __name__ == "__main__":
    main()


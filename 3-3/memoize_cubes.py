def sum_cubes(n, cube_map):
    if n == 1:
        return 1
    else:
        if n in cube_map.keys():
            print("Found memoized value for " + str(n) +
                  ": " + str(cube_map[n]))
            return cube_map[n] + sum_cubes(n - 1, cube_map)
        else:
            print("Memoizing " + str(n))
            cube_map.update({n:  n ** 3})

        return cube_map[n] + sum_cubes(n - 1, cube_map)


cube_map = {}
print("Sum of cubes, up to 9: " + str(sum_cubes(9, cube_map)))
print("Sum of cubes, up to 13: " + str(sum_cubes(13, cube_map)))
print(cube_map)

import matplotlib.pyplot as plot
from random_walk import RandomWalk

# Keep plotting new walks until told otherwise
while True:
    # Make a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plot.style.use('classic')
    fig, ax = plot.subplots(figsize=(15, 9), dpi=128)

    point_nums = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_nums, cmap=plot.cm.Blues,
               edgecolors='none', s=1)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
               s=100)
    
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plot.show()

    # Ask the user if the would like to plot another walk if n then end loop.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
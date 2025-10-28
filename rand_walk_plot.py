import matplotlib.pyplot as plot
from random_walk import RandomWalk

# Keep plotting new walks until told otherwise
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plot.style.use('classic')
    fig, ax = plot.subplots()

    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')

    plot.show()

    # Ask the user if the would like to plot another walk if n then end loop.
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
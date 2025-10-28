import matplotlib.pyplot as plot
from motion import MolecularMotion

# Keep plotting until told otherwise
while True:
    # Make a random walk
    mm = MolecularMotion(5_000)
    mm.fill_path()

    # Plot the points in the walk
    plot.style.use('classic')
    fig, ax = plot.subplots(figsize=(15, 9), dpi=128)

    point_nums = range(mm.num_points)

    ax.plot(mm.x_values, mm.y_values, linewidth=1)
    ax.set_aspect('equal')
    
    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plot.show()

    # Ask the user if the would like to plot another walk if n then end loop.
    keep_running = input("Simulate another path? (y/n): ")
    if keep_running == 'n':
        break
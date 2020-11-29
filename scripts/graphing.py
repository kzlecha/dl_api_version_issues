from matplotlib import pyplot


def hist_one(population, population_label, title, xlabel):
    '''
    Create histogram for populations
    ---
    @param population: data vector
    @param title: string title for graph
    @param xlabel: string labels for x axis
    @param population_label: string labels for population
    ---
    displays output plot
    '''
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)
    pyplot.hist(population, bins=50, alpha=0.8, color="#81B29A", label=population_label)
    pyplot.title(title, fontsize=14, color='#2E282A')
    pyplot.xlabel(xlabel, fontsize=12, color='#2E282A')
    pyplot.ylabel("Frequency", fontsize=12, color='#2E282A')
    pyplot.xlim(0)
    pyplot.legend()
    pyplot.show()


def hist_two(population_1, population_2, label1, label2, title, xlabel):
    '''
    Create overlayed histogram for two different populations
    ---
    @param population_1: data vector
    @param population_2: data vector
    @param title: string title for graph
    @param xlabel: string labels for x axis
    @param label1, label2: string labels for two groups
    ---
    displays output plot
    '''
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)
    pyplot.hist(population_1, bins=50, alpha=0.8, color="#81B29A", label=label1)
    pyplot.hist(population_2, bins=50, alpha=0.8, color="#F2CC8F", label=label2)
    pyplot.title(title, fontsize=14, color='#2E282A')
    pyplot.xlabel(xlabel, fontsize=12, color='#2E282A')
    pyplot.ylabel("Frequency", fontsize=12, color='#2E282A')
    pyplot.xlim(0)
    pyplot.legend()
    pyplot.show()


def scatter_one(x, y, title, xlabel, ylabel, label1):
    '''
    Scatter plot
    ---
    @param x: data vector
    @param y: data vector
    @param title: string title for graph
    @param xlabel, ylabel: string labels for x and y axis
    @param label1: label of the population
    ---
    displays output plot
    '''
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)
    pyplot.scatter(x, y, alpha=0.75, color="#F2CC8F", label=label1)
    pyplot.title(title, fontsize=14, color='#2E282A')
    pyplot.xlabel(xlabel, fontsize=12, color='#2E282A')
    pyplot.ylabel(ylabel, fontsize=12, color='#2E282A')
    pyplot.xlim(0)
    pyplot.legend()
    pyplot.show()


def scatter_two(x, y, mask, title, xlabel, ylabel, label1, label2):
    '''
    Scatter two different populations
    ---
    @param x: data vector
    @param y: data vector
    @param mask: a mask over the indicies of x and y
    @param title: string title for graph
    @param xlabel, ylabel: string labels for x and y axis
    @param label1, label2: string labels for two groups
    ---
    displays output plot
    '''
    pyplot.figure(figsize=(14,7), dpi=150)
    pyplot.grid(color="#2E282A", alpha=0.5)
    pyplot.scatter(x[~mask], y[~mask], alpha=0.75, color="#F2CC8F", label=label2)
    pyplot.scatter(x[mask], y[mask], alpha=0.75, color="#81B29A", label=label1)
    pyplot.title(title, fontsize=14, color='#2E282A')
    pyplot.xlabel(xlabel, fontsize=12, color='#2E282A')
    pyplot.ylabel(ylabel, fontsize=12, color='#2E282A')
    pyplot.xlim(0)
    pyplot.legend()
    pyplot.show()

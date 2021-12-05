# ConnectX
# pip install parl==1.3.2 torch torchvision tqdm
# 1. Enable Internet in the Kernel (Settings side pane)

# 2. Curl cache may need purged if v0.1.6 cannot be found (uncomment if needed).
# Если не удается найти версию 0.1.6, может потребоваться очистка кеша Curl (при необходимости раскомментируйте).
# !curl -X PURGE https://pypi.org/simple/kaggle-environments

# ConnectX environment was defined in v0.1.6
# !pip install 'kaggle-environments>=0.1.6'

from kaggle_environments import evaluate, make, utils

env = make("connectx", debug=True)
env.render()

# Создать агента
# Для создания представления функция агента должна быть полностью инкапсулирована (без внешних зависимостей).
# Когда ваш агент сравнивается с другими, у него не будет доступа к образу докера Kaggle. Можно импортировать только
# следующее: модули стандартной библиотеки Python, gym, numpy, scipy, pytorch (1.3.1, только cpu) и многое другое
# может быть добавлено позже.
def cell_swarm(obs, conf):  # функция клеточный рой
    def evaluate_cell(cell):  # функция оценить ячейку
        """ evaluate qualities of the cell """  # оценивать качества клетки
        cell = get_patterns(cell)  # получить образцы
        cell = calculate_points(cell)  # подсчитывать баллы
        for i in range(1, conf.rows):
            cell = explore_cell_above(cell, i)
        return cell

    def get_patterns(cell):  # получить образцы
        """ get swarm and opponent's patterns of each axis of the cell """
        '''получить образцы роя и противника для каждой оси ячейки'''
        ne = get_pattern(cell["x"], lambda z: z + 1, cell["y"], lambda z: z - 1, conf.inarow)
        sw = get_pattern(cell["x"], lambda z: z - 1, cell["y"], lambda z: z + 1, conf.inarow)[::-1]

        cell["swarm_patterns"]["NE_SW"] = sw + [{"mark": swarm_mark}] + ne
        cell["opp_patterns"]["NE_SW"] = sw + [{"mark": opp_mark}] + ne

        e = get_pattern(cell["x"], lambda z: z + 1, cell["y"], lambda z: z, conf.inarow)
        w = get_pattern(cell["x"], lambda z: z - 1, cell["y"], lambda z: z, conf.inarow)[::-1]
        cell["swarm_patterns"]["E_W"] = w + [{"mark": swarm_mark}] + e
        cell["opp_patterns"]["E_W"] = w + [{"mark": opp_mark}] + e

        se = get_pattern(cell["x"], lambda z: z + 1, cell["y"], lambda z: z + 1, conf.inarow)
        nw = get_pattern(cell["x"], lambda z: z - 1, cell["y"], lambda z: z - 1, conf.inarow)[::-1]
        cell["swarm_patterns"]["SE_NW"] = nw + [{"mark": swarm_mark}] + se
        cell["opp_patterns"]["SE_NW"] = nw + [{"mark": opp_mark}] + se

        s = get_pattern(cell["x"], lambda z: z, cell["y"], lambda z: z + 1, conf.inarow)
        n = get_pattern(cell["x"], lambda z: z, cell["y"], lambda z: z - 1, conf.inarow)[::-1]
        cell["swarm_patterns"]["S_N"] = n + [{"mark": swarm_mark}] + s
        cell["opp_patterns"]["S_N"] = n + [{"mark": opp_mark}] + s
        return cell

    def get_pattern(x, x_fun, y, y_fun, cells_remained):
        """ get pattern of marks in direction """
        pattern = []
        x = x_fun(x)
        y = y_fun(y)
        # if cell is inside swarm's borders
        if y >= 0 and y < conf.rows and x >= 0 and x < conf.columns:
            pattern.append({
                "mark": swarm[x][y]["mark"]
            })
            # amount of cells to explore in this direction
            cells_remained -= 1
            if cells_remained > 1:
                pattern.extend(get_pattern(x, x_fun, y, y_fun, cells_remained))
        return pattern

    def calculate_points(cell):
        """ calculate amounts of swarm's and opponent's correct patterns and add them to cell's points """
        for i in range(conf.inarow - 1):
            # inarow = amount of marks in pattern to consider that pattern as correct
            inarow = conf.inarow - i
            swarm_points = 0
            opp_points = 0
            # calculate swarm's points and depth
            swarm_points = evaluate_pattern(swarm_points, cell["swarm_patterns"]["E_W"], swarm_mark, inarow)
            swarm_points = evaluate_pattern(swarm_points, cell["swarm_patterns"]["NE_SW"], swarm_mark, inarow)
            swarm_points = evaluate_pattern(swarm_points, cell["swarm_patterns"]["SE_NW"], swarm_mark, inarow)
            swarm_points = evaluate_pattern(swarm_points, cell["swarm_patterns"]["S_N"], swarm_mark, inarow)
            # calculate opponent's points and depth
            opp_points = evaluate_pattern(opp_points, cell["opp_patterns"]["E_W"], opp_mark, inarow)
            opp_points = evaluate_pattern(opp_points, cell["opp_patterns"]["NE_SW"], opp_mark, inarow)
            opp_points = evaluate_pattern(opp_points, cell["opp_patterns"]["SE_NW"], opp_mark, inarow)
            opp_points = evaluate_pattern(opp_points, cell["opp_patterns"]["S_N"], opp_mark, inarow)
            # if more than one mark required for victory
            if i > 0:
                # swarm_mark or opp_mark priority
                if swarm_points > opp_points:
                    cell["points"].append(swarm_points)
                    cell["points"].append(opp_points)
                else:
                    cell["points"].append(opp_points)
                    cell["points"].append(swarm_points)
            else:
                cell["points"].append(swarm_points)
                cell["points"].append(opp_points)
        return cell

    def evaluate_pattern(points, pattern, mark, inarow):
        """ get amount of points, if pattern has required amounts of marks and zeros """
        # saving enough cells for required amounts of marks and zeros
        for i in range(len(pattern) - (conf.inarow - 1)):
            marks = 0
            zeros = 0
            # check part of pattern for required amounts of marks and zeros
            for j in range(conf.inarow):
                if pattern[i + j]["mark"] == mark:
                    marks += 1
                elif pattern[i + j]["mark"] == 0:
                    zeros += 1
            if marks >= inarow and (marks + zeros) == conf.inarow:
                return points + 1
        return points

    def explore_cell_above(cell, i):
        """ add positive or negative points from cell above (if it exists) to points of current cell """
        if (cell["y"] - i) >= 0:
            cell_above = swarm[cell["x"]][cell["y"] - i]
            cell_above = get_patterns(cell_above)
            cell_above = calculate_points(cell_above)
            # points will be positive or negative
            n = -1 if i & 1 else 1
            # if it is first cell above
            if i == 1:
                # add first 4 points of cell_above["points"] to cell["points"]
                cell["points"][2:2] = [n * cell_above["points"][1], n * cell_above["points"][0]]
                # if it is not potential "seven" pattern in cell and cell_above has more points
                if abs(cell["points"][4]) < 2 and abs(cell["points"][4]) < cell_above["points"][2]:
                    cell["points"][4:4] = [n * cell_above["points"][2]]
                    # if it is not potential "seven" pattern in cell and cell_above has more points
                    if abs(cell["points"][5]) < 2 and abs(cell["points"][5]) < cell_above["points"][3]:
                        cell["points"][5:5] = [n * cell_above["points"][3]]
                    else:
                        cell["points"][7:7] = [n * cell_above["points"][3]]
                else:
                    cell["points"][6:6] = [n * cell_above["points"][2], n * cell_above["points"][3]]
                cell["points"].append(n * cell_above["points"][4])
                cell["points"].append(n * cell_above["points"][5])
            else:
                cell["points"].extend(map(lambda z: z * n, cell_above["points"]))
        else:
            cell["points"].extend([0, 0, 0, 0, 0, 0])
        return cell

    def choose_best_cell(best_cell, current_cell):
        """ compare two cells and return the best one """
        if best_cell is not None:
            for i in range(len(best_cell["points"])):
                # compare amounts of points of two cells
                if best_cell["points"][i] < current_cell["points"][i]:
                    best_cell = current_cell
                    break
                if best_cell["points"][i] > current_cell["points"][i]:
                    break
                # if ["points"][i] of cells are equal, compare distance to swarm's center of each cell
                if best_cell["points"][i] > 0:
                    if best_cell["distance_to_center"] > current_cell["distance_to_center"]:
                        best_cell = current_cell
                        break
                    if best_cell["distance_to_center"] < current_cell["distance_to_center"]:
                        break
        else:
            best_cell = current_cell
        return best_cell

    ###############################################################################
    # define swarm's and opponent's marks
    swarm_mark = obs.mark
    opp_mark = 2 if swarm_mark == 1 else 1
    # define swarm's center
    swarm_center_horizontal = conf.columns // 2
    swarm_center_vertical = conf.rows // 2

    # define swarm as two dimensional array of cells
    swarm = []
    for column in range(conf.columns):
        swarm.append([])
        for row in range(conf.rows):
            cell = {
                "x": column,
                "y": row,
                "mark": obs.board[conf.columns * row + column],
                "swarm_patterns": {},
                "opp_patterns": {},
                "distance_to_center": abs(row - swarm_center_vertical) + abs(column - swarm_center_horizontal),
                "points": []
            }
            swarm[column].append(cell)

    best_cell = None
    # start searching for best_cell from swarm center
    x = swarm_center_horizontal
    # shift to right or left from swarm center
    shift = 0

    # searching for best_cell
    while x >= 0 and x < conf.columns:
        # find first empty cell starting from bottom of the column
        y = conf.rows - 1
        while y >= 0 and swarm[x][y]["mark"] != 0:
            y -= 1
        # if column is not full
        if y >= 0:
            # current cell evaluates its own qualities
            current_cell = evaluate_cell(swarm[x][y])
            # current cell compares itself against best cell
            best_cell = choose_best_cell(best_cell, current_cell)

        # shift x to right or left from swarm center
        if shift >= 0:
            shift += 1
        shift *= -1
        x = swarm_center_horizontal + shift

    # return index of the best cell column
    return best_cell["x"]

# Test your Agent


env.reset()
# Play as the first agent against "negamax" agent.
env.run([cell_swarm, cell_swarm])
# env.run([cell_swarm, "negamax"])
# env.render(mode="ipython", width=500, height=450)  # работа в юпитер ноутбуке
# env.render(mode="human", width=500, height=450)  # работа через графический интерфейс
# env.render(mode="ansi", width=500, height=450)
# env.render(mode="html", width=500, height=450)



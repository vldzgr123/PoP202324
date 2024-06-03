import numpy as np

class CART:
    def __init__(self, max_depth=3, min_size=1):
        self.max_depth = max_depth
        self.min_size = min_size
        self.tree = None

    def fit(self, X, y):
        dataset = [list(X[i]) + [y[i]] for i in range(len(X))]
        self.tree = self.build_tree(dataset)

    def predict(self, row):
        return self._predict(self.tree, row)

    def build_tree(self, train):
        root = self.get_split(train)
        self.split(root, 1)
        return root

    def get_split(self, dataset):
        class_values = list(set(row[-1] for row in dataset))
        b_index, b_value, b_score, b_groups = 999, 999, 999, None
        for index in range(len(dataset[0])-1):
            for row in dataset:
                groups = self.test_split(index, row[index], dataset)
                gini = self.gini_index(groups, class_values)
                if gini < b_score:
                    b_index, b_value, b_score, b_groups = index, row[index], gini, groups
        return {'index': b_index, 'value': b_value, 'groups': b_groups}

    def test_split(self, index, value, dataset):
        left, right = list(), list()
        for row in dataset:
            if row[index] < value:
                left.append(row)
            else:
                right.append(row)
        return left, right

    def gini_index(self, groups, classes):
        n_instances = float(sum([len(group) for group in groups]))
        gini = 0.0
        for group in groups:
            size = float(len(group))
            if size == 0:
                continue
            score = 0.0
            for class_val in classes:
                p = [row[-1] for row in group].count(class_val) / size
                score += p * p
            gini += (1.0 - score) * (size / n_instances)
        return gini

    def to_terminal(self, group):
        outcomes = [row[-1] for row in group]
        return max(set(outcomes), key=outcomes.count)

    def split(self, node, depth):
        left, right = node['groups']
        del(node['groups'])
        if not left or not right:
            node['left'] = node['right'] = self.to_terminal(left + right)
            return
        if depth >= self.max_depth:
            node['left'], node['right'] = self.to_terminal(left), self.to_terminal(right)
            return
        if len(left) <= self.min_size:
            node['left'] = self.to_terminal(left)
        else:
            node['left'] = self.get_split(left)
            self.split(node['left'], depth+1)
        if len(right) <= self.min_size:
            node['right'] = self.to_terminal(right)
        else:
            node['right'] = self.get_split(right)
            self.split(node['right'], depth+1)

    def _predict(self, node, row):
        if row[node['index']] < node['value']:
            if isinstance(node['left'], dict):
                return self._predict(node['left'], row)
            else:
                return node['left']
        else:
            if isinstance(node['right'], dict):
                return self._predict(node['right'], row)
            else:
                return node['right']

# Пример использования класса CART
# Создаем небольшой датасет
X = [[2.771244718, 1.784783929],
     [1.728571309, 1.169761413],
     [3.678319846, 2.81281357],
     [3.961043357, 2.61995032],
     [2.999208922, 2.209014212],
     [7.497545867, 3.162953546],
     [9.00220326, 3.339047188],
     [7.444542326, 0.476683375],
     [10.12493903, 3.234550982],
     [6.642287351, 3.319983761]]
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

max_depth = 3
min_size = 1
cart = CART(max_depth, min_size)
cart.fit(X, y)

# Прогнозирование для нового набора данных
for row in X:
    prediction = cart.predict(row)
    print('Predicted=%d' % prediction)

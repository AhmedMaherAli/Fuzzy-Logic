class Inference:
    def __init__(self, variables):
        self.variables = variables

    def max(self, x, y):
        if x > y:
            return x
        return y

    def min(self, x, y):
        if x < y:
            return x
        return y

    def membership(self, premise):
        premise = premise.split()
        return self.variables[premise[0]].memberships[premise[2]]  # premise [0]->varName  premise[0]-> shapeName

    def doRule(self, expretion):
        if 'OR' in expretion:
            premise = expretion.split('OR', 1)  #split with maxSplit =1
            return max(self.doRule(premise[0]), self.doRule(premise[1]))
        elif 'AND' in expretion:
            premise = expretion.split('AND', 1)
            return min(self.doRule(premise[0]), self.doRule(premise[1]))
        elif 'NOT' in expretion:
            premise = expretion.split('NOT', 1)
            return 1 - self.doRule(premise[1])

        return self.membership(expretion)

    def doInference(self, rule):
        num = rule[0]  # i didnt use it
        rule = rule[2:]
        rule = rule.split("then")
        then = rule[1]
        return self.doRule(rule[0]), then.split()[2]  #value, shapeName


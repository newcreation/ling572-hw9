#imports
import sys
import operator

############# functions
# get vectors
def get_vectors(data_filename):
    data_file = open(data_filename, 'r')

    instances = {}
    labels = set()
    all_features = set()
    for line in data_file:
        line_array = line.split()
        instance_name = line_array[0]
        label = line_array[1]
    
        instances[instance_name] = {}
        instances[instance_name]['_label_'] = label
        labels.add(label)
            
        features = line_array[2::2] # every other word in line starting with third
        values = line_array[3::2] # every other word in line starting with fourth
            
        for f, v in zip(features, values):
            all_features.add(f)
            if not (f in instances[instance_name]):
                instances[instance_name][f] = v
            else:
                instances[instance_name][f] += v
        
    data_file.close()
    return [instances, labels, all_features]

def train(vectors, labels, all_features, min_gain):
    expected = {}
    # initialize all guesses to "guns"
    for vector in vectors:
        expected[vector] = "guns"
    
    rule_list = []

    rules_gain = get_gain(expected, vectors, labels)
    best_gain = rules_gain[2]
    while best_gain >= min_gain:
        rule_list.append((rules_gain[1], rules_gain[2]))
        expected = apply_rule(rules_gain[1], expected, vectors)
        rules_gain = get_gain(expected, vectors, labels)
        best_gain = rules_gain[2]

    return rule_list

def apply_rule(rule, expected, vectors):
    feature_present = rule[0]
    from_class = rule[1]
    to_class = rule[2]

    for vector in vectors:
        if feature_present in vectors[vector] and \
        from_class == expected[vector]:
            expected[vector] = to_class
    return expected

def get_gain(expected, vectors, labels):
    rules = {}
    best_gain = -10000
    best_rule = ["", "", ""]
    for vector in vectors:
        gold_label = vectors[vector]["_label_"]
        from_label = expected[vector]
        for feature in vectors[vector]:
            if feature == "_label_":
                continue
            if feature not in rules:
                rules[feature] = {}
            if from_label not in rules[feature]:
                rules[feature][from_label] = {}

            for label in labels:
                # formulate a rule going from expected[vector] to label
                # if feature is present in vector
                if label not in rules[feature][from_label]:
                    rules[feature][from_label][label] = 0

                # in the case that we'd get a new correct result
                if label == gold_label and from_label != gold_label:
                    rules[feature][from_label][label] += 1
                # in the case that we'd remove a correct result
                elif label != gold_label and from_label == gold_label:
                    rules[feature][from_label][label] -= 1

                # keep track of the best gain
                if rules[feature][from_label][label] >= best_gain:
                    best_gain = rules[feature][from_label][label]
                    best_rule = [feature, from_label, label]
    return [rules, best_rule, best_gain]

def print_model(model_filename, rule_list, init_label):
    model_file = open(model_filename, 'w')
    model_file.write(init_label + "\n")
    for rule_gain in rule_list:
        feature = rule_gain[0][0]
        from_label = rule_gain[0][1]
        to_label = rule_gain[0][2]
        gain = rule_gain[1]
        model_file.write(feature + " " + from_label + " " + to_label + " ")
        model_file.write(str(gain) + "\n")

############# main
#arguments
try: #do casting here, too
	train_data_filename = sys.argv[1]
	model_filename = sys.argv[2]
	min_gain = int(sys.argv[3])
except Exception:
	print "requires arguments: train_data model_file min_gain"

# read in vectors
v_list = get_vectors(train_data_filename)
vectors = v_list[0]
labels = v_list[1]
all_features = v_list[2]

rule_list = train(vectors, labels, all_features, min_gain)
print_model(model_filename, rule_list, "guns")




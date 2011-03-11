 
# model file has the default classname (i.e., the first class in the training data) in the first line, 
# followed by a list of transformations (one transformation per line). 
# The transformation line has the format “featName from_class to_class net_gain”.

#imports
import sys




def get_model(model_filename):
	model_file = open(model_filename,'r')
	return model_file.readlines()


def get_vectors(test_data_filename):
	vectors = {}
	labels = set()
	
	test_file = open(test_data_filename,'r')
	for instance in test_file.readlines():
		instance = instance.split()
		instance_name = instance[0]
		label = instance[1]
		features = line_array[2::2] 
		values = line_array[3::2]
		vectors[instance_name] = {}
		vectors[instance_name]["_label_"] = label
		labels.add(label)
		for (f, v) in zip(features, values):
			vectors[instance_name][f] = v
	return [vectors, labels]

def classify(vectors,model,N):
	# go into each instance
	# assign it the default class in the model
	# for each level in the model, up to N, test the instance to see if it has the trigger feature
	# if it does, do the transformation
	# save each time to system out
	data = {}
	for instance in vectors:
			curr_hypothesis = model[0]
			data[instance] = {}
			transformations = []
			data[instance]["_truelabel_"] = vectors[instance]["label"]
			for index in range(1,min(N,len(model)):
				feat_name,from_class,to_class,net_gain = model[index].split()
				if feat_name in vectors[instance]:
					if curr_hypothesis == from_class:
						transformations.append((feat_name,from_class,to_class))
						curr_hypothesis = to_class
			data[instance]["_syslabel_"] = to_class
			data[instance]["_transformations_"] = transformations
	return data
	
def print_sys(data,sys_output_filename):
	sys_file = open(sys_output_filename, 'r')
	correct = 0
	total = 0
	for instance in data:
		total +=1
		truelabel = data[instance]["_truelabel_"]
		syslabel = data[instance]["_syslabel_"]
		if truelabel==syslabel:
			correct +=1
		sys_file.write(instance+" ")
		sys_file.write(+truelabel" ")
		sys_file.write(syslabel+" ")
		for transformation in data[instance]["_transformations_"]:
			sys_file.write(transformation[0]+" "+transformation[1]+" "+transformation[2])
		sys_file.write("\n")
	return [correct,total]
		
def print_acc(correct,total):
	print "Correct: " + correct
	print "Total: " + total
	print "Accuracy " + correct/total

try:
	test_data_filename = sys.argv[1]
	model_filename = sys.argv[2]
	sys_output = sys.argv[3]
	N = int(sys.argv[4])
except Exception:
	print "requires arguments: train_data model_file sys_output N"
	
vectors,labels = get_vectors(test_data_filename)
model = get_model(model_filename)
data = classify(vectors,model,N)
correct,total = print_sys(data,sys_output_filename)
print_acc(correct,total)

 
# model file has the default classname (i.e., the first class in the training data) in the first line, 
# followed by a list of transformations (one transformation per line). 
# The transformation line has the format “featName from_class to_class net_gain”.

#imports
import sys




def get_model(model_filename):
	model_file = open(model_filename,'r')
	

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
	
#The command line is: TBL classify.sh test_data model_file sys_output N
try: #do casting here, too
	test_data_filename = sys.argv[1]
	model_filename = sys.argv[2]
	sys_output = sys.argv[3]
	N = sys.argv[4]
except Exception:
	print "requires arguments: train_data model_file sys_output N"
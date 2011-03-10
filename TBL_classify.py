 
# model file has the default classname (i.e., the first class in the training data) in the first line, 
# followed by a list of transformations (one transformation per line). 
# The transformation line has the format “featName from_class to_class net_gain”.

#imports
import sys

#arguments
#The command line is: TBL classify.sh test_data model_file sys_output N
try: #do casting here, too
	train_data_filename = sys.argv[1]
	model_file = sys.argv[2]
	sys_output = sys.argv[3]
	N = sys.argv[4]
except Exception:
	print "requires arguments: train_data model_file min_gain"





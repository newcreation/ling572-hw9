#imports
import sys

#arguments
try: #do casting here, too
	train_data_filename = sys.argv[1]
	model_file = sys.argv[2]
	min_gain = sys.argv[3]
except Exception:
	print "requires arguments: train_data model_file min_gain"



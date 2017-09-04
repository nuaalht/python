import input_data
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
data_sets = input_data.read_data_sets(FLAGS.train_dir, FLAGS.fake_data)
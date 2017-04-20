# Write out the graph for TensorBoard
model = build_rnn(len(vocab),
                  batch_size=batch_size,
                  num_steps=num_steps,
                  learning_rate=learning_rate,
                  lstm_size=lstm_size,
                  num_layers=num_layers)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    file_writer = tf.summary.FileWriter('./logs/1', sess.graph)

# Launch TensorBoard
tensorboard --logdir logs/1


# Use tf.name_scope() to pretify the graph
def build_rnn(num_classes, batch_size=50, num_steps=50, lstm_size=128, num_layers=2,
              learning_rate=0.001, grad_clip=5, sampling=False):
        
    if sampling == True:
        batch_size, num_steps = 1, 1

    tf.reset_default_graph()
    
    # Declare placeholders we'll feed into the graph
    with tf.name_scope('inputs'):
        inputs = tf.placeholder(tf.int32, [batch_size, num_steps], name='inputs')
        x_one_hot = tf.one_hot(inputs, num_classes, name='x_one_hot')
    
    with tf.name_scope('targets'):
        targets = tf.placeholder(tf.int32, [batch_size, num_steps], name='targets')
        y_one_hot = tf.one_hot(targets, num_classes, name='y_one_hot')
        y_reshaped = tf.reshape(y_one_hot, [-1, num_classes])
    
    keep_prob = tf.placeholder(tf.float32, name='keep_prob')
    
    # Build the RNN layers
    with tf.name_scope("RNN_layers"):
        lstm = tf.contrib.rnn.BasicLSTMCell(lstm_size)
        drop = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob=keep_prob)
        cell = tf.contrib.rnn.MultiRNNCell([drop] * num_layers)
    
    with tf.name_scope("RNN_init_state"):
        initial_state = cell.zero_state(batch_size, tf.float32)

    # Run the data through the RNN layers
    with tf.name_scope("RNN_forward"):
        rnn_inputs = [tf.squeeze(i, squeeze_dims=[1]) for i in tf.split(x_one_hot, num_steps, 1)]
        outputs, state = tf.contrib.rnn.static_rnn(cell, rnn_inputs, initial_state=initial_state)
    
    final_state = state
    
    # Reshape output so it's a bunch of rows, one row for each cell output
    with tf.name_scope('sequence_reshape'):
        seq_output = tf.concat(outputs, axis=1,name='seq_output')
        output = tf.reshape(seq_output, [-1, lstm_size], name='graph_output')
    
    # Now connect the RNN putputs to a softmax layer and calculate the cost
    with tf.name_scope('logits'):
        softmax_w = tf.Variable(tf.truncated_normal((lstm_size, num_classes), stddev=0.1),
                               name='softmax_w')
        softmax_b = tf.Variable(tf.zeros(num_classes), name='softmax_b')
        logits = tf.matmul(output, softmax_w) + softmax_b

    with tf.name_scope('predictions'):
        preds = tf.nn.softmax(logits, name='predictions')
    
    
    with tf.name_scope('cost'):
        loss = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y_reshaped, name='loss')
        cost = tf.reduce_mean(loss, name='cost')

    # Optimizer for training, using gradient clipping to control exploding gradients
    with tf.name_scope('train'):
        tvars = tf.trainable_variables()
        grads, _ = tf.clip_by_global_norm(tf.gradients(cost, tvars), grad_clip)
        train_op = tf.train.AdamOptimizer(learning_rate)
        optimizer = train_op.apply_gradients(zip(grads, tvars))
    
    # Export the nodes 
    export_nodes = ['inputs', 'targets', 'initial_state', 'final_state',
                    'keep_prob', 'cost', 'preds', 'optimizer']
    Graph = namedtuple('Graph', export_nodes)
    local_dict = locals()
    graph = Graph(*[local_dict[each] for each in export_nodes])
    
    return graph

# Hyperparameters testing
def train(model, epochs, file_writer):
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        # Use the line below to load a checkpoint and resume training
        #saver.restore(sess, 'checkpoints/anna20.ckpt')

        n_batches = int(train_x.shape[1]/num_steps)
        iterations = n_batches * epochs
        for e in range(epochs):

            # Train network
            new_state = sess.run(model.initial_state)
            loss = 0
            for b, (x, y) in enumerate(get_batch([train_x, train_y], num_steps), 1):
                iteration = e*n_batches + b
                start = time.time()
                feed = {model.inputs: x,
                        model.targets: y,
                        model.keep_prob: 0.5,
                        model.initial_state: new_state}
                summary, batch_loss, new_state, _ = sess.run([model.merged, model.cost, 
                                                              model.final_state, model.optimizer], 
                                                              feed_dict=feed)
                loss += batch_loss
                end = time.time()
                print('Epoch {}/{} '.format(e+1, epochs),
                      'Iteration {}/{}'.format(iteration, iterations),
                      'Training loss: {:.4f}'.format(loss/b),
                      '{:.4f} sec/batch'.format((end-start)))

                file_writer.add_summary(summary, iteration)

epochs = 20
batch_size = 100
num_steps = 100
train_x, train_y, val_x, val_y = split_data(chars, batch_size, num_steps)

for lstm_size in [128,256,512]:
    for num_layers in [1, 2]:
        for learning_rate in [0.002, 0.001]:
            log_string = 'logs/1/lr={},rl={},ru={}'.format(learning_rate, num_layers, lstm_size)
            writer = tf.summary.FileWriter(log_string)
            model = build_rnn(len(vocab), 
                    batch_size=batch_size,
                    num_steps=num_steps,
                    learning_rate=learning_rate,
                    lstm_size=lstm_size,
                    num_layers=num_layers)
            
            train(model, epochs, writer)


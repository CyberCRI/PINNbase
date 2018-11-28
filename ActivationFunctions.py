import tensorflow as tf

def tanhshrink(x):
    '''
    Implementation of the tanhshrink activation function for tensorflow.
    '''

    a = x - tf.tanh(x)
    return a

import tensorflow as tf

state = tf.Variable(0,name='count')
print(state.name)

one = tf.constant(1)

new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init = tf.initialize_all_variables() #初始化

with tf.Session() as sess:
     sess.run(init)  #run之后才能激活变量
     for _ in range(3):
         sess.run(update)
         print(sess.run(state))
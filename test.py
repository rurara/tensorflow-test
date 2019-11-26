# https://github.com/golbin/TensorFlow-Tutorials 예제 따라해보기 
# 텐서플로우의 기본적인 구성을 익힙니다.
import tensorflow as tf

# tf.constant: 말 그대로 상수입니다.
hello = tf.constant('Hello, TensorFlow!')
print(hello)

a = tf.constant(10)
b = tf.constant(32)
c = tf.add(a, b)  # a + b 로도 쓸 수 있음
print('heelo tf')
print(c)

# 위에서 변수와 수식들을 정의했지만, 실행이 정의한 시점에서 실행되는 것은 아닙니다.
# 다음처럼 Session 객제와 run 메소드를 사용할 때 계산이 됩니다.
# 따라서 모델을 구성하는 것과, 실행하는 것을 분리하여 프로그램을 깔끔하게 작성할 수 있습니다.
# 그래프를 실행할 세션을 구성합니다.

#https://github.com/tensorflow/tensorflow/issues/18538
#Session 금지되어 v1으로 사용 
session = tf.compat.v1.Session()
# sess.run: 설정한 텐서 그래프(변수나 수식 등등)를 실행합니다.
print(session.run(hello))
print(session.run([a, b, c]))

# 세션을 닫습니다.
session.close()


#https://gist.github.com/haje01/202ac276bace4b25dd3f

# 변수를 0으로 초기화
state = tf.Variable(0, name="counter")

# state에 1을 더할 오퍼레이션 생성
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 그래프는 처음에 변수를 초기화해야 합니다. 아래 함수를 통해 init 오퍼레이션을 만듭니다.   
init_op = tf.initialize_all_variables()

# 그래프를 띄우고 오퍼레이션들을 실행
with tf.Session() as sess:
  # 초기화 오퍼레이션 실행
  sess.run(init_op)
  # state의 초기 값을 출력
  print(sess.run(state))
  # state를 갱신하는 오퍼레이션을 실행하고, state를 출력
  for _ in range(3):
    sess.run(update)
    print(sess.run(state))
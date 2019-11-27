import tensorflow as tf
import numpy as np

# Numpy 랜덤으로 100개의 가짜 데이터 채우기. (float64 -> float32로 변환)
x_data = np.float32(np.random.rand(2, 100))
# 학습 레이블(목표값)은 아래의 식으로 산출. (W = [0.1, 0.2], b = 0.3)
y_data = np.dot([0.100, 0.200], x_data) + 0.300
#입력 데이터와 W, b를 사용해 선형 모델을 정의합니다.

# b는 0,
b = tf.Variable(tf.zeros([1]))
# W는 1x2 형태의 웨이트 변수 (균등 랜덤값으로 초기화)
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b
#이제 손실과 학습 함수를 정의 합니다. 평균 제곱 오차가 최소화 되는 지점을 경사하강법으로 구하게 됩니다.

# 손실 함수 정의
loss = tf.reduce_mean(tf.square(y - y_data))
# 경사하강법으로 손실 함수를 최소화 (0.5는 학습 비율)
optimizer = tf.train.GradientDescentOptimizer(0.5)
# 학습 오퍼레이션 정의
train = optimizer.minimize(loss)
#학습 세션을 시작합니다.

# 모든 변수를 초기화.
init = tf.initialize_all_variables()

# 세션 시작
sess = tf.Session()
sess.run(init)

# 200번 학습.
for step in xrange(0, 201):
    sess.run(train)
    if step % 20 == 0:
    	print ('야호')
        # print (step, sess.run(W), sess.run(b))
#https://gist.github.com/haje01/202ac276bace4b25dd3f
#경사 하강법(Gradient Descent)으로 인자 찾아내기
#아래의 예제는 가중치 행렬W와 바이어스b를 경사하강법을 통해서 찾아내는 것을 보여줍니다. 목표값은 간단한 식으로 산출되도록 합니다.


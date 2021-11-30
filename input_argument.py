import argparse
# python manage.py 0.0.0.0:8000 파일명 뒷부분이 아규먼트다.
args = argparse.ArgumentParser()
# 아규먼트를 받는 형식 지정. 값, 변수명
args.add_argument('-x', '--xVal', required=True)
#args.add_argument('-y', '--yVal', required=False)

argvar = vars(args.parse_args())
# print 쓰면 안되. pass로 마무리짓기
print(argvar)
pass



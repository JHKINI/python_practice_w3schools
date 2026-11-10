# 가상환경 만들기
python -m venv .venv

# 활성화 (Windows)
.venv\Scripts\activate

# 활성화 (macOS / Linux)
source .venv/bin/activate

# 가상환경 안에서 패키지 설치
pip install cowsay

# 설치된 패키지 목록 저장 / 복원
pip freeze > requirements.txt
pip install -r requirements.txt

# 비활성화
deactivate

# AI News Blog

AI 서비스 관련 뉴스를 자동으로 수집하여 발행하는 블로그입니다.

## 테마

이 블로그는 [Lanyon](https://github.com/poole/lanyon) 테마를 사용합니다.

## 로컬 실행 방법

### 1. Ruby 환경 설정

시스템 Ruby 대신 rbenv 또는 RVM을 사용하는 것이 권장됩니다:

```bash
# rbenv 설치 (Homebrew 사용)
brew install rbenv ruby-build

# rbenv 초기화
rbenv init

# Ruby 설치
rbenv install 3.1.3
rbenv global 3.1.3
```

### 2. 의존성 설치

```bash
# 의존성 설치
bundle install
```

### 3. 로컬 서버 실행

```bash
bundle exec jekyll serve
```

## 문제 해결

### google-protobuf 관련 오류

만약 `cannot load such file -- google/protobuf_c` 오류가 발생한다면:

1. Jekyll 버전을 낮추거나 sass-converter 버전 변경:
   ```ruby
   gem "jekyll", "~> 4.2.0"
   gem "jekyll-sass-converter", "~> 2.0"
   ```

2. 또는 다음 명령어로 로컬에 gem 설치:
   ```bash
   bundle config set --local path 'vendor/bundle'
   bundle install
   ```

## 라이센스

MIT
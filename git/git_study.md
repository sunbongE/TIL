# git

> 버전 관리 분산 시스템 	

**버전** : 컴퓨터 소프트웨어의 특정 상태를 의미함

---

### git 장점

네이버 같은 기업에서 예전 버전부터 현재 버전까지의 모든 버전의 용량이 25GB 하나의 폴더의 크기로 관리되게 만들어줌

**git은 스냅샷으로 관리하여 크기가 매우 작음** (틀린 그림 같은 느낌으로 달라진게 있으면 그부분만 추가해 관리하는거 같음)

---



### 기초 흐름

- 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 일들의 작업을 조율



1. 작업하면
2. add하여 staging area에모아(사용법 :` git add `파일명 or `git add .` )
3. commit 작성(`git commit -m '메시지' `을 통해 버전으로 기록한다.)

> staging area는 내가 버전으로 기록하기 위한 파일을 이 공간에 모은다.
>
> 보통 임시적인 공간으로 이용한다고 한다.

` git commit -m <커밋 메세지>`:내가 했던 작업이 무엇인지 알리는게 좋다.



---

### git은 파일을 modified, staged, committed 로 관리

**modified: 파일 수정상태라는 의미**

**staged :  수정한 파일을 곧 커밋할 것이라고 표시한 상태**

**committde : 커밋 된 상태**





---

### 명령어

| 명령어                                                       | 역할                                       |
| ------------------------------------------------------------ | ------------------------------------------ |
| **git init**                                                 | 로컬 저장소 생성                           |
| **git status**                                               | 상태를 알려줌                              |
| **git restore --staged** `<파일명>`                          | 수정내용 삭제                              |
| **git add** `<파일명>`                                       | 특정 파일/폴더의 변경 사항 추가, `.`: 전부 |
| **git commit -m** `'메시지' `                                | 커밋 메세지 입력                           |
| **git log -1**                                               | 이전 작업 1개만 가져오기                   |
| **git log --oneline**                                        | 한줄로 표시                                |
| **git log -2 --oneline**                                     | 최근 2개를 한줄로 보여줘                   |
| **git commit --amend**                                       | 커밋 메세지 변경                           |
| **git checkout -b [새로운 브랜치 이름]**                     | 브랜치 생성 후 이동                        |
| **git branch [새로운 브랜치 이름]**                          | 브랜치 생성                                |
| **git checkout [브랜치 이름]**                               | 브랜치 이동                                |
| **git branch**                                               | 브랜치 목록 보기                           |
| **git branch -d [삭제할 브랜치 이름]**                       | 브랜치 삭제                                |
| **git merge [병합할 브랜치 이름]**                           | 브랜치 병합                                |
| **git branch -m [현재 브랜치 이름] [새로운 브랜치 이름]**    | 브랜치 이름 변경                           |
| **git fetch [원격 저장소 이름]**                             | 원격 브랜치 가져오기                       |
| **git checkout -b [새로운 로컬 브랜치 이름] [원격 브랜치 이름]** | 원격 브랜치에서 로컬 브랜치 생성           |



---



# Git Status

## a.txt 파일을 만든 직후

> 빨간 글씨 => 1통

```bash
$ git status
On branch master

# 트래킹이 되고 있지 않은 파일?
# => 1통 (working directory)
# => 한번도 git으로 관리되고 있지 않은 파일!
Untracked files:
# git add 사용해봐...
# 포함시키기 위해서 / 커밋이 될 것 => 2통에 넣으려면
  (use "git add <file>..." to include in what will be committed)
        a.txt

# 커밋할 것은 없어 => 2통이 비어있어
# 하지만(but) 트래킹되지 않은 파일은 존재한다. 
# (git add 사용해서 트래킹해)
nothing added to commit but untracked files present (use "git add" to track)
```

## b.txt 파일을 만들고 add한 이후

> 초록 글씨 => 2통

```bash
$ git status
On branch master
# (커밋될) 변경사항들 => 2통
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
  		# 새로운 파일: b.txt
        new file:   b.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

```

# a.txt 파일과 b.txt 파일을 모두 add한 이후 커밋까지

```bash
$ git status
On branch master
# 2통, 1통 모두 클린~!
nothing to commit, working tree clean
```


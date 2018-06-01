Microsoft Windows [版本 6.1.7601]

版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

 

C:\Users\Administrator>git --version

git version 2.14.0.windows.1

 

C:\Users\Administrator>cd desktop

 

C:\Users\Administrator\Desktop>mkdir hello

 

C:\Users\Administrator\Desktop>cd hello

 

C:\Users\Administrator\Desktop\hello>git init

Initialized empty Git repository in C:/Users/Administrator/Desktop/hello/.git/

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add readme.txt

 

C:\Users\Administrator\Desktop\hello>git commit -m '写了一行'

 

*** Please tell me who you are.

 

Run

 

  git config --global user.email "you@example.com"

  git config --global user.name "Your Name"

 

to set your account's default identity.

Omit --global to set the identity only in this repository.

 

fatal: unable to auto-detect email address (got 'Administrator@USER-20180417VY.(

none)')

 

C:\Users\Administrator\Desktop\hello>git config --global user.email '462189066@q

q.com

 

C:\Users\Administrator\Desktop\hello>git config --global user.name 'huanghong'

 

C:\Users\Administrator\Desktop\hello>git commit -m '写了一行'

[master (root-commit) d571ecf] '写了一行'

 1 file changed, 1 insertion(+)

 create mode 100644 readme.txt

 

C:\Users\Administrator\Desktop\hello>git commit -m '写了一行'

On branch master

nothing to commit, working tree clean

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add .

 

C:\Users\Administrator\Desktop\hello>git status

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

 

​        modified:   readme.txt

 

 

C:\Users\Administrator\Desktop\hello>git commit -m '我帅啊‘

[master c582ed5] '我帅啊‘

 1 file changed, 2 insertions(+), 1 deletion(-)

 

C:\Users\Administrator\Desktop\hello>git log

commit c582ed5138938823c3979bf19971feec36247dad (HEAD -> master)

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:52:32 2018 +0800

 

​    '<E6><88><91><E5><B8><85><E5><95><8A><E2><80><98>

 

commit d571ecfcf9e652a08069b9be5206a03b5a7dcda3

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:43:25 2018 +0800

 

​    '<E5><86><99><E4><BA><86><E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reset --hard d571ec

HEAD is now at d571ecf '写了一行'

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git log

commit d571ecfcf9e652a08069b9be5206a03b5a7dcda3 (HEAD -> master)

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:43:25 2018 +0800

 

​    '<E5><86><99><E4><BA><86><E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reflog

d571ecf (HEAD -> master) HEAD@{0}: reset: moving to d571ec

c582ed5 HEAD@{1}: commit: '<E6><88><91><E5><B8><85><E5><95><8A><E2><80><98>

d571ecf (HEAD -> master) HEAD@{2}: commit (initial): '<E5><86><99><E4><BA><86>

<E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reset --hard c582ed5

HEAD is now at c582ed5 '我帅啊‘

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add .

 

C:\Users\Administrator\Desktop\hello>get status

'get' 不是内部或外部命令，也不是可运行的程序

或批处理文件。

 

C:\Users\Administrator\Desktop\hello>git status

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

 

​        modified:   readme.txt

 

 

C:\Users\Administrator\Desktop\hello>git checkout --

M       readme.txt

 

C:\Users\Administrator\Desktop\hello>git status

On branch master

Changes to be committed:

  (use "git reset HEAD <file>..." to unstage)

 

​        modified:   readme.txt

 

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add .

 

C:\Users\Administrator\Desktop\hello>git checkout --

M       readme.txt

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add .

 

C:\Users\Administrator\Desktop\hello>git commit -m '说错了'

[master 9763653] '说错了'

 1 file changed, 2 insertions(+), 1 deletion(-)

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>
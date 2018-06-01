Microsoft Windows [版本 6.1.7601]

版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

 

C:\Users\Administrator>git --version     <b>查看版本</b>

git version 2.14.0.windows.1

 

C:\Users\Administrator>cd desktop

 

C:\Users\Administrator\Desktop>mkdir hello

 

C:\Users\Administrator\Desktop>cd hello

 

C:\Users\Administrator\Desktop\hello>git init         #####初始化厂库

Initialized empty Git repository in C:/Users/Administrator/Desktop/hello/.git/

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git add readme.txt           <b>纳入厂库</b>

 

C:\Users\Administrator\Desktop\hello>git commit -m '写了一行'     <b>提交到本地厂库</b>

 

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

 

C:\Users\Administrator\Desktop\hello>git log                   <b>查询提交日志（有提交才行）</b>

commit c582ed5138938823c3979bf19971feec36247dad (HEAD -> master)

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:52:32 2018 +0800

 

​    '<E6><88><91><E5><B8><85><E5><95><8A><E2><80><98>

 

commit d571ecfcf9e652a08069b9be5206a03b5a7dcda3

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:43:25 2018 +0800

 

​    '<E5><86><99><E4><BA><86><E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reset --hard d571ec       <b>返回到上一个版本</b>

HEAD is now at d571ecf '写了一行'

 

C:\Users\Administrator\Desktop\hello>notepad readme.txt

 

C:\Users\Administrator\Desktop\hello>git log

commit d571ecfcf9e652a08069b9be5206a03b5a7dcda3 (HEAD -> master)

Author: huanghong <462189066@qq.com>

Date:   Fri May 11 09:43:25 2018 +0800

 

​    '<E5><86><99><E4><BA><86><E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reflog      <b>修改并提交几个版本过后，要去未来的某个版本</b>

d571ecf (HEAD -> master) HEAD@{0}: reset: moving to d571ec

c582ed5 HEAD@{1}: commit: '<E6><88><91><E5><B8><85><E5><95><8A><E2><80><98>

d571ecf (HEAD -> master) HEAD@{2}: commit (initial): '<E5><86><99><E4><BA><86>

<E4><B8><80><E8><A1><8C>'

 

C:\Users\Administrator\Desktop\hello>git reset --hard c582ed5  <b>同样能去未来某个版本</b>>

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

###建立分支
git branch     --查看当前分支
git branch de  --建立de分支
git checkout de   --切换分支
git add .     --再分支里建内容
git checkout master   --切换到主分支
git merge de     --合并到主分支

git branch -d de   --删除分支

###远端项目存在
git clone <url>  克隆远端项目

cd hello   进入项目文件夹

git add .  把修改好的内容纳入版本控制

git checkout --  如果有错，可以撤销

git commit -m 'aaa'  本地版本控制

git push origin master 推送到远端master分支

git pull  再次要用项目的东西直接pull





### 本地建立厂库再托管到远端

mkdir hello
cd hello
git init
git add .
git status
git commit -m 'aaa'
git log
git reset --hard id
git reflog
git remote add origin <url>
git push -u origin master
git pull







![git流程](D:\用户目录\我的图片\git流程.PNG)

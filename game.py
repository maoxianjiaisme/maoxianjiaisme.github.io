# -*- coding: utf-8 -*-
print(''' 

                        .;lc'
                 .,lxxkkkkOOOO000Ol'
            .':oxxxxxkkkkOOOO0000KK0x:'
          .;ldxxxxxxxxkxl,.'lk0000KKKXXXKd;.
       ':oxxxxxxxxxxo;.       .:oOKKKXXXNNNNOl.
      '';ldxxxxxdc,.              ,oOXXXNNNXd;,.
     .ddc;,,:c;.         ,c:         .cxxc:;:ox:
     .dxxxxo,     .,   ,kMMM0:.  .,     .lxxxxx:
     .dxxxxxc     lW. oMMMMMMMK  d0     .xxxxxx:
     .dxxxxxc     .0k.,KWMMMWNo :X:     .xxxxxx:
     .dxxxxxc      .xN0xxxxxxxkXK,      .xxxxxx:
     .dxxxxxc    lddOMMMMWd0MMMMKddd.   .xxxxxx:
     .dxxxxxc      .cNMMMN.oMMMMx'      .xxxxxx:
     .dxxxxxc     lKo;dNMN.oMM0;:Ok.    'xxxxxx:
     .dxxxxxc    ;Mc   .lx.:o,    Kl    'xxxxxx:
     .dxxxxxdl;. .,               .. .;cdxxxxxx:
     .dxxxxxxxxxdc,.              'cdkkxxxxxxxx:
      .':oxxxxxxxxxdl;.       .;lxkkkkkxxxxdc,.
          .;ldxxxxxxxxxdc, .cxkkkkkkkkkxd:.
             .':oxxxxxxxxx.ckkkkkkkkxl,.
                .,cdxxxxx.ckkkkkxc.
                    .':odx.ckxl,.
                        .,.'.
						
	This is My blog！ www.fjhack.me\n
	
	''')
print('''-----------------这是一个简单的网络安全题库程序！-----------------\n

''')

print('''PS：一共三十道比较简单的网络安全选择题，按照要求填入选项，程序会自动判断对错，加油！:)\n==================================================================''')

print('[提示：题目为选择题，按照要求填入A,B,C,D！请注意看题！可能会有多个答案哦！]')

A = raw_input('''第一题！\n应用程序开发过程中，下面那些开发习惯可能导致安全漏洞？\nA 在程序代码中打印日志输出敏感信息方便调式\nB 在使用数组前判断是否越界\nC 在生成随机数前使用当前时间设置随机数种子\nD 设置配置文件权限为rw-rw-rw-\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

B = raw_input('''第二题！\n以下哪些工具提供拦截和修改HTTP数据包的功能? \nA Burpsuite\nB Hackbar\nC Fiddler\nD Nmap\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

C = raw_input('''第三题！\n坏人通过XSS漏洞获取到QQ用户的身份后，可以进行以下哪些操作?\nA 偷取Q 币\nB 控制用户摄像头\nC 劫持微信用户\nD 进入QQ空间\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

D = raw_input('''第四题！\n以下哪些工具可以抓取HTTP数据包？\nA Burpsuite\nB Wireshark\nC Fiddler\nD Nmap\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

E = raw_input('''第五题！\n以下哪些说法是正确的？\nA iOS系统从IOS6开始引入kernelASLR安全措施\nB 主流的Iphone手机内置了AES及RSA硬件加速解密引擎\nC 安卓系统采用了安全引导链（secureboot chain ），而IOS系统则未采用\nD Android 4.1 系统默认启用了内存ASLR\n请输入你的答案： ''')

print('==================答题成功！进入下一题。============================================')

F = raw_input('''第六题！\n以下哪些是常见的PHP ’ 一句话木马“ ？\nA < ?php assert ($_POST(value));?>\nB <%execute(request("value"))%>\nC <?php @eval ($_POST(value)):?>\nD <%if(request.getParameter("!")!=null)(newjavio.FileOutputStream(application.getRealPath("\\") + request.getParmeter("!"))).write (request.getParameter("t").getByte())):%>\n请输入你答案：''')

print('==================答题成功！进入下一题。============================================')

G = raw_input('''第七题！以下哪个说法是正确的？\nA xcodeghost 是一种可以直接远程控制手机控制权的攻击方式\nB wormhole是一种可以直接远程控制手机控制权的攻击方式\nC ” 心脏滴血“ 是一种可以直接远程控制手机控制权的攻击方式\nD shellshock是一种可以直接远程控制手机控制权的攻击方式 \n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

H = raw_input('''第八题！\n在同一个bash 下依次执行\nroot@kali：~/Desktop#  whoami\nroot\nroot@kali：~/Desktop# function whoami() { echo 1;}\nroot@kali：~/Desktop# whoami\n请问最后一次执行的whoami 的结果是什么？\nA root\nB 1 \nC echo 1\nD echo 1;\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

I = raw_input('''第九题！\n以下哪个攻击可用来运行ddos攻击？\nA 菜刀\nB WSI\nC Dosend\nD Chkrootkit\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

J = raw_input('''第十题！\n以下哪些服务器曾被发现文件解析漏洞？\nA Apache\nB IIS\nC nginx\nD squid\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

K = raw_input('''第十一题！\n以下命令可以用来获取DNS记录的是？\nA traceroute\nB ping\nC dig\nD who\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

L = raw_input('''第十二题！\nlinux 环境下，查询日志文件最后100行数据，正确的方式是？\nA mv -100 log\nB grep -100 log\nC cat -100 log\nD tail -100 log\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

M = raw_input('''第十三题！\nFirefox浏览器插件Hacbar提供的功能\nA POST方式提交数据\nB BASE64编码和解码\nC 代理修改WEB页面的内容\nD修改浏览器访问referer\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

N = raw_input('''第十四题！\n以下哪个攻击可以提供拦截和修改http数据包功能？\nA Metasploit\nB Hackbar\nC Sqlmap \nD Burpsuite\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

O = raw_input('''第十五题！\n以下哪几种工具可以对网站进行自动化web漏洞扫描？\nA hackbar\nB AWVS\nC IBM appscan\nD Nmap\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

P = raw_input('''第十六题！\n黑客控制一台Windows服务器，发现IE浏览器使用了代理，可以访问外网，执行如下命令发现\nC:\\Users\\test>ping www.baidu.com -n 1\n正在 Pingwww.a.shifen.com [14.215.177.38]具有32字节的数据：\n请求超时\nC:\\Users\\test>telnet www.baidu.com 80\n正在链接www.baidu.com...无法打开到主机的连接。\n在端口 80: 连接失败。\n通过如上信息判断，以下哪些反弹shell操作会失败

\nA windows/meterpreter/reverse_http\nB icmp协议的后门\nC windows/meterpreter/reverse_https\nD windows/meterpreter/reverse_tcp\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

Q = raw_input('''第十七题！\n关于XcodeGhost事件的正确说法是\nA部分Android产品也受到了影响\nB应用程序开发使用了包含后门插件的IDE\nC当手机被盗时才有风险\nD苹果官方回应APPSTORE上的应用程序不受影响\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

R = raw_input('''第十八题！\nAndroid 应用中导致HTTPS中间人攻击的原因有？\nA 没有对SSL证书校验 \nB 没有对主机名进行校验\nC SSL证书被泄露\nD 使用WIFI连接网络\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

S = raw_input('''第十九题！\n这段代码存在的安全问题，会产生什么安全漏洞？\n<?php\n$username = $_GET(username);\necho $uername\nmysql_query("select * from orders where username = "$username"or dir (mysql_error():\n?>\nA 命令执行漏洞\nB SQL注入漏洞\nC 文件包含漏洞\nD 反射XSS漏洞\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

T = raw_input('''第二十题！这是最后一个选择题了，加油！\nandroid manifest.xml中哪项配置可能造成安卓内部文件被窃取？\nA android：allowbackup=“ true "\nB Android:name = " con.trsc"\nC Android: debug = " true "\nD Androidtarget sdkversion = "17"\n请输入你的答案：''')

print('==================选择题全部答题完毕！进入下一阶段！。============================================')

print('[提示：题目为五道填空题和五道判断题，请注意看题！]')

U  = raw_input('''第一题！\nsql注入（MySQL数据库）中常用的延时函数是？\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

V = raw_input('''第二题！\n Linux上查看用户ssh登陆历史的指令last，它读取的日志文件名是？\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

W = raw_input('''第三题！\n 国内历史最久的黑客安全技术峰会是？\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

X = raw_input('''第四题！\naslr是对抗什么类型攻击的技术？\n请输入你的答案：''')

print('==================答题成功！进入下一题。============================================')

Y = raw_input('''第五题！\n当访问web网站某个资源不存在时，返回的HTTP状态码是？\n请输入你的答案：''')

print('==================填空题全部答题完毕！还剩五道判断题，你只要填入 "对" 或者 "错" 即可！加油吧！。============================================')

Z = raw_input('''第一题！\nzmap单次执行可以对多个端口同时扫描\n 请输入"对"或者"错"：''')

print('==================答题成功！进入下一题。============================================')

AA = raw_input('''第二题！\nTCP和UDP协议对比，TCP传送数据更安全\n请输入"对"或者"错"：''')

print('==================答题成功！进入下一题。============================================')

BB = raw_input('''第三题！\nRedis常用的默认端口是873\n请输入"对"或者"错"：''')

print('==================答题成功！进入下一题。============================================')

CC = raw_input('''第四题！\nDES、RC4均属于对称加密算法\n请输入"对"或者"错"：''')

print('==================还剩最后一道题！加油！。============================================')

DD = raw_input('''第五题！\n写这个程序的作者是不是很帅？：）\n请输入"对"或者"错"：''')

print('''====================================\n
====================程序已判断出你的答案对错，结果如下！==================''')

print('================PS：YES为正确，NO为错误！==================')

if A == ('AD'):
    print('选择题第一题：yes')
else:
	print('选择题第一题：NO，答案为：AD')
	

if B == ('AC'):
    print('选择题第二题：yes')
else:
	print('选择题第二题：NO，答案为：AC')

	
if C == ('D'):
    print('选择题第三题：yes')
else:
	print('选择题第三题：NO，答案为：D')

	
if D == ('ABC'):
    print('选择题第四题：yes')
else:
	print('选择题第四题：NO，答案为：ABC')

	
if E == ('ABD'):
    print('选择题第五题：yes')
else:
	print('选择题第五题：NO，答案为：ABD')
	
if F == ('ABCD'):
    print('选择题第六题：yes')
else:
	print('选择题第六题：NO，答案为：ABCD')	
	
if G == ('A'):
    print('选择题第七题：yes')
else:
	print('选择题第七题：NO，答案为：A')	

if H == ('B'):
    print('选择题第八题：yes')
else:
	print('选择题第八题：NO，答案为：B')
	
if I == ('C'):
    print('选择题第九题：yes')
else:
	print('选择题第九题：NO，答案为：C')	

if J == ('ABC'):
    print('选择题第十题：yes')
else:
	print('选择题第十题：NO，答案为：ABC')		
	
if K == ('C'):
    print('选择题第十一题：yes')
else:
	print('选择题第十一题：NO，答案为：C')	
	
if L == ('D'):
    print('选择题第十二题：yes')
else:
	print('选择题第十二题：NO，答案为：D')		
	
if M == ('ABD'):
    print('选择题第十三题：yes')
else:
	print('选择题第十三题：NO，答案为：ABD')	
	
if N == ('D'):
    print('选择题第十四题：yes')
else:
	print('选择题第十四题：NO，答案为：D')	
	
if O == ('BC'):
    print('选择题第十五题：yes')
else:
	print('选择题第十五题：NO，答案为：BC')	

if P == ('ABCD'):
    print('选择题第十六题：yes')
else:
	print('选择题第十六题：NO，答案为：ABCD')	

if Q == ('AB'):
    print('选择题第十七题：yes')
else:
	print('选择题第十七题：NO，答案为：AB')	

if R == ('ABC'):
    print('选择题第十八题：yes')
else:
	print('选择题第十八题：NO，答案为：ABC')	

if S == ('ABD'):
    print('选择题第十九题：yes')
else:
	print('选择题第十九题：NO，答案为：ABD')
	
if T == ('ABC'):
    print('选择题第二十题：yes')
else:
	print('选择题第二十题：NO，答案为：ABC')	
	
print('''\n
================以上为你做的二十道选择题的结果！==================\n
''')
	
if U == ('sleep()'):
    print('填空题第一题：yes')
else:
	print('填空题第一题：NO，答案为：sleep()')		
	
if V == ('/var/log/wtmp'):
    print('填空题第二题：yes')
else:
	print('填空题第二题：NO，答案为：/var/log/wtmp')	

if W == ('Xcon'):
    print('填空题第三题：yes')
else:
	print('填空题第三题：NO，答案为：Xcon')		
	
if X == ('缓冲区溢出'):
    print('填空题第四题：yes')
else:
	print('填空题第四题：NO，答案为：缓冲区溢出')	
	
if Y == ('404'):
    print('填空题第五题：yes')
else:
	print('填空题第五题：NO，答案为：404')	

print('''\n
================以上为你做的五道填空题的结果！==================\n
''')

if Z == ('对'):
    print('判断题第一题：yes')
else:
	print('判断题第一题：NO')
	
if AA == ('错'):
    print('判断题第二题：yes')
else:
	print('判断题第二题：NO')	
	
if BB == ('错'):
    print('判断题第三题：yes')
else:
	print('判断题第三题：NO')	
	
if CC == ('对'):
    print('判断题第四题：yes')
else:
	print('判断题第四题：NO')	

if DD == ('对'):
    print('判断题第五题：yes')
else:
	print('判断题第五题：NO,作者肯定很帅:)')
	
print('''\n
================以上为你做的最后五道判断题的结果！==================\n
''')	


print('''题目已经全部做完，错了很多？没事，别灰心再接再厉！:)\n
注：以上问题以及参考答案全部来自：http://blog.csdn.net/qq_29277155/article/details/51628939\n

文章里写了关于问题的详细解释！值得一看\n

''')
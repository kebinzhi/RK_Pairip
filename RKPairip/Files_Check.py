from.C_M import CM
C=CM()
class FileCheck:
	def set_paths(A):B=C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]));A.apkeditor_path=C.os.path.join(B,'APKEditor.jar');A.apktool_path=C.os.path.join(B,'APKTool_OR.jar');A.axml2xml_jar_path=C.os.path.join(B,'axml2xml.jar');A.Objectlogger=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'Objectlogger.smali');A.baksmali=C.os.path.join(C.os.path.dirname(C.os.path.abspath(__file__)),'Bak_Smali.jar')
	def calculate_checksum(E,file_path):
		A=C.hashlib.sha256()
		try:
			with open(file_path,'rb')as B:
				for D in iter(lambda:B.read(4096),b''):A.update(D)
			return A.hexdigest()
		except FileNotFoundError:return
	def download_file(K,jar_urls_and_paths):
		H=True;import requests as F;Z=set()
		for(L,A,M)in jar_urls_and_paths:
			B=C.os.path.basename(A)
			if C.os.path.exists(A):
				N=K.calculate_checksum(A)
				if N==M:continue
				else:print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{B} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.{C.r}\n");C.os.remove(A)
			try:
				O='2.2';P='https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/setup.py'
				if(Q:=F.get(P)).status_code==200 and(R:=C.re.search('version="(.*?)"',Q.text)):
					if(S:=R.group(1))!=O:print(f"\n{C.lb}[ {C.y}Update {C.lb}]{C.c} Updating ApkPatcher to {C.g}{S}...\n\n");I=['pip','install','git+https://github.com/TechnoIndian/ApkPatcher.git']if C.os.name=='nt'else'curl -L -o ApkPatcher.sh https://github.com/TechnoIndian/ApkPatcher/releases/download/ApkPatcher/ApkPatcher.sh && chmod +x ApkPatcher.sh && ./ApkPatcher.sh';C.subprocess.run(I,shell=isinstance(I,str),check=H)
				print(f"\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B}",end='',flush=H);D=F.get(L,stream=H,timeout=10)
				if D.status_code==200:
					E=int(D.headers.get('content-length',0));T=1024;G=0
					with open(A,'wb')as U:
						for J in D.iter_content(T):G+=len(J);U.write(J);V=G/E*100 if E>0 else 0;W=G/(1024*1024);X=E/(1024*1024)if E>0 else 0;Y=f"\r{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{B} {C.g}➸❥ {V:.2f}% ({W:.2f}/{X:.2f} MB)";print(Y,end='\r')
					print(f"\n{C.g}       |\n       └──── {C.r}Downloaded ~{C.g}$ {B} Successfully. ✔\n")
				else:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{B} {C.rd}Status Code: {D.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...{C.r}\n')
			except F.exceptions.RequestException:exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{A}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{B}\n')
	def F_D(A):B=[('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/APKEditor.jar',A.apkeditor_path,'758f2f9153fff96c20260b177f025a3ca3cecc9777abdd43139a17e225724612'),('https://raw.githubusercontent.com/TechnoIndian/Objectlogger/main/Objectlogger.smali',A.Objectlogger,'ff31dd1f55d95c595b77888b9606263256f1ed151a5bf5706265e74fc0b46697')];A.download_file(B);C.os.system('cls'if C.os.name=='nt'else'clear')
	def F_D_A(B,isAPKTool,Fix_dex,isSmali):
		E=isSmali;D=Fix_dex;C=isAPKTool;A=[]
		if C or D:A.append(('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/apktool.jar',B.apktool_path,'56d59c524fc764263ba8d345754d8daf55b1887818b15cd3b594f555d249e2db'))
		if E:A.append(('https://github.com/TechnoIndian/ApkTool_Framwork/releases/download/APKTool_2.10.0/Bak_Smali.jar',B.baksmali,'418b3861efc0f3afffb10d58a244e848d34f86cbdd3261ad2a2d1d57ee663766'))
		if C or D or E:A.append(('https://github.com/TechnoIndian/RKPairip/releases/download/Editor/axml2xml.jar',B.axml2xml_jar_path,'e3a09af1255c703fc050e17add898562e463c87bb90c085b4b4e9e56d1b5fa62'))
		if A:B.download_file(A)
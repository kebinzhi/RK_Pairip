_G='ignore'
_F='utf-8'
_E=True
_D='-o'
_C='-f'
_B='-jar'
_A='java'
from.C_M import CM
C=CM()
from.Files_Check import FileCheck
F=FileCheck()
F.set_paths()
class De_Compiler:
	def decompile_apk_choice(E,apk_path,decompile_dir,isAPKTool,Fix_dex):
		B=decompile_dir;A=apk_path;print(f"\n{C.r}_____________________________________________________________\n")
		if isAPKTool or Fix_dex:D=[_A,_B,F.apktool_path,'d',_C,'-r','--only-main-classes',A,_D,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with ApkTool...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} d -f -r --only-main-classes {A} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		else:D=[_A,_B,F.apkeditor_path,'d',_C,'-no-dex-debug','-i',A,_D,B];print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile with APKEditor...");print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.apkeditor_path)} d -f -no-dex-debug -i {A} -o {C.os.path.basename(B)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
		try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
		except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile Failed ! ✘{C.r}\n");return None,None
	def Application_Name(K,L_N_S_F):
		E=C.re.compile('\\.class\\s+public\\s+Lcom/pairip/application/Application;\\s+\\.super\\s+L([^;\\s]+)',C.re.DOTALL);A=None
		for(F,L,G)in C.os.walk(L_N_S_F):
			for B in G:
				if B=='Application.smali':
					H=C.os.path.join(F,B)
					with open(H,'r',encoding=_F,errors=_G)as I:J=I.read()
					D=E.search(J)
					if D:A=D.group(1).replace(C.os.sep,'.');break
			if A:break
		return A
	def replace_application_value(E,manifest_path,old_value,new_value):
		B=manifest_path
		with open(B,'r',encoding=_F,errors=_G)as A:C=A.read()
		D=C.replace(old_value,new_value)
		with open(B,'w',encoding=_F,errors=_G)as A:A.write(D)
	def recompile_apk(G,decompile_dir,isAPKTool,build_dir):
		E='b';B=decompile_dir;A=build_dir
		if isAPKTool:
			D=[_A,_B,F.apktool_path,E,_C,B,_D,A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b -f {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool Default...{C.g}\n")
			try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:
				print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Default Recompile Failed! ✘{C.r}\n");D=[_A,_B,F.apktool_path,E,_C,'-use-aapt2',B,_D,A];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling with aapt2 ~{C.g}$ java -jar {C.os.path.basename(F.apktool_path)} b -f -use-aapt2 {C.os.path.basename(B)} -o {C.os.path.basename(A)}\n");print(f"{C.r}_____________________________________________________________{C.g}\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} ApkTool AAPT2...{C.g}\n")
				try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful with aapt2 {C.g} ✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
				except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} AAPT2 Recompile Failed! ✘{C.r}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with both Default & aapt2 ! ✘{C.r}\n")
		else:
			D=[_A,_B,F.apkeditor_path,E,'-i',B,_D,A,_C];print(f"{C.r}_____________________________________________________________\n");print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK...");print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.apkeditor_path)} b -i {C.os.path.basename(B)} -o {C.os.path.basename(A)} -f\n");print(f"{C.r}_____________________________________________________________{C.g}\n")
			try:C.subprocess.run(D,check=_E);print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔{C.r}\n");print(f"{C.r}_____________________________________________________________\n")
			except C.subprocess.CalledProcessError:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile Failed with APKEditor ! ✘{C.r}\n")
		if C.os.path.exists(A):print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} APK Successfully Created {C.g}➸❥ {C.y}{A} {C.g}✔{C.r}\n")
		else:exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Failed to Create APK at: {A} ! ✘{C.r}\n")
		print(f"{C.r}_____________________________________________________________\n")
from.C_M import CM
C=CM()
class CRC:
	def format_time(A,timestamp):return C.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
	def process_apks(I,m_skip,apk_path,build_dir,file_types):
		Q='little';P='.apk';O='.dex';J=apk_path;D=file_types;B=build_dir
		if m_skip:
			with C.zipfile.ZipFile(B,'r')as R:S=f"classes{int(sorted([A.filename for A in R.infolist()if A.filename.endswith(O)])[-1].split('classes')[1].split(O)[0])}.dex"
			input(f"\n{C.lb}[ {C.pr}FYI ! {C.lb}] {C.c} Now Script is Listen Mode, Cuz The value of your Last Dex {C.y}{S} {C.c}Field/method is greater than 65536., So you can do Max Value Dex Redivision {C.pr}( like 65536 ) {C.g}using MT/ApkTool_M then correct the name of the APK again and then press enter in the script, which will bypass CRC )\n\n\n{C.lb}[ {C.pr}CRC Fix {C.lb}] {C.c} Press Enter to After Dex Redivision & Should Apk Name is {C.y}{C.os.path.basename(B)} ...{C.r}\n")
		E=B.replace(P,P);K=0;L=[]
		try:
			with C.zipfile.ZipFile(J)as M,C.zipfile.ZipFile(B)as N:T={A.filename:A.CRC for A in M.infolist()if any(B in A.filename for B in D)};F={A.filename:A.CRC for A in N.infolist()if any(B in A.filename for B in D)};U={A.filename:A.date_time for A in M.infolist()if any(B in A.filename for B in D)};V={A.filename:A.date_time for A in N.infolist()if any(B in A.filename for B in D)}
			for(A,H)in T.items():
				if A in F and H!=F[A]:
					W=H.to_bytes(4,Q);X=F[A].to_bytes(4,Q);K+=1;Y=I.format_time(C.datetime(*U[A]).timestamp());Z=I.format_time(C.datetime(*V[A]).timestamp());L.append((A,f"{H:08x}",f"{F[A]:08x}",Y,Z))
					with open(B,'rb')as a:b=a.read()
					c=b.replace(X,W)
					with open(E,'wb')as d:d.write(c)
					B=E
		except Exception as e:print(f"{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} processing APKs: {e} ! ✘{C.r}\n");return
		print(f"\n                    ✨ {C.g}CRCFix by Kirlif ✨\n");print(f"{C.c}File Name              CRC         FIX         Modified       ")
		for G in L:print(f"\n{C.g}{G[0]:<22} {G[1]}    {G[2]}    {G[4]}\n")
		print(f"\n{C.lb}[{C.c}  INPUT  {C.lb}] {C.g}➸❥ {C.y}{J}\n");print(f"{C.lb}[{C.c}  OUTPUT  {C.lb}] {C.g}➸❥ {C.y}{E}\n");print(f"\n{C.lb}[{C.c}  CRCFix  {C.lb}] {C.g}➸❥ {C.pr}{K}{C.r}\n");return E
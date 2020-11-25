import os

print("""
Press 1. Configure webserver inside docker container
Press 2. Run python code bt stting up the python interpreter inside docker container
""")

choice=int(input("Enter your choice : "))

if choice==1:
	os.system("systemctl start docker")
	os.system("docker create -it --network host --name task72os centos")
	os.system("docker start task72os")
	os.system("docker exec -it task72os yum clean all")
	os.system("docker exec -it task72os yum install httpd -y")
	os.system("docker exec -it task72os yum install net-tools wget -y")
	os.system("docker exec -it task72os wget -O /var/www/html/a.html https://task7arth.s3.ap-south-1.amazonaws.com/a.html")
	os.system("docker exec -it task72os /usr/sbin/httpd")
	os.system("docker exec -it task72os ifconfig docker0")

elif choice==2:
	os.system("systemctl start docker")
	os.system("docker create -it --network host --name task72os2 centos")
	os.system("docker start task72os2")
	os.system("docker exec -it task72os2 yum clean all")
	os.system("docker exec -it task72os2 yum install python3 wget -y")
	os.system("docker exec -it task72os2 wget -O /a.py https://task7arth.s3.ap-south-1.amazonaws.com/a.py")
	os.system("docker exec -it task72os2 python3 a.py")

else:
	print("Invalid choice")


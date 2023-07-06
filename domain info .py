# pip install python-whois
# this is to find the domain info in the terminal by using python 
import whois

def Domain_info(link):
    Domain= whois.whois(url)
    print(f"server : {Domain.whois_server}")
    print(f"Expairation Date : {Domain.expiration_date}")
    print(f"name : {Domain.name}")
    print(f"organation : {Domain.org}")
    print(f"state : {Domain.state}")
    print(f"city : {Domain.city}")
    print(f"country : {Domain.country}")

url =input("Enter your url \n")
 
try:
    Domain = whois.whois(url)
except:
    print("this domain is avilable")
else:
    print("this domain is already purchased")
    print("Domain information\n")
    Domain_info(url)
            
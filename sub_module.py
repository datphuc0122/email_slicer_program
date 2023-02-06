from main_program import slicer , print_ans

def main():
    emails = ['datphuc0122@gmail.com','datphucdted@gmail.com','phuc.ho220120@hcmut.edu.vn']
    for email in emails:
        user_name, email_domain = slicer(email)
        print_ans(user_name, email_domain)

if __name__ =="__main__":
    main()
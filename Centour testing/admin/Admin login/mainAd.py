

if __name__ == "__main__":
    print("Admin panel open ")
    try:
        import admin_login
    except Exception as e:
        print(e)
    print("Test cases Admin login ")
    try:
        import admin_checkIn
    except Exception as e:
        print(e)
    try :
        import admin_ASSIanWork
    except Exception as e:
        print(e)
    try:
        import admin_document_voult
    except Exception as e:
        print(e)
    #
    try:
        import admin_Product
    except Exception as e :
        print(e)
    #
    try :
        import admin_add_client
    except Exception as e:
        print(e)
    #
    try:
        import admin_attendReport
    except Exception as e:
        print(e)

    # print("Every page showing a massege 'invalid crdentials '")
    try :
        import Admin_newWorkReport
    except Exception as e:
        print(e)
    # print ("add access group end ")
    # print("every page message showing invalid credentials")
    try :
        import admin_expencereport
    except Exception as e:
        print(e)
    # print("test cases add client")

    try :
        import admin_orderRe
    except Exception as e:
        print(e)
    print("test cases admin reports ")

    try :
        import admin_logout
    except Exception as e:
        print(e)
    print("Every thing is properly working")

    # try:
    #     import min_expenceRE
    # except Exception as e :
    #     print(e)
    # print("test cases Expence report")
    # try :
    #     import admin_orderRe
    # except Exception as e:
    #     print(e)
    # print("test cases order report")


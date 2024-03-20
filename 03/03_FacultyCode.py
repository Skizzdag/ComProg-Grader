def check_Faculty(code):
    faculty_code = ["01","02","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","53","55","58"]
    if code in faculty_code:
        return print("OK")
    else:
        return print("Error")
check_Faculty(input())